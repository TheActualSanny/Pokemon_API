# Generated by Django 5.2 on 2025-04-28 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_additionalinformation_capture_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='additionalinformation',
            name='name',
            field=models.CharField(max_length=90, null=True),
        ),
    ]
