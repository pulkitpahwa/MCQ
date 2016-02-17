from django.shortcuts import render, render_to_response
from django.template import RequestContext 
from Questions.models import Question, Tool_tags, Technique_tags, Domain_tags, Difficulty_tags

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


def find_questions_with_given_tags(request) :
    if request.method == "GET" :
        return render_to_response("form.html",{}, context_instance = RequestContext(request))
    else :
        req_domain_tags     = [i.lstrip().rstrip() for i in request.POST['domain'].split(",")]
        req_tools_tags      = [i.lstrip().rstrip() for i in request.POST['tools'].split(",")]
        req_techniques_tags = [i.lstrip().rstrip() for i in request.POST['techniques'].split(",")]
        req_difficulty_tags = [i.lstrip().rstrip() for i in request.POST['difficulty'].split(",")]

        tooltags = Tool_tags.objects.all().values_list("tag__name", flat = True)
        domaintags = Domain_tags.objects.all().values_list("tag__name", flat = True)
        techniquetags = Technique_tags.objects.all().values_list("tag__name", flat = True)
        difficultytags = Difficulty_tags.objects.all().values_list("tag__name", flat = True)

        non_req_tool_tags = list( set(tooltags) - set(req_tools_tags) )
        non_req_technique_tags = list( set(techniquetags) - set(req_techniques_tags) )
        non_req_domain_tags =  list( set(domaintags) - set(req_domain_tags) )
        non_req_difficulty_tags = list(set(difficultytags) - set(req_difficulty_tags) )

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
            result = result.exclude(tools__name__in = non_req_tool_tags)
        if 'techniques_exclude' in request.POST :
            result = result.exclude(techniques__name__in = non_req_technique_tags)
        if 'domain_exclude' in request.POST :
            result = result.exclude(domains__name__in = non_req_domain_tags)
        if 'difficulty_exclude' in request.POST :
            result = result.exclude(difficulty__name__in = non_req_difficulty_tags)

        count = len(result)
        return render_to_response("result.html",{"tools" : req_tools_tags, "domains" : req_domain_tags,
            "techniques" : req_techniques_tags, "difficulty": req_difficulty_tags, "result" : result,"count" : count},
                                 context_instance = RequestContext(request))


