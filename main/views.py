from django.shortcuts import render
from sys import platform
from .models import base_magasin
from django.db import models
from django.views.generic import DetailView
#from PIL import Image
#im = Image.open("logo.jpg")
#(width, height) = im.size

if platform == "linux" or platform == "linux2":
    var_for_show = "komp"
elif platform == "darwin":
    var_for_show = "komp"
elif platform == "win32":
    var_for_show = "komp"

class tovarDetailView(DetailView):
    if platform == "linux" or platform == "linux2":
        var_for_show = "komp"
    elif platform == "darwin":
        var_for_show = "komp"
    elif platform == "win32":
        var_for_show = "komp"
    extra_context = {"var_for_show": var_for_show}
    model = base_magasin
    template_name = 'main/detail_view.html'
    context_object_name = 'tovars'

class Images(models.Model):
    model_img = models.ImageField(upload_to='static/img')


def home_page(request):
    if platform == "linux" or platform == "linux2":
        var_for_show = "komp"
    elif platform == "darwin":
        var_for_show = "komp"
    elif platform == "win32":
        var_for_show = "komp"

    tovars = base_magasin.objects.order_by("price")
    for el in tovars:
        imageforsearchpath = el.photo_1
        #
    #num_img = Images.objects.order_by('-date')
    data = {"var_for_show": var_for_show, "tovars": tovars}
    return render(request, 'main/home_page.html', data)



def kr_page(request):
    if platform == "linux" or platform == "linux2":
        var_for_show = "komp"
    elif platform == "darwin":
        var_for_show = "komp"
    elif platform == "win32":
        var_for_show = "komp"


    tovars = base_magasin.objects.order_by("price")
    data = {"var_for_show": var_for_show, "tovars": tovars}
    return render(request, 'main/kr_page.html', data)

def vish_page(request):
    if platform == "linux" or platform == "linux2":
        var_for_show = "komp"
    elif platform == "darwin":
        var_for_show = "komp"
    elif platform == "win32":
        var_for_show = "komp"
    tovars = base_magasin.objects.order_by("price")
    data = {"var_for_show": var_for_show, "tovars": tovars}
    return render(request, 'main/vish_page.html', data)


def ost_page(request):
    if platform == "linux" or platform == "linux2":
        var_for_show = "komp"
    elif platform == "darwin":
        var_for_show = "komp"
    elif platform == "win32":
        var_for_show = "komp"
    tovars = base_magasin.objects.order_by("price")
    data = {"var_for_show": var_for_show, "tovars": tovars}
    return render(request, 'main/ost_page.html', data)