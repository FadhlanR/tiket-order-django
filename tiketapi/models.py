# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

class Booking(models.Model):
    kode_booking = models.AutoField(primary_key=True)
    id_layanan_kereta = models.ForeignKey('LayananKereta', db_column='id_layanan_kereta')
    jumlah_penumpang = models.IntegerField()
    waktu_mulai_booking = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        managed = False
        db_table = 'booking'


class CaraBayar(models.Model):
    id_cara_bayar = models.AutoField(primary_key=True)
    nama_cara_bayar = models.CharField(max_length=40)
    detil_cara_bayar = models.TextField()

    class Meta:
        managed = False
        db_table = 'cara_bayar'


class Kereta(models.Model):
    id_kereta = models.AutoField(primary_key=True)
    nama_kereta = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'kereta'


class LayananKereta(models.Model):
    id_layanan_kereta = models.AutoField(primary_key=True)
    id_kereta = models.ForeignKey(Kereta, db_column='id_kereta')
    kapasitas = models.IntegerField()
    harga_tiket = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'layanan_kereta'


class Pembayaran(models.Model):
    kode_pembayaran = models.AutoField(primary_key=True)
    kode_booking = models.ForeignKey(Booking, db_column='kode_booking')
    id_cara_bayar = models.ForeignKey(CaraBayar, db_column='id_cara_bayar')
    waktu_penagihan = models.DateTimeField(default=datetime.now, blank=True)
    waktu_pembayaran = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pembayaran'


class Pemesan(models.Model):
    kode_booking = models.ForeignKey(Booking, db_column='kode_booking', primary_key=True)
    nama_pemesan = models.CharField(max_length=64)
    email_pemesan = models.CharField(max_length=64)
    nomor_telepon_pemesan = models.CharField(max_length=16)
    alamat_pemesan = models.TextField()

    class Meta:
        managed = False
        db_table = 'pemesan'


class Penumpang(models.Model):
    id_penumpang = models.AutoField(primary_key=True)
    kode_booking = models.ForeignKey(Booking, db_column='kode_booking')
    nomor_identitas = models.CharField(max_length=24)
    nama_penumpang = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'penumpang'
        unique_together = (('kode_booking', 'nomor_identitas'),)


class RangkaianPerjalanan(models.Model):
    id_rangkaian_perjalanan = models.AutoField(primary_key=True)
    id_layanan_kereta = models.ForeignKey(LayananKereta, db_column='id_layanan_kereta')
    id_stasiun = models.ForeignKey('Stasiun', db_column='id_stasiun')
    jenis_perjalanan = models.CharField(max_length=1)
    waktu = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'rangkaian_perjalanan'
        unique_together = (('id_layanan_kereta', 'id_stasiun', 'jenis_perjalanan'),)


class Stasiun(models.Model):
    id_stasiun = models.CharField(primary_key=True, max_length=3)
    nama_stasiun = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'stasiun'
