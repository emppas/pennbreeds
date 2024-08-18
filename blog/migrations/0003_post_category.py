# Generated by Django 5.0.7 on 2024-08-18 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Tech', 'Tech'), ('Politics', 'Politics'), ('Education', 'Education'), ('Health', 'Health'), ('History', 'History'), ('Entertainment', 'Entertainment'), ('Style', 'Style')], default='Politics', max_length=50),
        ),
    ]
