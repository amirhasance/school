# Generated by Django 3.0.8 on 2020-07-13 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0009_auto_20200713_0915'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exam',
            old_name='Time_expires',
            new_name='time_ends',
        ),
        migrations.RenameField(
            model_name='exam',
            old_name='Time_starts',
            new_name='time_starts',
        ),
    ]
