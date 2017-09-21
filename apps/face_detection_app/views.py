from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages
import os
import cv2
import sys


# Create your views here.
def handle_uploaded_file(f):
    with open('./apps/face_detection_app/static/face_detection_app/img/upload.png', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def index(request):
    return render(request, 'face_detection_app/index.html')

def upload(request):
    if 'file' in request.FILES:
        handle_uploaded_file(request.FILES['file'])
        # os.system('python ./apps/face_detection_app/face_detect_cv3.py ./apps/face_detection_app/upload.png ./apps/face_detection_app/haarcascade_frontalface_default.xml
        # Get user supplied values
        imagePath = './apps/face_detection_app/static/face_detection_app/img/upload.png'
        cascPath = "./apps/face_detection_app/haarcascade_frontalface_default.xml"

        # Create the haar cascade
        faceCascade = cv2.CascadeClassifier(cascPath)

        # Read the image
        image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
            #flags = cv2.CV_HAAR_SCALE_IMAGE
        )

        print("Found {0} faces!".format(len(faces)))
        # messages.info(request, 'static/face_detection_app/img/upload.png')
        messages.info(request, 'Found ' + str(len(faces)) + ' face(s)!')
    return redirect('/')

                #   <div class = 'photo'>
                #     <img src = '{{message}}' alt = 'photo'>
                #   </div>
