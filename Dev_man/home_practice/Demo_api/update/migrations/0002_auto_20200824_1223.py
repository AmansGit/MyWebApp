# Generated by Django 2.2 on 2020-08-24 12:23

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('update', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='update',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
