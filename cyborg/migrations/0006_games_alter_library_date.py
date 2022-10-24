# Generated by Django 4.1.2 on 2022-10-24 09:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cyborg', '0005_library'),
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('name', models.CharField(default='game name', max_length=40)),
            ],
        ),
        migrations.AlterField(
            model_name='library',
            name='date',
            field=models.TimeField(default=datetime.datetime(2022, 10, 24, 9, 24, 44, 474441, tzinfo=datetime.timezone.utc)),
        ),
    ]
