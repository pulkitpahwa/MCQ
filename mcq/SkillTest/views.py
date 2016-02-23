from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.models import User

from SkillTest.models import Skill_test, Test_participant
from contest.models import Contest
from QuestionsPool.models import Candidate_Question_pool, Question_pool, Pool
from Questions.models import Question, Options

import datetime
import random
import json

#@login_required 
def create_skill_test(request) : 
    if request.method == "GET" :
        return render_to_response("SkillTest/create.html",{}, context_instance = RequestContext(request))
    else:
        name = request.POST['name']
        skill_test = Skill_test.objects.create(name = name)
        return HttpResponseRedirect("/mcq/" + skill_test.slug + "/create-pool")

def count_questions_with_given_tags(request, skill_test) :
    """
    This method is used to find the number of questions with the given tag set.
    """
    try : 
        skill_test = Skill_test.objects.get(slug = skill_test)
    except Skill_test.DoesNotExist: 
        return HttpResponse("no such contest")
    if request.method == "GET" :
        return render_to_response("form.html",{"skilltest":skill_test}, context_instance = RequestContext(request))
    else :
        number_of_questions = int(request.POST['number_of_questions'])
        req_domain_tags     = [i.lstrip().rstrip() for i in request.POST['domain'].split(",")]
        req_tools_tags      = [i.lstrip().rstrip() for i in request.POST['tools'].split(",")]
        req_techniques_tags = [i.lstrip().rstrip() for i in request.POST['techniques'].split(",")]
        req_difficulty_tags = [i.lstrip().rstrip() for i in request.POST['difficulty'].split(",")]


        result = Question.objects.all()
        for i in req_tools_tags : 
            if not i == "" :
                result = result.filter(tools__name__in = [i])
        for i in req_techniques_tags : 
            if not i == "" :
                result = result.filter(techniques__name__in = [i])
        for i in req_domain_tags :
            if not i == "" :
                result = result.filter(domains__name__in = [i])
        for i in req_difficulty_tags : 
            if not i == "" :
                result = result.filter(difficulty__name__in = [i])


        if 'tools_exclude' in request.POST :
            tooltags = Tool_tags.objects.all().values_list("tag__name", flat = True)
            non_req_tool_tags = list( set(tooltags) - set(req_tools_tags) )
            result = result.exclude(tools__name__in = non_req_tool_tags)
            tools_exclude = True 
        else : 
            tools_exclude = False

        if 'techniques_exclude' in request.POST :
            techniquetags = Technique_tags.objects.all().values_list("tag__name", flat = True)
            non_req_technique_tags = list( set(techniquetags) - set(req_techniques_tags) )
            result = result.exclude(techniques__name__in = non_req_technique_tags)
            techniques_exclude = True 
        else : 
            techniques_exclude = False 

        if 'domain_exclude' in request.POST :
            domaintags = Domain_tags.objects.all().values_list("tag__name", flat = True)
            non_req_domain_tags =  list( set(domaintags) - set(req_domain_tags) )
            result = result.exclude(domains__name__in = non_req_domain_tags)
            domain_exclude = True 
        else : 
            domain_exclude = False 

        if 'difficulty_exclude' in request.POST :
            difficultytags = Difficulty_tags.objects.all().values_list("tag__name", flat = True)
            non_req_difficulty_tags = list(set(difficultytags) - set(req_difficulty_tags) )
            result = result.exclude(difficulty__name__in = non_req_difficulty_tags)
            difficulty_exclude = True 
        else : 
            difficulty_exclude = False 

        count = len(result)

        return HttpResponse(json.dumps({"count" : count, "number_of_questions":number_of_questions, 
            "tools" : req_tools_tags, "techniques" : req_techniques_tags, "domains":req_domain_tags,
            "difficulty":req_difficulty_tags,"tools_exclude" : tools_exclude, 'techniques_exclude' : techniques_exclude, 
            'difficulty_exclude' :difficulty_exclude,"domain_exclude" : domain_exclude}),
            content_type = "application/json")

