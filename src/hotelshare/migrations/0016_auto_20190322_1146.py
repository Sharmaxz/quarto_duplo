# Generated by Django 2.0.13 on 2019-03-22 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotelshare', '0015_request_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='event',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='hotelshare.Event'),
        ),
    ]
