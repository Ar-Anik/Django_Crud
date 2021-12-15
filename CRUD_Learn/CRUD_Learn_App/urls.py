from django.urls import path
from .views import student_admission, student_list, student_detail, student_update, student_delete

urlpatterns = [
    path('admission_form/', student_admission, name='admission_form'),

    path('', student_list, name='student_list'),

    path('student_detail/<int:id>/', student_detail, name='student_detail'),

    path('student_update/<int:id>/', student_update, name='student_update'),

    path('student_delete/<int:id>/', student_delete, name='student_delete'),
]

