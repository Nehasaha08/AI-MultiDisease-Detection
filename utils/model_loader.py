from tensorflow.keras.models import load_model

# Load once when app starts
image_classifier = load_model(
    "models/imageprocess_model.h5"
)

pneumonia_model = load_model(
    "models/pneumonia_model.h5"
)

brain_model = load_model(
    "models/brain-tumor_model.h5"
)

breast_model = load_model(
    "models/breast-cancer_model.h5"
)