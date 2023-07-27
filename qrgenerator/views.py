from django.shortcuts import render
from django.http import HttpResponse
from .models import QRModel
import time
import pyqrcode
from django.conf import settings

# Create your views here.
def saveqrimage(text):
    image = pyqrcode.create(text)
    imagename = str(int(time.time()))
    image.png("./media/Qr-Images/{}.png".format(imagename), scale=10)
    return imagename

def Home(request):
    context = {"is_qr": "false"}
    if request.method == "POST":
        text = request.POST.get('comment')
        qr_image = "Qr-Images/{}.png".format(saveqrimage(text))
        data = QRModel.objects.create(text=text, qr_image=qr_image)
        context.update({"data": data, "is_qr": "true"})
    return render(request, 'qrgenerator/home.html', context=context)
