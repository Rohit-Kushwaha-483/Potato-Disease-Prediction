import os
import requests
from django.conf import settings
from django.core.files.storage import default_storage
from django.shortcuts import render
from .forms import UploadImageForm
from .api_config import FASTAPI_URL  # The URL to your FastAPI endpoint

def predict_image(request):
    result = None
    image_url = None

    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = request.FILES['image']

            # Save image so we can show it in the UI
            filename = default_storage.save(image.name, image)
            image_url = os.path.join(settings.MEDIA_URL, filename)

            # Rewind file pointer so FastAPI gets the full data
            image.seek(0)

            try:
                response = requests.post(
                    FASTAPI_URL,
                    files={"file": image.read()}
                )
                if response.ok:
                    result = response.json()
                    print("Prediction:", result)
                else:
                    print("FastAPI error:", response.status_code, response.text)
            except Exception as e:
                print(f"Error communicating with FastAPI: {e}")
    else:
        form = UploadImageForm()

    return render(request, 'predictor/predict.html', {
        'form': form,
        'image_url': image_url,
        'result': result
    })
