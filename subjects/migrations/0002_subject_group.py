# Generated by Django 3.0.6 on 2020-05-08 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='group',
            field=models.ManyToManyField(to='groups.Group'),
        ),
    ]
