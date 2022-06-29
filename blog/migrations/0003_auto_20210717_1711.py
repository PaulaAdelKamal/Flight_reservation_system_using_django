# Generated by Django 3.2.5 on 2021-07-17 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_flight_add_flight'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('price', models.DecimalField(decimal_places=2, default='100$', max_digits=4)),
            ],
        ),
        migrations.RemoveField(
            model_name='add_flight',
            name='class_available',
        ),
    ]
