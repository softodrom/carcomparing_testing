# Generated by Django 3.2.9 on 2021-12-03 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('car_brand', models.CharField(max_length=20)),
                ('car_model', models.CharField(max_length=20)),
                ('car_description', models.CharField(max_length=70)),
                ('engine_type', models.CharField(max_length=20)),
                ('power', models.IntegerField()),
                ('tourque', models.IntegerField()),
                ('no_of_cylinder', models.IntegerField()),
                ('valves_per_cylinder', models.IntegerField()),
                ('transmission_type', models.CharField(max_length=20)),
                ('drive_type', models.CharField(max_length=20)),
                ('fuel_type', models.CharField(max_length=20)),
                ('body_type', models.CharField(max_length=20)),
                ('seating_capacity', models.IntegerField()),
                ('wheel_size', models.IntegerField()),
                ('top_speed', models.IntegerField()),
                ('acceleration_to_100', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=70)),
                ('car_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car')),
            ],
        ),
    ]
