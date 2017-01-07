# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('kode_booking', models.AutoField(serialize=False, primary_key=True)),
                ('jumlah_penumpang', models.IntegerField()),
                ('waktu_mulai_booking', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 'booking',
            },
        ),
        migrations.CreateModel(
            name='CaraBayar',
            fields=[
                ('id_cara_bayar', models.AutoField(serialize=False, primary_key=True)),
                ('nama_cara_bayar', models.CharField(max_length=40)),
                ('detil_cara_bayar', models.TextField()),
            ],
            options={
                'managed': False,
                'db_table': 'cara_bayar',
            },
        ),
        migrations.CreateModel(
            name='Kereta',
            fields=[
                ('id_kereta', models.AutoField(serialize=False, primary_key=True)),
                ('nama_kereta', models.CharField(max_length=50)),
            ],
            options={
                'managed': False,
                'db_table': 'kereta',
            },
        ),
        migrations.CreateModel(
            name='LayananKereta',
            fields=[
                ('id_layanan_kereta', models.AutoField(serialize=False, primary_key=True)),
                ('kapasitas', models.IntegerField()),
                ('harga_tiket', models.IntegerField()),
            ],
            options={
                'managed': False,
                'db_table': 'layanan_kereta',
            },
        ),
        migrations.CreateModel(
            name='Pembayaran',
            fields=[
                ('kode_pembayaran', models.AutoField(serialize=False, primary_key=True)),
                ('waktu_penagihan', models.DateTimeField()),
                ('waktu_pembayaran', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'pembayaran',
            },
        ),
        migrations.CreateModel(
            name='Penumpang',
            fields=[
                ('id_penumpang', models.AutoField(serialize=False, primary_key=True)),
                ('nomor_identitas', models.CharField(max_length=24)),
                ('nama_penumpang', models.CharField(max_length=64)),
            ],
            options={
                'managed': False,
                'db_table': 'penumpang',
            },
        ),
        migrations.CreateModel(
            name='RangkaianPerjalanan',
            fields=[
                ('id_rangkaian_perjalanan', models.AutoField(serialize=False, primary_key=True)),
                ('jenis_perjalanan', models.CharField(max_length=1)),
                ('waktu', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 'rangkaian_perjalanan',
            },
        ),
        migrations.CreateModel(
            name='Stasiun',
            fields=[
                ('id_stasiun', models.CharField(max_length=3, serialize=False, primary_key=True)),
                ('nama_stasiun', models.CharField(max_length=30)),
            ],
            options={
                'managed': False,
                'db_table': 'stasiun',
            },
        ),
        migrations.CreateModel(
            name='Pemesan',
            fields=[
                ('kode_booking', models.ForeignKey(primary_key=True, to='tiketapi.Booking', serialize=False, db_column='kode_booking')),
                ('nama_pemesan', models.CharField(max_length=64)),
                ('email_pemesan', models.CharField(max_length=64)),
                ('nomor_telepon_pemesan', models.CharField(max_length=16)),
                ('alamat_pemesan', models.TextField()),
            ],
            options={
                'managed': False,
                'db_table': 'pemesan',
            },
        ),
    ]
