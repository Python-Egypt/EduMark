# Generated by Django 4.1 on 2022-09-12 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='discount',
            new_name='newprice',
        ),
    ]