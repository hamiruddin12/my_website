from django import forms

from .models import kategori


class frompoduk(forms.Form):
  kategori = forms.ModelChoiceField(queryset=kategori.objects.all())
  nama = forms.CharField()
  harga = forms.IntegerField()


