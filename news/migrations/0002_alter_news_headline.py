# Generated by Django 4.2.4 on 2023-09-05 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='headline',
            field=models.CharField(max_length=200),
        ),
    ]
