# Generated by Django 2.1.5 on 2020-03-17 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0021_auto_20200317_0300'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='documentgoldannotation',
            unique_together={('document', 'label', 'additional_data')},
        ),
        migrations.AlterUniqueTogether(
            name='documentmlmannotation',
            unique_together={('document', 'label', 'additional_data')},
        ),
    ]
