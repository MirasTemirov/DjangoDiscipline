# Generated by Django 3.2.6 on 2021-08-20 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20210816_1814'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='finish',
            new_name='end',
        ),
    ]