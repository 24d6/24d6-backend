# Generated by Django 2.0rc1 on 2017-11-25 21:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20171125_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='run',
            name='gamemaster',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]