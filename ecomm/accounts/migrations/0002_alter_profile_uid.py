# Generated by Django 4.2.4 on 2023-09-06 16:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('58f2f51a-289b-4019-9fdb-4afc59f76126'), editable=False, primary_key=True, serialize=False),
        ),
    ]
