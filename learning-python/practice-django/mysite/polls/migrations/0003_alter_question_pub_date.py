# Generated by Django 4.0.1 on 2022-01-15 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_rename_question_question_question_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date publisheru'),
        ),
    ]
