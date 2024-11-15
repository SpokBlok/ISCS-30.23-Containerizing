# Generated by Django 4.1.7 on 2024-03-04 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('game', models.CharField(max_length=100)),
                ('tier', models.CharField(choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=1)),
                ('location', models.CharField(max_length=100)),
                ('format', models.CharField(choices=[('single_elimination', 'Single Elimination'), ('double_elimination', 'Double Elimination')], max_length=100)),
                ('application_link', models.URLField()),
                ('schedule', models.TextField()),
                ('prize_pool', models.TextField()),
                ('more_details', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='tournament_images')),
            ],
        ),
    ]
