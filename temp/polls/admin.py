from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class ChoiceInlinne(admin.TabularInline):
    model = Choice
    extra = 4


class QuetionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    list_display = ['question_text', 'pub_date', 'was_published_recently']
    fieldsets = [
        (None, {'fields' : ['question_text']}),
        ('Published Date', {'fields' : ['pub_date']})
    ]
    inlines = [ChoiceInlinne]

admin.site.register(Question, QuetionAdmin)
admin.site.register(Choice)