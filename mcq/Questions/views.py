from django.shortcuts import render, render_to_response
from django.template import RequestContext 
from django.utils.crypto import get_random_string
from django.http import HttpResponse, HttpResponseRedirect

from Questions.models import Question, Tool_tags, Technique_tags, Domain_tags, Difficulty_tags, Options
from contest.models import Contest
from QuestionsPool.models import Pool, Question_pool

import csv
import json

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
                answer = [ i for i in rows[6].replace(", ", ",").split(",")]
                difficulty = [i for i in rows[7].replace(", ", ",").split(",")]
                tools =   [i for i in rows[8].replace(", ", ",").split(",")]
                techniques = [i for i in rows[9].replace(", ", ",").split(",")]
                domain = [i for i in rows[10].replace(", ", ",").split(",")]
                multiple_true = len(answer) > 1
                ques = Question.objects.create(  question = description,  multiple_true = multiple_true )
                for i in tools : 
                    ques.tools.add(i)
                for i in techniques : 
                    ques.techniques.add(i)
                for i in domain :
                    ques.domains.add(i)
                for i in difficulty : 
                    ques.difficulty.add(i)
                a_true = 'A' in answer
                b_true = 'B' in answer
                c_true = 'C' in answer
                d_true = 'D' in answer
                option1 = Options.objects.create(question = ques, option = rows[2], is_solution = a_true ) 
                option2 = Options.objects.create(question = ques, option = rows[3], is_solution = b_true )
                option3 = Options.objects.create(question = ques, option = rows[4], is_solution = c_true )
                option4 = Options.objects.create(question = ques, option = rows[5], is_solution = d_true )
        return HttpResponse("done")


def count_questions_with_given_tags(request, contest) :
    """
    This method is used to find the number of questions with the given tag set.
    """
    try : 
        contest = Contest.objects.get(slug = contest)
    except : 
        return HttpResponse("no such contest")
    if request.method == "GET" :
        return render_to_response("form.html",{"contest":contest}, context_instance = RequestContext(request))
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

def save_questions_with_given_tags(request, contest) :
    """
    This method is used to find the number of questions with the given tag set.
    """
    try : 
        contest = Contest.objects.get(slug = contest)
    except : 
        return HttpResponse("no such contest")
    if request.method == "GET" :
        return render_to_response("form.html",{"contest":contest}, context_instance = RequestContext(request))
    else :
        number_of_questions = int(request.POST['number_of_questions'])
        #count number of pools for the given contest 
        number_of_pools_of_this_contest = Pool.objects.filter(contest = contest).count() 
        pool_name = contest.slug + str(number_of_pools_of_this_contest + 1)

        pool = Pool.objects.create(contest = contest, number_of_questions = number_of_questions,pool_name  = pool_name )

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
            Question_pool.objects.create(contest = pool.contest, pool = pool, question = i)

        return HttpResponse("Your pool created")
#        return render_to_response("result.html",{"tools" : req_tools_tags, "domains" : req_domain_tags,
#            "techniques" : req_techniques_tags, "difficulty": req_difficulty_tags, "result" : result,"count" : count},
#                                 context_instance = RequestContext(request))


