# Generated by Django 4.2.5 on 2023-09-25 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('song_api', '0002_student'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
    ]