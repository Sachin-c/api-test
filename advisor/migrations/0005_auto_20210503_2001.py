# Generated by Django 2.1.3 on 2021-05-03 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advisor', '0004_booking_advisor_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='book_time',
            field=models.DateTimeField(max_length=420),
        ),
    ]
