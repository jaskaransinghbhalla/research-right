# Generated by Django 4.1.3 on 2023-01-31 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internships', '0027_alter_notification_recipient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internship',
            name='min_cgpa',
            field=models.DecimalField(decimal_places=3, default=7.0, max_digits=5),
        ),
    ]
