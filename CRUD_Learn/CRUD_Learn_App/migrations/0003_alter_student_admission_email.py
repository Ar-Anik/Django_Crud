# Generated by Django 4.0 on 2021-12-12 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD_Learn_App', '0002_alter_student_admission_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_admission',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
    ]
