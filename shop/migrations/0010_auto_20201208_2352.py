# Generated by Django 3.0 on 2020-12-08 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_id',
            field=models.EmailField(max_length=200, null=True),
        ),
    ]