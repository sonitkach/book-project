# Generated by Django 3.1 on 2020-09-29 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('title', models.CharField(max_length=100)),
                ('author_name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
