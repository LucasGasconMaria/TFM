import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import base64
import io
import os

from django.template.response import TemplateResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render
from django.http import HttpResponse
from django.templatetags.static import static

from .predictor import predict_image

from django.core.files.storage import FileSystemStorage


class CustomFileSystemStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        self.delete(name)
        return name


# Def index function
def index(request):
    message = ""
    prediction = ""

    try:
        image = request.FILES["image"]

        # Read the image
        image_content = image.read()
        imag = cv2.imdecode(np.frombuffer(image_content, np.uint8), cv2.IMREAD_COLOR)

        # image details
        image_url = f"data:image/{image.content_type};base64,{base64.b64encode(image_content).decode('utf-8')}"

        # Process the image in-memory
        img_from_ar = Image.fromarray(imag, 'RGB')
        resized_image = img_from_ar.resize((256, 256))

        test_image = np.expand_dims(resized_image, axis=0)
        def_image = test_image / 255.0

        class_names = {0: 'Basal cell carcinoma',
                       1: 'Melanoma',
                       2: 'Nevus'}

        # Make prediction using the predict_image function
        alteration, result_probability, result, prediction = predict_image(def_image)
        probability_values = result[0]

        # Plot the bar chart
        plt.switch_backend('agg')
        fig, ax = plt.subplots()
        ax.bar(class_names.values(), probability_values, color=['blue', 'orange', 'green'])
        ax.set_title('Probability Distribution')
        ax.set_xlabel('Classes')
        ax.set_ylabel('Probability')
        ax.set_ylim(0, 1)

        # Save the Matplotlib plot to a BytesIO buffer
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        plt.close()

        # Encode the image as base64
        plot_image = base64.b64encode(buffer.getvalue()).decode('utf-8')

        return TemplateResponse(
            request,
            "index.html",
            {
                "message": message,
                "image_url": image_url,
                "alteration": alteration,
                "result_probability": result_probability,
                "plot_image": plot_image,
                "prediction": prediction,
            },
        )

    except MultiValueDictKeyError:
        return TemplateResponse(
            request,
            "index.html",
            {"message": "No Image Selected"},
        )
    except Exception as e:
        # Print the exception for debugging
        print(f"An error occurred: {e}")
        return TemplateResponse(
            request,
            "index.html",
            {"message": "Error processing the image."},
        )


# Def bcc function
def bcc(request):
    return render(request, 'BCC.html')


# Def melanoma function
def melanoma(request):
    return render(request, 'Melanoma.html')


# Def nevus function
def nevus(request):
    return render(request, 'Nevus.html')


# Def references function
def references(request):
    return render(request, 'References.html')


# Def privacy function
def privacy(request):
    return render(request, 'Privacy.html')


# Def specifications function
def specifications(request):
    return render(request, 'Specifications.html')


# Def about_me function
def about_me(request):
    return render(request, 'AboutMe.html')

