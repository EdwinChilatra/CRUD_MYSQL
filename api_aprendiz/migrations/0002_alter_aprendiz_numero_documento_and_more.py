# Generated by Django 4.2.4 on 2023-09-01 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_aprendiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aprendiz',
            name='numero_documento',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='aprendiz',
            name='numero_ficha',
            field=models.IntegerField(max_length=10),
        ),
    ]
