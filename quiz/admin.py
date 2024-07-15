from django.contrib import admin

# Register your models here.
from .models import code_exam,code_question

admin.site.register(code_exam)
admin.site.register(code_question)