# Generated by Django 5.1.4 on 2024-12-18 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0004_reward_habit_myreward'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reward',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
