# Generated by Django 4.0.3 on 2022-03-07 11:45

import booking.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0002_alter_inventory_registration_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('B', 'Booked'), ('O', 'Ongoing'), ('C', 'Cancelled'), ('BC', 'Completed')], default='B', max_length=2)),
                ('booking_id', models.CharField(default=booking.utils.generate_booking_id, max_length=8)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookings', to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookings', to='inventory.inventory')),
            ],
        ),
    ]
