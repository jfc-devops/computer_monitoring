# Generated by Django 2.0 on 2020-02-20 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispositivo', '0011_tabelaend_modelo'),
    ]

    operations = [
        migrations.CreateModel(
            name='AudioVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio', models.FileField(blank=True, null=True, upload_to='', verbose_name='Makaleye Fotoğraf Ekleyin')),
                ('imagem', models.FileField(blank=True, null=True, upload_to='', verbose_name='Makaleye Fotoğraf Ekleyin')),
            ],
        ),
    ]