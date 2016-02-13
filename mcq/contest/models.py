from django.db import models

class Contest(models.Model):
    contest_name = models.CharField(max_length = 40)

    def __unicode__(self) :
        return self.contest_name
