from django.db import models

from django.contrib.auth.models import User

from contest.models import Contest
from Questions.models import Question
from SkillTest.models import Skill_test



class Pool(models.Model) :
    """
    Model to store information of question's pool
    """
    contest              = models.ForeignKey(Contest)
    tools                = models.TextField(blank = True, null = True)
    tools_exclusive      = models.BooleanField(default = False)
    pool_name            = models.CharField(max_length = 50, unique = True)
    techniques           = models.TextField(blank = True, null = True)
    techniques_exclusive = models.BooleanField(default = False)
    domains              = models.TextField(blank = True, null = True)
    domains_exclusive    = models.BooleanField(default = False)
    difficulty           = models.TextField(blank = True, null = True)
    difficulty_exclusive = models.BooleanField(default = False)
    number_of_questions = models.IntegerField(default = 0)

    def __unicode__(self) : 
        return self.pool_name

class Question_pool(models.Model) :
    """
    Store questions for a given pool
    """
    contest = models.ForeignKey(Contest)
    question = models.ForeignKey(Question)
    pool = models.ForeignKey(Pool)

    def __unicode__(self) :
        return self.pool.pool_name

class Candidate_Question_pool(models.Model) : 
    """
      Set of questions to be served to a particular user for a given skill test
    """
    contest    = models.ForeignKey(Contest, blank = True, null = True)
    skill_test = models.ForeignKey(Skill_test)
    question   = models.ForeignKey(Question) 
    candidate  = models.ForeignKey(User)

    def __unicode__(self) : 
        return self.contest, self.question
