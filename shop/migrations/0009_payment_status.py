# Generated by Django 3.0 on 2020-12-06 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20201206_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='status',
            field=models.CharField(default='Failed', max_length=200),
        ),
    ]
