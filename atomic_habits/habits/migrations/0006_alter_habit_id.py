# Generated by Django 5.1.4 on 2024-12-19 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0005_alter_reward_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
