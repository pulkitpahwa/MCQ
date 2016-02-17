from django.shortcuts import render, render_to_response
from django.template import RequestContext 
from django.utils.crypto import get_random_string

from Questions.models import Question, Tool_tags, Technique_tags, Domain_tags, Difficulty_tags, Options

import csv

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

def find_unique_id() : 
    unique_id = get_random_string(length = 12)
    try : 
        question = Question.objects.get(question_unique_id = unique_id)
        unique_id = find_unique_id()
        return unique_id
    except : 
        return unique_id

def find_option_id() : 
    unique_id = get_random_string(length = 12)
    try : 
        options = Options.objects.get(option_id = unique_id)
        unique_id = find_option_id()
        return unique_id
    except : 
        return unique_id


def add_questions_from_csv(request) : 
    """
    Use this method to add multiple questions from a csv file. 
    Sample format of csv file : staticfiles/sample_mcq.csv
    Currently the image upload option is not available in this method.
    """
    if request.method == "GET" :
        return render_to_response("create_questions_from_csv.html",{}, context_instance = RequestContext(request))
    else : 
        csv_file = request.FILES['csv_file']
        with csv_file as f : 
            data = csv.reader(f)
            for rows in data : 
                description = rows[1]
                answer = [ i.lstrip().rstrip() for i in rows[6].split(",")]
                difficulty = [i.lstrip().rstrip() for i in rows[7].split(",")]
                tools = [i.lstrip().rstrip() for i in rows[8].split(",")]
                techniques = [i.lstrip().rstrip() for i in rows[9].split(",")]
                domain = [i.lstrip().rstrip() for i in rows[10].split(",")]
                multiple_true = len(answer) > 1
                ques = Question.objects.create(  question = description, question_unique_id = find_unique_id(), multiple_true = multiple_true )
                for i in tools : 
                    ques.tools.add(i)
                for i in techniques : 
                    ques.techniques.add(i)
                for i in domain :
                    ques.domains.add(i)
                for i in difficulty : 
                    ques.difficulty.add(i)
                option1 = Options.objects.create(question = ques, option = rows[2], is_solution = 'A' in answer, option_id = find_option_id() ) 
                option2 = Options.objects.create(question = ques, option = rows[3], is_solution = 'B' in answer, option_id = find_option_id() ) 
                option3 = Options.objects.create(question = ques, option = rows[4], is_solution = 'C' in answer, option_id = find_option_id() ) 
                option4 = Options.objects.create(question = ques, option = rows[5], is_solution = 'D' in answer, option_id = find_option_id() ) 
        return HttpResponse("done")



                

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


