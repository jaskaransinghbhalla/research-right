# Generated by Django 4.1.3 on 2022-12-28 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('internships', '0007_remove_internship_end_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='internship',
            name='selected_students',
        ),
    ]
