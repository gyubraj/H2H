# Generated by Django 4.0.2 on 2022-03-19 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_propertyreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertyreview',
            name='update_date',
            field=models.DateField(auto_now=True),
        ),
    ]