from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from SkillTest.models import Skill_test, Test_participant
from contest.models import Contest
from QuestionsPool.models import Candidate_Question_pool, Question_pool, Pool
from Questions.models import Question, Options

import datetime
import random

@login_required
def particular_skill_test(request, skill_test_slug) : 
    """
      Checks if the skill test exist. If not exist, return error. else, return test_participant, and take the user 
      to hackathon home.
    """
    try : 
        skill_test = Skill_test.objects.get(slug = skill_test_slug)
        #check if the user has joined the hackathon
        try :
            test_participant = Test_participant.objects.get(participant = request.user, skill_test = skill_test)
            return render_to_response("Skill_test/skill_test_home_registered.html",
                       {"skill_test":skill_test, "participant" : test_participant},
                       context_instance = RequestContext(request))
        except Test_participant.DoesNotExist : 
            return render_to_response("Skill_test/join_skill_test.html", {"skill_test":skill_test}, 
                  context_instance = RequestContext(request))
    except Skill_test.DoesNotExist: 
        return HttpResponse("NO such test found")

@login_required
def join_skill_test(request, skill_test_slug) : 
    """
      This method allows the user to join a skill test. 
      Once the user has joined the skill test, the set of questions to be served to him are created and his timer is started.
      The questions are then served to him.
    """
    try : 
        skill_test = Skill_test.objects.get(slug = skill_test_slug)
        #check if the user has joined the hackathon
        try :
            user = request.user  #change this with your own user model 
            test_participant = Test_participant.objects.get(participant = user, skill_test = skill_test)
            return HttpResponse(json.dumps({"error":"true","message":"You have already joined the test."}),
                 content_type = "application/json")
        except Test_participant.DoesNotExist: 
            # create model entry for this user in model Test_participant
            user = request.user
            test_participant = Test_participant.objects.create(skill_test = skill_test, participant = user )

            # create pool of questions that will be served to this user.
            pools = Pool.objects.filter(skill_test = skill_test)
            for pool in pools : 
                number_of_questions = pool.number_of_questions 
                question_ids_in_pool = list( Question_pool.objects.filter(pool = pool).values_list("id", flat = True) )
                random_ids = random.sample(question_ids_in_pool, number_of_questions)
                questions_set = Question.objects.filter(id__in = random_ids)
                for question in questions_set : 
                    c = Candidate_Question_pool.objects.create(contest = skill_test.contest, skill_test = skill_test, 
                            question = question, candidate = user)

            # save start time and return the user to questions page.
            skill_test.start_time = datetime.datetime.now()
            skill_test.save()
            return HttpResponseRedirect("Redirect to skilltest home with mcq")
    except Skill_test.DoesNotExist : 
        return HttpResponse("NO such test found")


def mcq_home( request, skill_test_slug, question_id ) :
    """
     MCQ home for a particular skill test. 
     Will serve questions to the user.
     The sidebar will contains the list of all questions. The main screen will serve one MCQ at a time
    """
    try : 
        question = Question.objects.get(question_id = question_id)
        options = Options.objects.filter(question = question)
        return HttpResponse(json.dumps({"question" : question, "options" : options}), content_type = "application/json")
    except Question.DoesNotExist : 
        return HttpResponse(json.dumps({"error":"true", "message" : "No MCQ exist. Invalid URL"}), 
                content_type = "application/json")


