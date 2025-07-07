# 🥔 Potato Disease Prediction

A full-stack deep learning application that identifies **potato leaf diseases** using image classification. This project combines a **CNN model** with a **FastAPI backend** and **Django frontend**, delivering a real-time tool for farmers and agricultural researchers to diagnose **Early Blight**, **Late Blight**, or **Healthy** leaf conditions by simply uploading an image.

---

## 🚀 Features

- ✅ CNN trained on potato leaf dataset  
- ✅ FastAPI server for real-time image prediction  
- ✅ Django frontend with intuitive image upload interface  
- ✅ Predicts: `Early Blight`, `Late Blight`, or `Healthy`  
- ✅ Returns confidence score with prediction  
- ✅ Jupyter Notebook for model training and experimentation  

---

## 🧠 Technologies Used

| Layer         | Technologies Used                        |
|---------------|-------------------------------------------|
| Deep Learning | TensorFlow, Keras                         |
| Backend       | FastAPI, Uvicorn                          |
| Frontend      | Django                                    |
| Data          | Custom image dataset (Potato Leaf Images) |
| Image Utils   | Pillow, NumPy                             |

---

## 🗂️ Folder Structure

```plaintext
potato-disease-classification/
├── api/             # FastAPI backend (main.py)
├── frontend/        # Django frontend for UI
├── saved_models/    # Trained CNN model files (.keras)
├── training/        # Dataset & model training notebooks
└── README.md        # Project documentation
```

## ⚙️ Setup Instructions
🔁 Clone the Repository

```git clone https://github.com/Rohit-Kushwaha-483/Potato-Disease-Prediction.git
cd Potato-Disease-Prediction
```

## 📦 Install Required Packages
```
pip install -r requirements.txt
```

## 🚀 Run FastAPI Backend
```
cd api
uvicorn main:app --reload
```

## 💻 Run Django Frontend
| ⚠️ Ensure Django is configured to connect with the FastAPI backend (e.g., proper URLs, CORS setup).
```
cd ../frontend
python manage.py runserver
```

## 🧪 API Usage
- Endpoint: /predict
- Method: POST
- Request: Upload an image as form-data (key: file)
- Response Example:

```
{
  "class": "Early Blight",
  "confidence": "98.45%"
}
```

## Screenshot - UI

### Prediction Class : Late blight

<img src="https://i.ibb.co/FkMgmR11/late-blight.png" alt="late-blight" border="2">

### Prediction Class : Healthy

<img src="https://i.ibb.co/YBJbymZQ/healthy.png" alt="healthy" border="2">