# Generated by Django 2.0rc1 on 2017-11-25 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='lang',
            field=models.CharField(choices=[('de', 'de_DE'), ('en', 'en_GB')], max_length=5),
        ),
    ]
