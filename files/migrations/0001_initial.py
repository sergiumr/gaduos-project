# Generated by Django 3.2.9 on 2021-12-29 15:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=128)),
                ('filecontent', models.FileField(upload_to='files/%Y/')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='courses.course')),
            ],
        ),
    ]