from django.shortcuts import render, redirect
from .forms import Student_admission_form

def index(request):
    return render(request, 'index.html')

def student_admission(request):
    form = Student_admission_form(request.POST, request.FILES)
    
    if request.method == "POST" and form.is_valid():
        form = form.save(commit=False)
        form.save()
        return redirect('main')

    context = {
            'form' : form,
    }

    return render(request, 'student_admission_form.html', context)

