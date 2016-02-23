from django.db import models

from django.contrib.auth.models import User

from contest.models import Contest
from Questions.models import Question
from SkillTest.models import Skill_test



class Pool(models.Model) :
    """
    Model to store information of question's pool
    """
    contest              = models.ForeignKey(Contest, blank = True, null = True)
    tools                = models.TextField(blank = True, null = True)
    tools_exclusive      = models.BooleanField(default = False)
    pool_name            = models.CharField(max_length = 50, unique = True)
    techniques           = models.TextField(blank = True, null = True)
    techniques_exclusive = models.BooleanField(default = False)
    domains              = models.TextField(blank = True, null = True)
    domains_exclusive    = models.BooleanField(default = False)
    difficulty           = models.TextField(blank = True, null = True)
    difficulty_exclusive = models.BooleanField(default = False)
    number_of_questions  = models.IntegerField(default = 0)
    skill_test           = models.ForeignKey(Skill_test, default = 1)

    def __unicode__(self) : 
        return self.pool_name

class Question_pool(models.Model) :
    """
    Store questions for a given pool
    """
    contest = models.ForeignKey(Contest, blank = True, null = True)
    question = models.ForeignKey(Question)
    pool = models.ForeignKey(Pool)
    skill_test = models.ForeignKey(Skill_test)

    def __unicode__(self) :
        return self.pool.pool_name

class Candidate_Question_pool(models.Model) : 
    """
      Set of questions to be served to a particular user for a given skill test
    """
    contest           = models.ForeignKey(Contest, blank = True, null = True)
    skill_test        = models.ForeignKey(Skill_test)
    question          = models.ForeignKey(Question) 
    candidate         = models.ForeignKey(User)
    visited           = models.BooleanField(default = False)
    time_started      = models.DateTimeField(blank = True, null = True)
    time_completed    = models.DateTimeField(blank = True, null = True)
    time_taken        = models.IntegerField(default = 0)
    option1           = models.BooleanField(default = False) 
    option2           = models.BooleanField(default = False) 
    option3           = models.BooleanField(default = False) 
    option4           = models.BooleanField(default = False) 
    option5           = models.BooleanField(default = False) 
    option6           = models.BooleanField(default = False) 
    fill_ups_answer   = models.CharField(max_length = 120,blank = True, null = True)
    is_correct        = models.BooleanField(default = False)
    score             = models.FloatField(default = 0)


    def __unicode__(self) : 
        return self.candidate , self.question, self.contest, self.skill_test
