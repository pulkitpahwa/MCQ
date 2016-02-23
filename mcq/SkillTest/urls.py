from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'SkillTest.views.create_skill_test',name = 'create-skill-test'),
    url(r'^(?P<skill_test>[-\w]+)/create-pool$', 'SkillTest.views.count_questions_with_given_tags', name='questions-home'),
    url(r'^(?P<skill_test>[-\w]+)/save-pool$', 'SkillTest.views.save_questions_with_given_tags', name='questions-home'),
    url(r'^(?P<skill_test>[-\w]+)/$', 'SkillTest.views.particular_skill_test', name='particular_skill_test'),
    url(r'^(?P<skill_test>[-\w]+)/join$', 'SkillTest.views.join_skill_test', name='join_skill_test'),
    url(r'^(?P<skill_test>[-\w]+)/playground$', 'SkillTest.views.playground', name='questions-playground'),
    url(r'^add_multiple$', 'Questions.views.add_questions_from_csv', name='csv-upload'),
]
