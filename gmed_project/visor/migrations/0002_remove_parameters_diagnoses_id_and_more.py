# Generated by Django 4.0.4 on 2022-05-07 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parameters',
            name='diagnoses_id',
        ),
        migrations.RemoveField(
            model_name='parameters',
            name='parameter_id',
        ),
        migrations.RemoveField(
            model_name='parameters',
            name='research_id',
        ),
        migrations.DeleteModel(
            name='Diagnoses',
        ),
        migrations.DeleteModel(
            name='Parameters',
        ),
        migrations.DeleteModel(
            name='ParametersList',
        ),
    ]
