from django.urls import path
from .views import student_admission, index

urlpatterns = [
    path('', index, name='main'),
    path('admission_form/', student_admission, name='student_admission'),
]

