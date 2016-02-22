from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
#from contest.models import Contest_participants

class Skill_test(models.Model) :
    name = models.CharField(max_length = 30)
    slug = AutoSlugField(populate_from = 'name', unique = True, blank = True, null = True)


class Test_participant(models.Model) : 
    skill_test = models.ForeignKey(Skill_test)
    participant = models.ForeignKey(User)
#   contest_participant = models.ForeignKey(Contest_participants)
    start_time = models.DateTimeField(blank = True, null = True)
    end_time = models.DateTimeField(blank =True, null = True)
    score = models.FloatField(default = 0)
