# Generated by Django 4.1 on 2022-08-27 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('start_address', models.CharField(max_length=256)),
                ('end_address', models.CharField(max_length=256)),
            ],
        ),
    ]
