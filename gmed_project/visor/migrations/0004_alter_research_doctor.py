# Generated by Django 4.0.4 on 2022-05-23 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('visor', '0003_alter_doctor_change_date_alter_doctor_create_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='research',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
