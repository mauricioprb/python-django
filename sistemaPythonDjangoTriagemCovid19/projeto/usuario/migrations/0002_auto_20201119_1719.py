# Generated by Django 3.0.4 on 2020-11-19 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='tipo',
            field=models.CharField(choices=[('ADMINISTRADOR', 'Administrador'), ('ENFERMEIRO', 'Enfermeiro'), ('TÉCNICO', 'Técnico')], default='TÉCNICO', help_text='* Campos obrigatórios', max_length=15, verbose_name='Tipo do usuário *'),
        ),
    ]
