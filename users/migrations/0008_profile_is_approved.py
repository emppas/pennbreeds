# Generated by Django 5.0.7 on 2024-08-20 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_profile_is_approved_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
