from django.db import models
from contest.models import Contest
from Questions.models import Question

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
