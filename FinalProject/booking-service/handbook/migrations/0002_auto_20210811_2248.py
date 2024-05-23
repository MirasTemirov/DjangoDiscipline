# Generated by Django 3.2.6 on 2021-08-11 22:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('handbook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='group',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='deleted_on',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='edited_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='group',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]