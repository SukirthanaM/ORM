# Generated by Django 5.1.2 on 2024-10-22 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('uname', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('accountnum', models.IntegerField(primary_key=True, serialize=False)),
                ('loan', models.IntegerField()),
            ],
        ),
    ]
