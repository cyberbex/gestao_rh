# Generated by Django 2.1.5 on 2024-01-20 22:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0002_auto_20240120_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
