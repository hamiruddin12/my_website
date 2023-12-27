from django.http import HttpResponse
from django.template import loader

def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())
def produk(request):
  template = loader.get_template('produk.html')
  return HttpResponse(template.render())