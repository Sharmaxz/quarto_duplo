# Generated by Django 2.0.13 on 2019-03-21 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotelshare', '0011_local_adress'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='adress',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='hotelshare.Local'),
        ),
    ]