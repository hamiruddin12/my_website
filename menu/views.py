from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .forms import frompoduk
from .models import produk, kategori
from django.shortcuts import redirect

def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def data_produk(request):
  submitted = False
  if request.method == "POST":
    form = frompoduk(request.POST)
    if form.is_valid():
      simpandata = produk.objects.create(
        nama=form.cleaned_data.get("nama"),
        harga=form.cleaned_data.get("harga"),
        katgori=form.cleaned_data.get("kategori"),
      )
      simpandata.save()
      return HttpResponseRedirect("/produk?submitted=True")
  else:
    form = frompoduk
    if "submitted" in request.GET:
      submitted = True

  data_produk = produk.objects.all()

  context = {
    "form": frompoduk,
    "produk": data_produk,
  }
  template = loader.get_template('produk.html')
  return HttpResponse(template.render(context, request))

def hapus_produk(request, produk_id):
  data_produk = produk.objects.get(id=produk_id)
  data_produk.delete()
  return redirect("produk")