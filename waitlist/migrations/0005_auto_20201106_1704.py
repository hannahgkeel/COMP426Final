# Generated by Django 3.1.1 on 2020-11-06 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waitlist', '0004_auto_20201106_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waitlistticket',
            name='location',
            field=models.CharField(choices=[('Carrboro', 'Carrboro'), ('Chapel Hill', 'Chapel Hill')], max_length=50),
        ),
    ]
