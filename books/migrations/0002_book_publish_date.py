# Generated by Django 2.1.5 on 2019-02-02 16:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publish_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
