# Generated by Django 4.1.3 on 2022-12-13 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internships', '0004_remove_internship_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='internship',
            name='is_accepting',
            field=models.BooleanField(default=True),
        ),
    ]