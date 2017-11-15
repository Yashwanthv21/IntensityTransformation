from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from forms import UploadImageForm, OperationsForm
from django.http import HttpResponseRedirect

import base64
def home(request):
    return render(request,'home.html')
    # return HttpResponse("success")


def app(request):
    form = UploadImageForm
    return render(request, 'app.html',{'form': form})



def upload_file(request):
    form = UploadImageForm(request.POST, request.FILES)
    if form.is_valid():
        base64Image = base64.b64encode(form.cleaned_data['image'].read())
        # print(base64Image)

        return render(request, 'app.html', {'form': UploadImageForm, 'image': displayImage(base64Image), 'ops': OperationsForm, 'imageData':base64Image})

def displayImage(base64Image):
    return "data:image/jpeg;base64," + base64Image


def operations(request):
    from negative import negativeImage
    if request.POST.get("operation","") == 1: #Negative Image hardcoded in Forms.py
        img = request.POST.get("imageData","")
        res = negativeImage(img)

    return render(request, 'app.html', {'form': UploadImageForm, 'image': displayImage(img), 'ops': OperationsForm, 'imageData':img, 'result': displayImage(res)})