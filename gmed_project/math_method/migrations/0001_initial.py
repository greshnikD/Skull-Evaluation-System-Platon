# Generated by Django 4.0.4 on 2022-05-07 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('visor', '0002_remove_parameters_diagnoses_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnoses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnoses_name', models.TextField(blank=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ParametersList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('measure', models.TextField(blank=True, null=True)),
                ('normal_value', models.IntegerField(blank=True, null=True)),
                ('delta', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parameters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(blank=True, null=True)),
                ('diagnoses_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='math_method.diagnoses')),
                ('parameter_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='math_method.parameterslist')),
                ('research_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='visor.research')),
            ],
        ),
    ]