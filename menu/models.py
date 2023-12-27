from django.db import models
from django.contrib import admin

# Create your models here.


class kategori(models.Model):
    namaproduk = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.namaproduk}"


class produk(models.Model):
    katgori = models.ForeignKey(kategori, on_delete=models.CASCADE)
    nama = models.CharField(max_length=255)
    harga = models.IntegerField()

    def __str__(self):
        return f"{self.nama}"

