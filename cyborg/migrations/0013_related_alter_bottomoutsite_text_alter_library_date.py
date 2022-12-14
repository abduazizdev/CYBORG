# Generated by Django 4.1.2 on 2022-11-04 10:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cyborg', '0012_bottomoutsite_alter_library_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Related',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('game', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('pubg', 'pubg'), ('sandbox', 'sandbox')], max_length=8)),
            ],
        ),
        migrations.AlterField(
            model_name='bottomoutsite',
            name='text',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='library',
            name='date',
            field=models.TimeField(default=datetime.datetime(2022, 11, 4, 10, 9, 57, 433662, tzinfo=datetime.timezone.utc)),
        ),
    ]
