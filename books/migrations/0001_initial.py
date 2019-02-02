# Generated by Django 2.1.5 on 2019-02-02 16:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('changed', models.DateTimeField(auto_now=True, null=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('changed', models.DateTimeField(auto_now=True, null=True)),
                ('title', models.CharField(max_length=250)),
                ('price', models.FloatField()),
                ('ISBN', models.CharField(max_length=150, unique=True)),
                ('authors', models.ManyToManyField(to='books.Author')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('changed', models.DateTimeField(auto_now=True, null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('host', models.CharField(max_length=1000)),
                ('path', models.CharField(max_length=1000)),
                ('method', models.CharField(max_length=50)),
                ('content_type', models.CharField(max_length=1000)),
                ('user_agent', models.CharField(max_length=2500)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]