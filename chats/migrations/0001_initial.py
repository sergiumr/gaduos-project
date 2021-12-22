# Generated by Django 3.2.9 on 2021-12-22 12:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=512)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='chat_user1', to='users.person')),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='chat_user2', to='users.person')),
            ],
        ),
    ]
