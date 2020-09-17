from django.forms import forms, ModelForm
from .models import QuestionBank, Test
from django.forms.widgets import DateTimeInput

class AddQuestionForm(ModelForm):
    class Meta:
        model = QuestionBank
        fields = [
            'year',
            'subject',
            'unit',
            'question',
        ]



class AddTestForm(ModelForm):

    class Meta:
        model = Test
        fields = [
            'test_name',
            'test_date',
            'test_duration',
            'test_marks',
            'test_question',
        ]
        widgets = {
            'test_date': DateTimeInput(attrs={'type': 'date'})
        }



    # test_question = forms.

    