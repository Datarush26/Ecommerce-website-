# Generated by Django 4.2.4 on 2024-01-05 14:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_profile_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('11f05ef5-72d1-4660-ae37-fdd1e1e5b98a'), editable=False, primary_key=True, serialize=False),
        ),
    ]
