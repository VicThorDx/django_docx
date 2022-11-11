from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .forms import ClienteForm
import datetime
from pathlib import Path
from docxtpl import DocxTemplate,InlineImage
from docx.shared import Mm
from PIL import Image
from docx2pdf import convert
import os 
from docx import Document
from base64 import b64encode
from urllib import request
import io


# Create your views here.

def index(request):
    if request.method == "POST":
        form = ClienteForm(request.POST, request.FILES)  
        if form.is_valid:
            file = request.FILES['image']
            data = file.read()
            imageStream = io.BytesIO(data)
            imageFile = Image.open(imageStream)

            base_dir = Path(__file__).parent
            word_template_path = base_dir / "docxmedia/pacientetemplate.docx"
            today = datetime.date.today()
            doc = DocxTemplate(word_template_path)
            context = {
                "CLIENT": "Bombardeen Guatemala",
                "NAME": form["nombre"].value(),
                "DATE": today,
                "IMAGE": InlineImage(doc, "https://www.purina-latam.com/sites/g/files/auxxlc391/files/styles/social_share_large/public/Que_debes_saber_antes_de_adoptar_un_gatito.jpg?itok=guFplHEU")

            }
            doc.render(context)

            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
            response['Content-Disposition'] = 'attachment; filename=paciente.docx'
            doc.save(response)


            return response 
    else:
         return render(request, "index.html", {
        "form": ClienteForm()
    })