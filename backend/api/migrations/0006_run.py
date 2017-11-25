# Generated by Django 2.0rc1 on 2017-11-25 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20171125_1958'),
    ]

    operations = [
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Group')),
            ],
        ),
    ]
