# Generated by Django 4.2.5 on 2023-09-25 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=100)),
            ],
        ),
    ]