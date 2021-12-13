from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Student_Admission(models.Model):
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    number = PhoneNumberField(null=False, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    student_image = models.ImageField(upload_to="student_admission", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

