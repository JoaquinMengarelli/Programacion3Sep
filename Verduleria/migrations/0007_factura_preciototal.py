# Generated by Django 3.1.1 on 2020-10-01 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Verduleria', '0006_sumatotal'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='preciototal',
            field=models.CharField(default=0, editable=False, max_length=5000),
        ),
    ]