#@login_required
def save_questions_with_given_tags(request, skill_test) :
    """
    This method is used to find the number of questions with the given tag set.
    """
    try : 
        skilltest = Skill_test.objects.get(slug = skill_test)
    except Skill_test.DoesNotExist: 
        return HttpResponse("no such contest")

    if request.method == "GET" :
        return render_to_response("form.html",{"skilltest": skilltest}, context_instance = RequestContext(request))
    else :
        number_of_questions = int(request.POST['number_of_questions'])
        #count number of pools for the given contest 
        number_of_pools_of_this_skill_test = Pool.objects.filter(skill_test = skilltest).count() 
        pool_name = skilltest.slug + str(number_of_pools_of_this_skill_test + 1)

        pool = Pool.objects.create(number_of_questions = number_of_questions,pool_name  = pool_name, skill_test = skilltest )

        tools = request.POST['tools_response']
        techniques = request.POST['techniques_response']
        domains = request.POST['domain_response']
        difficulty = request.POST['difficulty_response']

        pool.tools = tools 
        pool.techniques = techniques 
        pool.domains = domains 
        pool.difficulty = difficulty 

        req_domain_tags     = [i.lstrip().rstrip() for i in domains.split(",")]
        req_tools_tags      = [i.lstrip().rstrip() for i in tools.split(",")]
        req_techniques_tags = [i.lstrip().rstrip() for i in techniques.split(",")]
        req_difficulty_tags = [i.lstrip().rstrip() for i in difficulty.split(",")]


        result = Question.objects.all()
        for i in req_tools_tags : 
            if not i == "" :
                result = result.filter(tools__name__in = [i])
        for i in req_techniques_tags : 
            if not i == "" :
                result = result.filter(techniques__name__in = [i])
        for i in req_domain_tags :
            if not i == "" :
                result = result.filter(domains__name__in = [i])
        for i in req_difficulty_tags : 
            if not i == "" :
                result = result.filter(difficulty__name__in = [i])


        if 'tools_exclude' in request.POST :
            tooltags = Tool_tags.objects.all().values_list("tag__name", flat = True)
            non_req_tool_tags = list( set(tooltags) - set(req_tools_tags) )
            result = result.exclude(tools__name__in = non_req_tool_tags)
            tools_exclude = True 
        else : 
            tools_exclude = False

        if 'techniques_exclude' in request.POST :
            domaintags = Domain_tags.objects.all().values_list("tag__name", flat = True)
            non_req_technique_tags = list( set(techniquetags) - set(req_techniques_tags) )
            result = result.exclude(techniques__name__in = non_req_technique_tags)
            techniques_exclude = True 
        else : 
            techniques_exclude = False 

        if 'domain_exclude' in request.POST :
            techniquetags = Technique_tags.objects.all().values_list("tag__name", flat = True)
            non_req_domain_tags =  list( set(domaintags) - set(req_domain_tags) )
            result = result.exclude(domains__name__in = non_req_domain_tags)
            domain_exclude = True 
        else : 
            domain_exclude = False 

        if 'difficulty_exclude' in request.POST :
            difficultytags = Difficulty_tags.objects.all().values_list("tag__name", flat = True)
            non_req_difficulty_tags = list(set(difficultytags) - set(req_difficulty_tags) )
            result = result.exclude(difficulty__name__in = non_req_difficulty_tags)
            difficulty_exclude = True 
        else : 
            difficulty_exclude = False 

        pool.tools_exclusive = tools_exclude 
        pool.techniques_exclusive = techniques_exclude 
        pool.domains_exclusive = domain_exclude 
        pool.difficulty_exclusive = difficulty_exclude 
        pool.save()

        count = len(result)
        if count < number_of_questions : 
            pools.number_of_questions = count 
            pools.save()

        for i in result : 
            Question_pool.objects.create(skill_test = pool.skill_test, pool = pool, question = i)

        return HttpResponse("Your pool created")
#        return render_to_response("result.html",{"tools" : req_tools_tags, "domains" : req_domain_tags,
#            "techniques" : req_techniques_tags, "difficulty": req_difficulty_tags, "result" : result,"count" : count},
#                                 context_instance = RequestContext(request))

#################################################the process of creating skill test ends here.  candidate's process starts from now ###################################

#@login_required
def particular_skill_test(request, skill_test) : 
    """
      Checks if the skill test exist. If not exist, return error. else, return test_participant, and take the user 
      to hackathon home.
    """
    try : 
        skill_test = Skill_test.objects.get(slug = skill_test)
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

#@login_required
def join_skill_test(request, skill_test) : 
    """
    This method allows the user to join a skill test. 
    Once the user has joined the skill test, the set of questions to be served are created 
    The questions are then served to him.
    """
    try : 
        skill_test = Skill_test.objects.get(slug = skill_test)
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
            #This was discussed that the timer should start only when the user has started timer,i.e. there should be a 
            #seperate option to start skill test. But,I am saying that we should provide the user the FAQs and warning
            #that once started, you can't stop the timer.
            skill_test.start_time = datetime.datetime.now()
            skill_test.save()
            return HttpResponseRedirect(reverse('questions-playground', kwargs = {"skill_test":skill_test.slug}))
    except Skill_test.DoesNotExist : 
        return HttpResponse("NO such test found")

#@login_required        
def playground(request, skill_test) :
    try : 
        skill_test = Skill_test.objects.get(slug = skill_test)
        try : 
            user  = request.user 
            participant = Test_participant.objects.get(skill_test = skill_test, participant = user)
            mcqs_set = Candidate_Question_pool.objects.filter(candidate = participant, skill_test = skill_test)
            return render_to_response("SkillTest/playground.html",{"skilltest":skill_test, "mcqs" : mcqs_set},
                    context_instance = RequestContext(request))
        except Test_participant.DoesNotExist :
            return HttpResponseRedirect(reverse('join_skill_test', kwargs = {"skill_test":skill_test.slug}))

    except Skill_test.DoesNotExist : 
        return render_to_response("SkillTest/skill_test_not_found.html",{}, 
                context_instance = RequestContext(request))



def particular_mcq( request, skill_test_slug, question_id ) :
    """
     MCQ home for a particular skill test. 
     Will serve questions to the user.
     The sidebar will contains the list of all questions. The main screen will serve one MCQ at a time
    """
    try : 
        skill_test = Skill_test.objects.get(slug = skill_test_slug)
        try : 
            question = Question.objects.get(question_id = question_id)
            try : 
                user = request.user    #change this with your custom user model
                candidate_Question_pool = Candidate_Question_pool.objects.get(skill_test = skill_test, 
                        question = question, candidate = user)
                options = Options.objects.filter(question = question)
                return HttpResponse(json.dumps({"question" : question, "options" : options}), content_type = "application/json")

            except Candidate_Question_pool.DoesNotExist : 
                return HttpResponse(json.dumps({"error":"true","message":"This question does not exist for you."}),
                        content_type = "application/json")
        except Question.DoesNotExist : 
            return HttpResponse(json.dumps({"error":"true","message" : "No such MCQ exist. Invalid URL"}), 
                    content_type = "application/json")

    except Skill_test.DoesNotExist : 
        return HttpResponse(json.dumps({"error":"true", "message" : "No such Skill_test exist. Invalid URL"}), 
                content_type = "application/json")

