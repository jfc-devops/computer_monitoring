# Generated by Django 2.0 on 2020-02-15 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dispositivo', '0003_tabelaend_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tabelaend',
            name='usuario',
        ),
    ]
