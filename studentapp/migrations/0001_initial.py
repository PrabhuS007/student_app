# Generated by Django 4.1.7 on 2023-03-26 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=20)),
                ('semail', models.EmailField(max_length=254)),
                ('sage', models.IntegerField()),
                ('sgender', models.CharField(max_length=20)),
            ],
        ),
    ]
