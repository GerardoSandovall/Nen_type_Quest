# Generated by Django 5.1.2 on 2024-11-03 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nen_type', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nenpoints',
            name='answered_fiel',
            field=models.BooleanField(default=False),
        ),
    ]