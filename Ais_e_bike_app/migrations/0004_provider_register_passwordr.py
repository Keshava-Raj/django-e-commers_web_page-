# Generated by Django 5.0.4 on 2024-05-04 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ais_e_bike_app', '0003_cntact_us_provider_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider_register',
            name='passwordR',
            field=models.CharField(default=2, max_length=18),
            preserve_default=False,
        ),
    ]
