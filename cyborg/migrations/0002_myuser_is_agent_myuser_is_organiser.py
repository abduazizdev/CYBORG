# Generated by Django 4.1.2 on 2022-10-15 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cyborg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_agent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='myuser',
            name='is_organiser',
            field=models.BooleanField(default=False),
        ),
    ]
