# Generated by Django 2.0.2 on 2018-03-26 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(help_text='Enter Your User Name Here', max_length=150)),
                ('password', models.CharField(help_text='Enter Your Password Here', max_length=400)),
            ],
        ),
    ]
