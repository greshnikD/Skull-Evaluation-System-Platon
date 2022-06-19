# Generated by Django 4.0.4 on 2022-05-09 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0003_dotpairs_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dotpairs',
            name='dot_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='DotPairs_dot_1', to='predict.dotlist'),
        ),
        migrations.AlterField(
            model_name='dotpairs',
            name='dot_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='DotPairs_dot_2', to='predict.dotlist'),
        ),
    ]
