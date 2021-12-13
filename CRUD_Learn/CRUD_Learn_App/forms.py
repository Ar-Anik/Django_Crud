from django import forms
from .models import Student_Admission

class Student_admission_form(forms.ModelForm):
    class Meta:
        model = Student_Admission
        fields = ['name', 'father_name', 'mother_name', 'email', 'number', 'student_image']
