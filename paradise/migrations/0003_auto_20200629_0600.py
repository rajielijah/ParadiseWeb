# Generated by Django 3.0.7 on 2020-06-29 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paradise', '0002_competition_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='expiration_date',
            field=models.DateTimeField(),
        ),
    ]