# Generated by Django 3.2.25 on 2025-06-02 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0024_alter_room_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='code',
            field=models.CharField(default='1F168CF5', max_length=8, unique=True),
        ),
    ]
