# Generated by Django 3.1.2 on 2020-11-11 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gold_app', '0007_auto_20201110_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='gold_lot',
            name='jewller_last_interest_paid_when',
            field=models.DateField(default=''),
        ),
    ]
