# Generated by Django 4.1 on 2022-09-12 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_remove_course_course_introvideo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='videos_hours',
            field=models.IntegerField(),
        ),
    ]
