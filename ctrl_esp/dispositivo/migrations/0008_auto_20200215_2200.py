# Generated by Django 2.0 on 2020-02-15 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispositivo', '0007_auto_20200215_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tabelaend',
            name='ario',
            field=models.ManyToManyField(related_name='_tabelaend_ario_+', to='dispositivo.TabelaEnd'),
        ),
    ]
