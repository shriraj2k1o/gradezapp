from django.shortcuts import render, redirect
from .forms import AddQuestionForm, AddTestForm
from .models import QuestionBank, Test

# Create your views here.
def AddQuestion(request):
    note =''
    p = request.session.get('profession')
    form = AddQuestionForm(request.POST or None)
    if form.is_valid():
        form.save()
        note = "Question Added!"
        # if p == 'P':
        #     return redirect('professor:index')
        # else:
        #     return redirect('siteadmin:index')
    return render(request, 'exam/add-question.html', {'form': form, 'note':note})


def ViewQuestion(request):

    questions = QuestionBank.objects.all()

    return render(request, 'exam/view-qb.html', {'questions': questions})


def AddTest(request):
    form = AddTestForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, 'exam/add-test.html', {'form':form})