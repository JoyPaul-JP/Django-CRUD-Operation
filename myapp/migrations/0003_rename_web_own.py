# Generated by Django 4.1.2 on 2022-10-12 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_myapp_web'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='web',
            new_name='own',
        ),
    ]
