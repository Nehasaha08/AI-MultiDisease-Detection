# 🩺 AI Multi-Disease Detection System

## 📌 Overview

The **AI Multi-Disease Detection System** is a deep learning–based web application that assists users in detecting diseases from medical images. The system automatically identifies the uploaded image type and predicts the corresponding disease using trained convolutional neural network (CNN) models.

The application also provides secure user authentication, prediction history, downloadable PDF reports, and an AI-powered medical assistant for educational health-related queries.

> **Disclaimer:** This application is developed for educational and research purposes only. It is **not intended to replace professional medical diagnosis or treatment**.

---

# ✨ Features

* 🔐 User Registration & Login Authentication
* 🩺 Automatic Medical Image Type Classification
* 🫁 Pneumonia Detection (Chest X-ray)
* 🧠 Brain Tumor Detection (MRI)
* 🎗️ Breast Cancer Detection
* 📄 Downloadable PDF Medical Reports
* 📊 Prediction History
* 🤖 AI Health Assistant Chatbot
* 💻 Interactive Streamlit Dashboard
* 🗄️ SQLite Database for User & Prediction Management

---

# 🧠 Diseases Supported

| Image Type     | Disease Detection      |
| -------------- | ---------------------- |
| Chest X-ray    | Pneumonia / Normal     |
| Brain MRI      | Brain Tumor / No Tumor |
| Breast Imaging | Malignant / Benign     |

---

# 🏗️ Project Architecture

```text
AI-Multi-Disease-Detection/
│
├── app.py
├── README.md
├── requirements.txt
│
├── Auth/
│   ├── login.py
│   └── register.py
│
├── models/
│   ├── imageprocess_model.h5
│   ├── pneumonia_model.h5
│   ├── brain-tumor_model.h5
│   └── breast-cancer_model.h5
│
├── utils/
│   ├── prediction.py
│   ├── image_processing.py
│   ├── database.py
│   ├── pdf_generator.py
│   └── chatbot.py
│
├── database/
│   ├── users.db
│   └── prediction_history.db
│
├── assets/
│
└── reports/
```

---

# 🛠️ Technologies Used

### Programming Language

* Python

### Framework

* Streamlit

### Deep Learning

* TensorFlow
* Keras

### Models

* EfficientNetB0 (Medical Image Type Classification)
* DenseNet121 (Disease Detection Models)

### Database

* SQLite

### Libraries

* NumPy
* Pillow
* Pandas
* Requests
* FPDF

---



# 🚀 How It Works

1. Register a new account or log in.
2. Upload a supported medical image.
3. The EfficientNetB0 model identifies the image type.
4. The corresponding disease-specific model performs prediction.
5. The prediction result and confidence score are displayed.
6. A PDF report can be generated and downloaded.
7. Prediction history is stored for the logged-in user.
8. Users can interact with the AI Health Assistant for educational medical information.

---

# 📊 Models Used

| Model          | Purpose                           |
| -------------- | --------------------------------- |
| EfficientNetB0 | Medical Image Type Classification |
| DenseNet121    | Pneumonia Detection               |
| DenseNet121    | Brain Tumor Detection             |
| DenseNet121    | Breast Cancer Detection           |

---

# 🔒 Authentication

* Secure User Registration
* Secure Login
* Session Management
* Individual Prediction History

---

# 📄 PDF Reports

The application automatically generates downloadable PDF reports containing:

* Username
* Image Type
* Predicted Disease
* Confidence Score
* Prediction Date & Time

---

# 🤖 AI Health Assistant

The integrated AI assistant provides educational information about:

* Medical conditions
* Symptoms
* Preventive measures
* General health awareness

**Note:** The chatbot does not provide medical diagnoses or replace healthcare professionals.

---



# 📌 Future Enhancements

* Additional disease detection models
* Doctor recommendation system
* Cloud database integration
* Email report delivery
* Explainable AI visualizations (Grad-CAM)
* Mobile application
* Multi-language support

---

# 👩‍💻 Author

**Neha Saha**

B.Tech – Computer Science & Engineering (Cyber Security)

---



## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.
