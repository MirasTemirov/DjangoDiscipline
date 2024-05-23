# Generated by Django 3.2.6 on 2021-08-21 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0003_alter_log_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='data',
            field=models.CharField(choices=[('account', 'account'), ('booking', 'booking'), ('handbook_group', 'handbook_group'), ('handbook_object', 'handbook_object'), ('log', 'log'), ('booking_business_hour', 'booking_business_hour')], max_length=30),
        ),
    ]