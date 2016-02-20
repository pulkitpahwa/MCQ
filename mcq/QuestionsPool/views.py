from django.shortcuts import render, render_to_response
from django.template import RequestContext 
from django.http import HttpResponse

from QuestionsPool.models import Pool 

def pool_cache(request, pool_name) : 
    try : 
        pool = Pool.objects.get(pool_name = pool_name)
        return render_to_response("Pool/pool_info.html",{"pool":pool}, context_instance = RequestContext(request))
    except : 
        return HttpResponse("No such pool exist")

