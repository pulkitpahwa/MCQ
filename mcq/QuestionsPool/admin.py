from django.contrib import admin
from QuestionsPool.models import Pool, Question_pool, Candidate_Question_pool

admin.site.register(Pool)
admin.site.register(Question_pool)
admin.site.register(Candidate_Question_pool)

# Register your models here.
