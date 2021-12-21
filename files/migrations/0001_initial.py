# Generated by Django 3.2.9 on 2021-12-21 16:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=128)),
                ('filecontent', models.FileField(upload_to='files/%Y/')),
                ('size', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
