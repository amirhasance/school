# Generated by Django 3.0.8 on 2020-07-13 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0008_auto_20200712_1850'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date_time', models.DateTimeField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='JD',
        ),
    ]
