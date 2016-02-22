from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from SkillTest.models import Skill_test, Test_participant
from contest.models import Contest

import datetime

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
            test_participant = Test_participants.objects.get(participant = request.user, skill_test = skill_test)
            return render_to_response("Skill_test/skill_test_home_registered.html",
                       {"skill_test":skill_test, "participant" : test_participant},
                       context_instance = RequestContext(request))
        except : 
            return render_to_response("Skill_test/join_skill_test.html", {"skill_test":skill_test}, 
                  context_instance = RequestContext(request))
    except : 
        return HttpResponse("NO such test found")

@login_required
def join_skill_test(request, skill_test_slug) : 
    try : 
        skill_test = Skill_test.objects.get(slug = skill_test_slug)
        #check if the user has joined the hackathon
        try :
            test_participant = Test_participants.objects.get(participant = request.user, skill_test = skill_test)
            return HttpResponse(json.dumps({"error":"true","message":"You have already joined the test."}),
                 content_type = "application/json")
        except : 
            # create model entry for this user in model Test_participant
            test_participant = Test_participants.objects.create(skill_test = skill_test, participant = user, 
                start_time = datetime.datetime.now())
            # create pool of questions that will be served to this user.
            # save start time and return the user to questions page.
    except : 
        return HttpResponse("NO such test found")

