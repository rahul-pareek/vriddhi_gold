# Generated by Django 3.1.2 on 2020-10-31 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gold_app', '0019_auto_20201031_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gl_lead',
            name='lead_branch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gold_app.branch', to_field='branch_name'),
        ),
        migrations.AlterField(
            model_name='gl_lead',
            name='member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gold_app.user'),
        ),
    ]