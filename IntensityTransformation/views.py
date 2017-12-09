from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from forms import UploadImageForm, OperationsForm, UploadTwoImageForm
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
    if request.POST.get("operation","") == '1': #Negative Image hardcoded in Forms.py
        img = request.POST.get("imageData","")
        res = negativeImage(img)

    from power_gamma import adjust_gamma
    if request.POST.get("operation","") == '2':
        img = request.POST.get("imageData", "")
        res = adjust_gamma(img)

    from hist_match import histmatch
    if request.POST.get("operation", "") == '3':
        img = request.POST.get("imageData", "")
        img1 = request.POST.get("imageData1", "")
        res = histmatch(img, img1)

    from hist_eq import histogram_equalization
    if request.POST.get("operation","") == '4':
        img = request.POST.get("imageData", "")
        res = histogram_equalization(img)



    return render(request, 'app.html', {'form': UploadImageForm, 'image': displayImage(img), 'ops': OperationsForm, 'imageData':img, 'result': displayImage(res)})


def negative(request):
    if request.method == 'GET':
        form = UploadImageForm
        return render(request, 'image_negative.html', {'form': form})
    elif request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            base64Image = base64.b64encode(form.cleaned_data['image'].read())
            from negative import negativeImage
            res = negativeImage(base64Image)
            return render(request, 'image_negative.html',
                      {'form': UploadImageForm, 'image': displayImage(base64Image),'result': displayImage(res)})


def power(request):
    if request.method == 'GET':
        form = UploadImageForm
        return render(request, 'power-gamma.html', {'form': form})
    elif request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            base64Image = base64.b64encode(form.cleaned_data['image'].read())
            gamma = request.POST.get("gamma", "")
            from power_gamma import adjust_gamma
            res = adjust_gamma(base64Image,float(gamma))
            return render(request, 'power-gamma.html',
                      {'form': UploadImageForm, 'image': displayImage(base64Image),'result': displayImage(res)})


def matching(request):
    if request.method == 'GET':
        form = UploadTwoImageForm
        return render(request, 'hist_matching.html', {'form': form})
    elif request.method == 'POST':
        form = UploadTwoImageForm(request.POST, request.FILES)
        if form.is_valid():
            base64Image = base64.b64encode(form.cleaned_data['image'].read())
            from hist_match import histmatch
            img2 = base64.b64encode(form.cleaned_data['image2'].read())
            print(img2)
            res = histmatch(base64Image, img2)
            return render(request, 'hist_matching.html',
                      {'form': UploadTwoImageForm, 'image': displayImage(base64Image),'image2':displayImage(img2),'result': displayImage(res)})


def equilisation(request):
    if request.method == 'GET':
        form = UploadImageForm
        return render(request, 'hist_equilisation.html', {'form': form})
    elif request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            base64Image = base64.b64encode(form.cleaned_data['image'].read())
            from hist_eq import histogram_equalization
            res = histogram_equalization(base64Image)
            return render(request, 'hist_equilisation.html',
                      {'form': UploadImageForm, 'image': displayImage(base64Image),'result': displayImage(res)})

def histogram(request):
    if request.method == 'GET':
        form = UploadImageForm
        return render(request, 'histogram.html', {'form': form})
    elif request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            base64Image = base64.b64encode(form.cleaned_data['image'].read())
            from histogram import Image2Histogram
            res = Image2Histogram(base64Image)
            return render(request, 'histogram.html',
                      {'form': UploadImageForm, 'image': displayImage(base64Image),'result': res})