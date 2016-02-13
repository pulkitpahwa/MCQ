from django.db import models
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase
from contest.models import Contest 

class ToolTags(TaggedItemBase) :
    content_object = models.ForeignKey('Question')

class TechniqueTags(TaggedItemBase) :
    content_object = models.ForeignKey('Question')

class DomainTags(TaggedItemBase) :
    content_object = models.ForeignKey('Question')

class DifficultyTags(TaggedItemBase) :
    content_object = models.ForeignKey('Question')

class Question(models.Model) : 
    question       = models.TextField()
    description    = models.TextField(blank = True, null = True)
    multiple_true  = models.BooleanField(default = False)
    tools          = TaggableManager(through = ToolTags, related_name = "tools",verbose_name = "tools")
    techniques     = TaggableManager(through = TechniqueTags, related_name = "techniques", verbose_name = "techniques")
    domains        = TaggableManager(through = DomainTags, related_name = "domains", verbose_name = "domains")
    difficulty     = TaggableManager(through = DifficultyTags, related_name = "difficulty", verbose_name = "difficulty")
    author         = models.ForeignKey(UserProfile, blank = True, null = True)
    mcq_unique_id  = models.CharField(max_length = 12, unique = True)
    approved       = models.BooleanField(default = False) #the question has to be approved to be available for shortlisting

    def __unicode__(self):
        return self.question[:20]

class Options(models.Model) : 
    OPTION_CHOICE = (
            ('text', 'Text'),
            ('image', 'Image'),
            )
    question = models.ForeignKey(Question)
    option_type = models.CharField(max_length = 5, choices = OPTION_CHOICE, default = 'text')
    option_image = models.FileField(upload_to = "options", blank = True, null = True)
    option = models.TextField(blank = True, null = True)
    is_solution = models.BooleanField(default = False)
    option_id = models.CharField(max_length = 12, unique = True)


    def __unicode__(self):
        return self.option

class QuestionPool(models.Model) :



class Particpations(models.Model) : 
    user = models.ForeignKey(UserProfile)
    mcq  = models.ForeignKey(MCQ)
    contest = models.ForeignKey(Contest)
    start_time = models.DateTimeField(blank = True, null = True)
    end_time = models.DateTimeField(blank = True, null = True)
    time_taken = models.IntegerField(default = 0) #this time is in seconds
    option1 = models.CharField(max_length = 12, blank = True, null = True)
    option2 = models.CharField(max_length = 12, blank = True, null = True)
    option3 = models.CharField(max_length = 12, blank = True, null = True)
    option4 = models.CharField(max_length = 12, blank = True, null = True)
    option5 = models.CharField(max_length = 12, blank = True, null = True)
    is_correct = models.BooleanField(default = False)
    score      = models.FloatField(defualt = 0)
    
    def __unicode__(self):
        return self.user, self.mcq, self.contest
