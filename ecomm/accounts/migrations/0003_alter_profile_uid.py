# Generated by Django 4.2.4 on 2024-01-05 14:16

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('1bba9293-014a-4995-9c5b-f0b78d2aafd4'), editable=False, primary_key=True, serialize=False),
        ),
    ]
