# Generated by Django 3.0.6 on 2020-05-09 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='subject',
            new_name='subjects',
        ),
    ]
