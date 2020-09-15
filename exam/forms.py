from django.forms import forms, ModelForm
from .models import QuestionBank

class AddQuestionForm(ModelForm):
    class Meta:
        model = QuestionBank
        fields = [
            'year',
            'subject',
            'unit',
            'question',
        ]