# Generated by Django 4.2.4 on 2024-01-05 14:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_profile_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('e86be0e8-2e1e-443f-a527-153820ce4e5f'), editable=False, primary_key=True, serialize=False),
        ),
    ]
