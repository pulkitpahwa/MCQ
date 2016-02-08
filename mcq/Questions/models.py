from django.db import models
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase

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

    def __unicode__(self):
        return self.option



# Create your models here.
