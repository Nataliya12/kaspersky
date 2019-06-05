from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(ModelTestirovanie)
admin.site.register(ModelTestQuestions)
admin.site.register(ModelTestAnswer)
admin.site.register(ModelTestirovanieUser)
admin.site.register(ModelTestAnswerUser)
admin.site.register(Text)