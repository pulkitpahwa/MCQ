from django.db import models
from autoslug import AutoSlugField


class Contest(models.Model):
    contest_name = models.CharField(max_length = 40)
    slug = AutoSlugField(populate_from = 'contest_name', unique = True, blank = True, null = True)


    def __unicode__(self) :
        return self.contest_name
