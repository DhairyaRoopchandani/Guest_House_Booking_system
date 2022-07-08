# Generated by Django 3.2.5 on 2021-11-03 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GuestDetails',
            fields=[
                ('user_name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=400)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('adhaar_no', models.CharField(max_length=20)),
            ],
        ),
    ]
