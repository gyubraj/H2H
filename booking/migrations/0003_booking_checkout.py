# Generated by Django 4.0.2 on 2022-03-19 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_alter_booking_property'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='checkout',
            field=models.BooleanField(default=False),
        ),
    ]
