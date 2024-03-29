# Generated by Django 3.2.14 on 2022-07-06 16:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workoutapp', '0002_itemtable_day'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemtable',
            name='day',
        ),
        migrations.RemoveField(
            model_name='itemtable',
            name='user',
        ),
        migrations.CreateModel(
            name='planTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('sunday', 'sunday'), ('monday', 'monday'), ('tuesday', 'tuesday')], max_length=10, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='workoutapp.workouttable')),
                ('exercise', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='workoutapp.itemtable')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
