from django.db import models
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase
from contest.models import Contest 
from django.contrib.auth.models import User

class Tool_tags(TaggedItemBase) :
    """
    Tools tags' custom through model
    """
    content_object = models.ForeignKey('Question')


class Technique_tags(TaggedItemBase) :
    """
    Technique tags custom through model
    """
    content_object = models.ForeignKey('Question')

class Domain_tags(TaggedItemBase) :
    """
    Domain tags' custom through model
    """
    content_object = models.ForeignKey('Question')

class Difficulty_tags(TaggedItemBase) :
    """
    Difficulty tags' custom through model
    """
    content_object = models.ForeignKey('Question')

class Question(models.Model) : 
    """
    Model for questions. 
    """
    TYPE_CHOICE = (
            ('choices', 'Multiple Choices'),
            ('fill_ups', 'Fill Right Answer'),
    )
    FILL_UPS_CHOICE = (
            ('string', 'Text'),
            ('int', 'Integer'),
            ('float', 'Float'),
    )
    question       = models.TextField()
    description    = models.TextField(blank = True, null = True)
    multiple_true  = models.BooleanField(default = False)
    tools          = TaggableManager(through = Tool_tags, related_name = "tools",verbose_name = "tools")
    techniques     = TaggableManager(through = Technique_tags, related_name = "techniques", verbose_name = "techniques")
    domains        = TaggableManager(through = Domain_tags, related_name = "domains", verbose_name = "domains")
    difficulty     = TaggableManager(through = Difficulty_tags, related_name = "difficulty", verbose_name = "difficulty")
#    question_unique_id  = models.CharField(max_length = 12, unique = True)
    approved       = models.BooleanField(default = False) #the question has to be approved to be available for shortlisting
    author         = models.ForeignKey(User, blank = True, null = True)
    question_type  = models.CharField(max_length = 10, blank = True, null = True, choices = TYPE_CHOICE, default = 'choices')
    fill_ups_correct_ans = models.CharField(max_length = 100, blank = True, null = True) 
    fill_ups_type = models.CharField(max_length = 10, blank = True, null = True, choices = FILL_UPS_CHOICE)

    def __unicode__(self):
        return self.question

class Options(models.Model) : 
    """
    Model to store options for a given question.
    """
    OPTION_CHOICE = (
            ('text', 'Text'),
            ('image', 'Image'),
            )
    question = models.ForeignKey(Question)
    option_type = models.CharField(max_length = 5, choices = OPTION_CHOICE, default = 'text')
    option_image = models.FileField(upload_to = "options", blank = True, null = True)
    option = models.TextField(blank = True, null = True)
    is_solution = models.BooleanField(default = False)
#    option_id = models.CharField(max_length = 12, unique = True)


    def __unicode__(self):
        return self.option
#
#class Pool(models.Model) :
#    """
#    Model to store information of question's pool
#    """
#    contest              = models.ForeignKey(Contest)
#    tools                = models.TextField(blank = True, null = True)
#    tools_exclusive      = models.BooleanField(default = False)
#    pool_name            = models.CharField(max_length = 50, unique = True)
#    techniques           = models.TextField(blank = True, null = True)
#    techniques_exclusive = models.BooleanField(default = False)
#    domains              = models.TextField(blank = True, null = True)
#    domains_exclusive    = models.BooleanField(default = False)
#    difficulty           = models.TextField(blank = True, null = True)
#    difficulty_exclusive = models.BooleanField(default = False)
#
#    def __unicode__(self) : 
#        return self.pool_name
#
#class Question_pool(models.Model) :
#    """
#    Store questions for a given pool
#    """
#    contest = models.ForeignKey(Contest)
#    question = models.ForeignKey(Question)
#    pool = models.ForeignKey(Pool)
#
#    def __unicode__(self) :
#        return self.pool


class Particpations(models.Model) : 
    """
    Model to store the list of mcqs a user has participated.
    """
    user = models.ForeignKey(User)
    mcq  = models.ForeignKey(Question)
    contest = models.ForeignKey(Contest)
    start_time = models.DateTimeField(blank = True, null = True)
    end_time = models.DateTimeField(blank = True, null = True)
    time_taken = models.IntegerField(default = 0) #this time is in seconds
    option1 = models.BooleanField(default = False)
    option2 = models.BooleanField(default = False)
    option3 = models.BooleanField(default = False)
    option4 = models.BooleanField(default = False)
    option5 = models.BooleanField(default = False)
    is_correct = models.BooleanField(default = False)
    score      = models.FloatField(default = 0)
    
    def __unicode__(self):
        return self.user, self.mcq, self.contest
