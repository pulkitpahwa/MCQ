from django.shortcuts import render
from contest.models import Contest
from django.shortcuts import render_to_response 
from django.template import RequestContext
from django.shortcuts import HttpResponseRedirect
from django.core.urlresolvers import reverse 


def create(request) : 
    if request.method == "GET" : 
        return render_to_response("contest/create.html",{}, context_instance = RequestContext(request))
    else : 
        name = request.POST['name']
        contest = Contest.objects.create(contest_name = name)
        return HttpResponseRedirect("/mcq/" + contest.slug + "/create-pool")



