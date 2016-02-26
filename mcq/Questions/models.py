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
    question             = models.TextField()
    description          = models.TextField(blank = True, null = True)
    multiple_true        = models.BooleanField(default = False)
    tools                = TaggableManager(through = Tool_tags, related_name = "tools",verbose_name = "tools")
    techniques           = TaggableManager(through = Technique_tags, related_name = "techniques", verbose_name = "techniques")
    domains              = TaggableManager(through = Domain_tags, related_name = "domains", verbose_name = "domains")
    difficulty           = TaggableManager(through = Difficulty_tags, related_name = "difficulty", verbose_name = "difficulty")
#    question_unique_id  = models.CharField(max_length = 12, unique = True)
    approved             = models.BooleanField(default = False) #the question has to be approved to be available for shortlisting
    author               = models.ForeignKey(User, blank = True, null = True)
    question_type        = models.CharField(max_length = 10, blank = True, null = True, choices = TYPE_CHOICE, default = 'choices')
    fill_ups_correct_ans = models.CharField(max_length = 100, blank = True, null = True) 
    fill_ups_type        = models.CharField(max_length = 10, blank = True, null = True, choices = FILL_UPS_CHOICE)
    avg_time             = models.IntegerField(blank = True, null = True)  #avg time taken to solve the mcq. in seconds
    accuracy             = models.FloatField(blank = True, null = True)   #avg accuracy of solving the contest

    def __unicode__(self):
        return str(self.question)

class Options(models.Model) : 
    """
    Model to store options for a given question.
    """
    OPTION_CHOICE = (
            ('text', 'Text'),
            ('image', 'Image'),
            )
    question          = models.ForeignKey(Question)
    option_type       = models.CharField(max_length = 5, choices = OPTION_CHOICE, default = 'text')
    option_image      = models.FileField(upload_to = "options", blank = True, null = True)
    option            = models.TextField(blank = True, null = True)
    is_solution       = models.BooleanField(default = False)
#    option_id = models.CharField(max_length = 12, unique = True)


    def __unicode__(self):
        return self.option

