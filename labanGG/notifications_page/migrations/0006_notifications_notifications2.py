# Generated by Django 4.1.7 on 2024-04-22 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications_page', '0005_remove_notifications_notifications2'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='notifications2',
            field=models.BooleanField(default=False),
        ),
    ]
