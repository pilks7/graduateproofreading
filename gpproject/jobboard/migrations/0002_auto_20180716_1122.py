# Generated by Django 2.0.2 on 2018-07-16 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobpost',
            options={'ordering': ['-created_at']},
        ),
    ]
