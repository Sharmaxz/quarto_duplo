# Generated by Django 2.0.13 on 2019-03-21 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotelshare', '0007_auto_20190321_1231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='local',
            name='request',
        ),
        migrations.AddField(
            model_name='request',
            name='local',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hotelshare.Local'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='adress',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hotelshare.Local'),
        ),
    ]
