# Generated by Django 4.1.1 on 2022-11-08 12:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Airplane',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'airplane',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('country', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'city',
            },
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('airplane', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customer.airplane')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customer.city')),
            ],
            options={
                'verbose_name': 'flight',
            },
        ),
        migrations.CreateModel(
            name='Gate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'gate',
            },
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('price', models.FloatField(default=0.0)),
            ],
            options={
                'verbose_name': 'option',
            },
        ),
        migrations.CreateModel(
            name='SeatClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('price', models.FloatField(default=0.0)),
            ],
            options={
                'verbose_name': 'seat_class',
            },
        ),
        migrations.CreateModel(
            name='SeatNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=3)),
                ('airplane', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customer.airplane')),
                ('seat_class', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customer.seatclass')),
            ],
            options={
                'verbose_name': 'seat_number',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('datetime', models.DateTimeField()),
                ('total_price', models.FloatField(default=0.0)),
                ('lunch', models.BooleanField(default=False)),
                ('luggage', models.BooleanField(default=False)),
                ('gateway_passed', models.BooleanField(default=False)),
                ('ticket_code', models.CharField(max_length=256)),
                ('create_datetime', models.DateTimeField(auto_now_add=True)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customer.flight')),
                ('gate', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customer.gate')),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customer.seatnumber')),
                ('seat_class', models.ForeignKey(db_column='seat_class', on_delete=django.db.models.deletion.PROTECT, to='customer.seatclass')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ticket',
            },
        ),
        migrations.AddField(
            model_name='flight',
            name='gate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customer.gate'),
        ),
        migrations.AddIndex(
            model_name='city',
            index=models.Index(fields=['name'], name='customer_ci_name_1900b1_idx'),
        ),
        migrations.AddIndex(
            model_name='ticket',
            index=models.Index(fields=['ticket_code'], name='customer_ti_ticket__6572c1_idx'),
        ),
    ]
