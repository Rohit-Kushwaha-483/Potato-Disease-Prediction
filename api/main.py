from fastapi import FastAPI, File, UploadFile   # FastAPI to create the web API, File and UploadFile for handling file uploads
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO  # To read the image as a byte stream
from PIL import Image  # Python Imaging Library (PIL) to handle image processing
import tensorflow as tf

# Create an instance of the FastAPI web application
app = FastAPI()

# Load the trained model.
MODEL = tf.keras.models.load_model("../saved_models/2/potato_disease_model.keras")

# These are the possible classes (labels) that the model can predict
CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

# Define a simple health check endpoint to see if the server is working
@app.get("/ping")
async def ping():
    return "Hello, I am alive"

# Helper function to read the uploaded image and convert it into a NumPy array
def read_file_as_image(data) -> np.ndarray:
    # Convert the byte data into an image using PIL, then convert it into a NumPy array
    image = np.array(Image.open(BytesIO(data)))
    return image

# Define the main prediction endpoint
@app.post("/predict")
async def predict(file: UploadFile = File(...)):   # This endpoint expects a file to be uploaded
    # Read the uploaded file as an image
    image = read_file_as_image(await file.read())
    
    # Add an extra dimension to the image to match the input shape expected by the model (batch size of 1)
    img_batch = np.expand_dims(image, axis=0)
    
    # Use the model to make predictions on the image
    # predictions = array([[3.5349350e-07, 9.9999690e-01, 2.7641331e-06]], dtype=float32)
    predictions = MODEL.predict(img_batch)

    # Get the class with the highest probability (most likely prediction)    
    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    
    # Get the confidence of the prediction (highest probability)
    confidence = f"{round(np.max(predictions[0]) * 100, 2)} %"

    # Return the predicted class and the confidence level
    return {
        'class': predicted_class,  # Name of the predicted class
        'confidence': confidence  # Confidence of the prediction (converted to a float)
    }

# Run the FastAPI application if the script is executed directly
if __name__ == "__main__":
    # Start the Uvicorn server to run the FastAPI app on localhost at port 8000
    uvicorn.run(app, host='localhost', port=8000)


# https://youtu.be/ttqHMljwacw?list=PLPbgcxheSpE1gl5WkrwtmRiCwiGMM8NdH&t=1550

