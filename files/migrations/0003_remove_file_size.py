# Generated by Django 3.2.9 on 2021-12-21 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0002_auto_20211221_1839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='size',
        ),
    ]
