from django.shortcuts import render

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
# Create your views here.
