import os
from huggingface_hub import hf_hub_download
from tensorflow.keras.models import load_model
from utils.image_processing import preprocess_image

REPO_ID = "nehasaha08/ai-multidisease-models"

os.makedirs("models", exist_ok=True)


def get_model(filename):
    return hf_hub_download(
        repo_id=REPO_ID,
        filename=filename,
        local_dir="models"
    )


image_classifier = load_model(
    get_model("imageprocess_model.h5")
)

pneumonia_model = load_model(
    get_model("pneumonia_model.h5")
)

brain_model = load_model(
    get_model("brain-tumor_model.h5")
)

breast_model = load_model(
    get_model("breast-cancer_model.h5")
)

IMAGE_TYPES = [
    "Chest Xray",
    "Brain MRI",
    "Breast Cancer"
]


def predict_image_type(image):
    img = preprocess_image(image)
    pred = image_classifier.predict(img)
    idx = pred.argmax()
    return IMAGE_TYPES[idx]


def predict_disease(image):
    image_type = predict_image_type(image)
    img = preprocess_image(image)

    if image_type == "Chest Xray":
        p = pneumonia_model.predict(img)[0][0]
        disease = "Pneumonia" if p > 0.5 else "Normal"
        confidence = float(max(p, 1 - p) * 100)

    elif image_type == "Brain MRI":
        p = brain_model.predict(img)[0][0]
        disease = "Tumor" if p > 0.5 else "No Tumor"
        confidence = float(max(p, 1 - p) * 100)

    else:
        p = breast_model.predict(img)[0][0]
        disease = "Malignant" if p > 0.5 else "Benign"
        confidence = float(max(p, 1 - p) * 100)

    return image_type, disease, confidence
