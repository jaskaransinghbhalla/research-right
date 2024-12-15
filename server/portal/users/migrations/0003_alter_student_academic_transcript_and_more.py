# Generated by Django 4.1.3 on 2023-01-04 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_professor_website_alter_student_academic_transcript_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='academic_transcript',
            field=models.FileField(upload_to='acad_transcripts/'),
        ),
        migrations.AlterField(
            model_name='student',
            name='resume',
            field=models.FileField(upload_to='resumes/'),
        ),
        migrations.AlterField(
            model_name='student',
            name='sop',
            field=models.FileField(upload_to='sops/'),
        ),
    ]