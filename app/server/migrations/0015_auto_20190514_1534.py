# Generated by Django 2.1.5 on 2019-05-14 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0014_auto_20190502_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='enable_metadata_search',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='show_predicted',
            field=models.BooleanField(default=False),
        ),
    ]
