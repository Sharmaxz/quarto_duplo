# Generated by Django 2.0.13 on 2019-03-19 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('adress', models.CharField(max_length=250)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('site', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('adress', models.CharField(max_length=250)),
                ('daily_min', models.DecimalField(decimal_places=2, max_digits=10)),
                ('daily_max', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin', models.DateField(blank=True, null=True)),
                ('checkout', models.DateField(blank=True, null=True)),
                ('gender_pref', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.DateField(blank=True)),
                ('cpf', models.CharField(max_length=14)),
                ('email', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='request',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='hotelshare.User'),
        ),
        migrations.AddField(
            model_name='match',
            name='request1',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='request', to='hotelshare.Request'),
        ),
        migrations.AddField(
            model_name='match',
            name='request2',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='request1', to='hotelshare.Request'),
        ),
        migrations.AddField(
            model_name='event',
            name='request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotelshare.Request'),
        ),
    ]
