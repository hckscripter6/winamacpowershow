# Generated by Django 3.0.5 on 2020-06-12 22:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='update',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
