# Generated by Django 4.2.6 on 2025-04-10 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Books_app', '0006_alter_reading_list_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reading_list',
            options={'ordering': ['position']},
        ),
    ]
