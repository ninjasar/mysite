# Generated by Django 4.0.6 on 2022-07-22 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_school_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='school',
        ),
        migrations.DeleteModel(
            name='School',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
