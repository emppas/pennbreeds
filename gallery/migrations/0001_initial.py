# Generated by Django 5.0.7 on 2024-09-05 14:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Sports & Recreation', 'Sports & Recreation'), ('Inductions', 'Inductions'), ('Award Nites', 'Award Nites'), ('Courtesy Visits', 'Courtesy Visits'), ('Club Retreats', 'Club Retreats'), ('Burials', 'Burials'), ('Monthly Meetings', 'Monthly Meetings')], max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('date', models.CharField(blank=True, max_length=50, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='event_images/')),
                ('caption', models.CharField(blank=True, max_length=200, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='gallery.event')),
            ],
        ),
    ]
