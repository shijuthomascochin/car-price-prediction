# Generated by Django 4.2.1 on 2023-06-06 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminuname', models.CharField(max_length=50)),
                ('adminpwd', models.CharField(max_length=50)),
            ],
        ),
    ]
