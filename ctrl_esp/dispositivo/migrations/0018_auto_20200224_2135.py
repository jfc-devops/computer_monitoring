# Generated by Django 2.0 on 2020-02-24 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dispositivo', '0017_tabelaend_dono'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tabelaend',
            old_name='dono',
            new_name='nome',
        ),
    ]