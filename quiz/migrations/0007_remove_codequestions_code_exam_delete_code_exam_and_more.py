# Generated by Django 4.1.7 on 2023-07-07 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_code_exam_codequestions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='codequestions',
            name='code_exam',
        ),
        migrations.DeleteModel(
            name='code_exam',
        ),
        migrations.DeleteModel(
            name='CodeQuestions',
        ),
    ]
