# Generated by Django 4.0.3 on 2022-05-24 17:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0018_alter_profile_last_sent_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='last_sent_email',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 24, 19, 59, 49, 78027)),
        ),
    ]
