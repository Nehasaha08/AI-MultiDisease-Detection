import os
from huggingface_hub import hf_hub_download
from tensorflow.keras.models import load_model

REPO_ID = "nehasaha08/ai-multidisease-models/tree/main/models"

os.makedirs("models", exist_ok=True)


def download_model(filename):
    return hf_hub_download(
        repo_id=REPO_ID,
        filename=filename,
        local_dir="models",
        local_dir_use_symlinks=False
    )


image_path = download_model("imageprocess_model.h5")
pneumonia_path = download_model("pneumonia_model.h5")
brain_path = download_model("brain-tumor_model.h5")
breast_path = download_model("breast-cancer_model.h5")


image_classifier = load_model(image_path)
pneumonia_model = load_model(pneumonia_path)
brain_model = load_model(brain_path)
breast_model = load_model(breast_path)
