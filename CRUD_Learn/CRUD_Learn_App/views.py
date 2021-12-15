from django.shortcuts import render, redirect
from .forms import Student_admission_form
from .models import Student_Admission

def student_admission(request):
    form = Student_admission_form(request.POST, request.FILES)
    
    if request.method == "POST" and form.is_valid():
        form = form.save(commit=False)
        form.save()
        return redirect('student_list')

    context = {
            'form' : form,
    }

    return render(request, 'student_admission_form.html', context)

def student_list(request):
    data = Student_Admission.objects.all()
    context = {
            'data' : data,
    }
    return render(request, 'student_list.html', context)

def student_detail(request, id):
    data = Student_Admission.objects.get(id=id)
    context = {
        'data':data,
    }
    return render(request, 'student_detail.html', context)

def student_update(request, id):
    data = Student_Admission.objects.get(id=id)
    form = Student_admission_form(request.POST or None, instance=data)

    if request.method == "POST" and form.is_valid():
        form = form.save(commit=False)
        form.save()

        return redirect('student_list')

    context = {
            'form' : form,
    }

    return render(request, 'student_admission_form.html', context)

def student_delete(request, id):
    data = Student_Admission.objects.get(id=id)
    data.delete()
    return redirect('student_list')

