# Generated by Django 5.2 on 2025-04-23 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_damageinfo_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='combatstats',
            old_name='special_health',
            new_name='special_attack',
        ),
    ]
