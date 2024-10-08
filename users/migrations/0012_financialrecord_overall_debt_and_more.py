# Generated by Django 5.0.7 on 2024-09-08 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_financialrecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='financialrecord',
            name='overall_debt',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='financialrecord',
            name='total_amount_due',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='financialrecord',
            name='total_amount_owed',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
