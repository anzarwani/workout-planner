# Generated by Django 3.2.14 on 2022-07-07 06:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workoutapp', '0004_remove_plantable_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='plantable',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
