# Generated by Django 2.0 on 2020-02-15 22:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dispositivo', '0009_auto_20200215_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabelaend',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TabelaEnd', to=settings.AUTH_USER_MODEL),
        ),
    ]
