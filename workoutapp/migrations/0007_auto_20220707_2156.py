# Generated by Django 3.2.14 on 2022-07-07 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workoutapp', '0006_auto_20220707_2144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plantable',
            name='exercise_item1',
        ),
        migrations.RemoveField(
            model_name='plantable',
            name='exercise_item2',
        ),
        migrations.AddField(
            model_name='plantable',
            name='exercise',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='workoutapp.itemtable'),
        ),
    ]
