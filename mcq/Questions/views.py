from django.shortcuts import render, render_to_response
from django.template import RequestContext 
from Questions.models import Question, ToolTags, TechniqueTags, DomainTags, DifficultyTags

# to filter out questions where tools = ['Python', 'Django'], techniques = ['pandas', 'scipy'], domains = ['xyz'], difficulty = 'beginner' : 
#    result = Question.objects.all()
#    req_tools_tags = ["Python", "Django"]
#    tooltags = ToolTags.objects.all().values_list("tag__name", flat = True)
#    non_req_tool_tags = set(tooltags) - set(req_tools_tags)
#    
#    req_techniques_tags = ["pandas", "scipy"]
#    techniquetags = TechniqueTags.objects.all().values_list("tag__name", flat = True)
#    non_req_technique_tags = set(techniquetags) - set(req_techniques)
#
#    req_domain_tags = ["xyz"]
#    domaintags = DomainTags.objects.all().values_list("tag__name", flat = True)
#    non_req_domain_tags = set(domaintags) - set(req_domain_tags)
#    
#    req_difficulty_tags = ["beginner"]
#    difficultytags = DifficultyTags.objects.all().values_list("tag__name", flat = True)
#    non_req_difficulty_tags = set(difficultytags) - set(req_difficulty_tags)
#
#    result = Question.objects.all().exclude(tools__name__in = non_req_tool_tags, techniques__name__in = non_req_technique_tags, 
#                                      domains__name__in = non_req_domain_tags, difficulty__name__in = non_req_domain_tags ).distinct()
#    for i in req_tools_tags : 
#         result = result.filter(tools__name__in = [i])
#    for i in req_techniques_tags : 
#        result = result.filter(techniques__name__in = [i])
#    for i in req_domain_tags :
#        result = result.filter(domains__name__in = [i])
#    for i in req_difficulty_tags : 
#        result = result.filter(domains__name__in = [i])
#
#

def find_questions_with_given_tags(request) :
    if request.method == "GET" :
        return render_to_response("form.html",{}, context_instance = RequestContext(request))
    else :
        req_domain_tags     = request.POST['domain'].split(",")
        req_tools_tags      = request.POST['tools'].split(",")
        req_techniques_tags = request.POST['techniques'].split(",")
        req_difficulty_tags = request.POST['difficulty'].split(",")

        tooltags = ToolTags.objects.all().values_list("tag__name", flat = True)
        domaintags = DomainTags.objects.all().values_list("tag__name", flat = True)
        techniquetags = TechniqueTags.objects.all().values_list("tag__name", flat = True)
        difficultytags = DifficultyTags.objects.all().values_list("tag__name", flat = True)

        non_req_tool_tags = list( set(tooltags) - set(req_tools_tags) )
        non_req_technique_tags = list( set(techniquetags) - set(req_techniques_tags) )
        non_req_domain_tags =  list( set(domaintags) - set(req_domain_tags) )
        non_req_difficulty_tags = list(set(difficultytags) - set(req_difficulty_tags) )


        result = Question.objects.all()
        for i in req_tools_tags : 
            result = result.filter(tools__name__in = [i]).exclude(tools__name__in = non_req_tool_tags)
        for i in req_techniques_tags : 
            result = result.filter(techniques__name__in = [i]).exclude(techniques__name__in = non_req_technique_tags)
        for i in req_domain_tags :
            result = result.filter(domains__name__in = [i]).exclude(domains__name__in = non_req_domain_tags)
        for i in req_difficulty_tags : 
            result = result.filter(difficulty__name__in = [i]).exclude(difficulty__name__in = non_req_difficulty_tags)


        print "result = ", result
        return render_to_response("result.html",{"tools" : req_tools_tags, "domains" : req_domain_tags,
            "techniques" : req_techniques_tags, "difficulty": req_difficulty_tags, "result" : result,
            "non_tools" : non_req_tool_tags, "non_techniques" : non_req_technique_tags, "non_domains" : non_req_domain_tags, "non_difficulty":non_req_difficulty_tags}, 
                                 context_instance = RequestContext(request))


