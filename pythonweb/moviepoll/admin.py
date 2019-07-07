from django.contrib import admin
from .models import Question, Choice

# Register your models here.
class ChoiceInLine(admin.StackedInline):
    model = Choice
    extra = 1
    
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInLine]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)