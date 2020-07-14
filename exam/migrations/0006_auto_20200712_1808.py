# Generated by Django 3.0.8 on 2020-07-12 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0005_answer_exam_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='Time_considered_to_solve_in_minute',
            new_name='Time_considered_to_solve_in_seconds',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='Barem',
            new_name='correct_ans',
        ),
        migrations.RemoveField(
            model_name='question',
            name='caution_help',
        ),
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='questions/test'),
        ),
        migrations.CreateModel(
            name='WQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('number', models.IntegerField(default=1)),
                ('question', models.CharField(max_length=500)),
                ('image', models.ImageField(blank=True, null=True, upload_to='questions/tashrihi')),
                ('Time_considered_to_solve_in_seconds', models.IntegerField(default=1)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.Exam')),
            ],
            options={
                'ordering': ('number',),
            },
        ),
    ]