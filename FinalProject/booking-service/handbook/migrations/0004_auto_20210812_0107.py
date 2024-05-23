# Generated by Django 3.2.6 on 2021-08-12 01:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('handbook', '0003_object'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='mentor_for_boys',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='abi_groups', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='group',
            name='mentor_for_girls',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='abla_groups', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='group',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_groups', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='group',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='object',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]