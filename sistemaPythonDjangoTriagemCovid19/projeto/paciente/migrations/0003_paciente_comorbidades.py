# Generated by Django 3.0.4 on 2024-04-16 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0002_auto_20230511_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='comorbidades',
            field=models.TextField(blank=True, help_text='Deixe em branco caso não possua', null=True, verbose_name='Comorbidade'),
        ),
    ]
