# Generated by Django 3.0.6 on 2020-05-08 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0002_subject_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='group',
        ),
    ]
