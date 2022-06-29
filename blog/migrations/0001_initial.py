# Generated by Django 3.2.3 on 2021-07-17 00:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aircraft', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=100)),
                ('To', models.CharField(max_length=100)),
                ('check_in_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('check_out_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.CharField(default='Admin', max_length=10)),
                ('class_available', models.DecimalField(decimal_places=0, default=3, max_digits=1)),
                ('plane', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='aircraft.addaircraft')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.flight')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]