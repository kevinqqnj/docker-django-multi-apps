# Generated by Django 2.0.3 on 2018-03-28 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmct', '0002_auto_20180328_0318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accept',
            old_name='securers',
            new_name='users',
        ),
        migrations.RenameField(
            model_name='assign',
            old_name='securers',
            new_name='users',
        ),
        migrations.RenameField(
            model_name='secure',
            old_name='securers',
            new_name='users',
        ),
    ]
