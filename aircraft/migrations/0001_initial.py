# Generated by Django 3.2.3 on 2021-07-17 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddAirCraft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Enter the name', max_length=100)),
                ('type', models.CharField(choices=[('Boeing', 'Boeing'), ('Airbus', 'Airbus'), ('Bombardier', 'Bombardier'), ('Embraer', 'Embraer'), ('ATR', 'ATR')], max_length=10)),
                ('number_of_sets', models.DecimalField(decimal_places=0, default=100, max_digits=3)),
            ],
        ),
    ]
