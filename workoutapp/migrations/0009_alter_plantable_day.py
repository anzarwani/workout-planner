# Generated by Django 3.2.14 on 2022-07-08 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workoutapp', '0008_alter_plantable_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantable',
            name='day',
            field=models.CharField(choices=[('sunday', 'sunday'), ('monday', 'monday'), ('tuesday', 'tuesday'), ('wednesday', 'wednesday'), ('thursday', 'thursday'), ('friday', 'friday')], max_length=10, null=True),
        ),
    ]