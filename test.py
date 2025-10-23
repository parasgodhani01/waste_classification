from keras.saving import load_model  # or from tensorflow.keras.models if using .h5
from PIL import Image
import numpy as np

# === CONFIGURATION ===
MODEL_PATH = "Models/ResNet50_Transfer_Learning/ResNet50TransferLearning.h5"  # or "model.h5"
IMAGE_PATH = "test_dir/image4.jpg"  # replace with your test image path
TARGET_SIZE = (384, 384)  # update this if your model uses different input size

# === LOAD MODEL ===
model = load_model(MODEL_PATH)
print("Model loaded successfully.")

# === PREPROCESS IMAGE ===
def preprocess_image(path, target_size):
    image = Image.open(path).convert("RGB")
    image = image.resize(target_size)
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)  # (1, h, w, c)
    return img_array

# === PREDICT ===
image = preprocess_image(IMAGE_PATH, TARGET_SIZE)
prediction = model.predict(image)

# === DECODE OUTPUT ===
predicted_class = int(np.argmax(prediction))
label_map = {0: "Plastic", 1: "Metal", 2: "Glass", 3: "Paper"}
predicted_label = label_map.get(predicted_class, "Unknown")

print(f"Image: {IMAGE_PATH}")
print(f"Predicted Class: {predicted_class}")
print(f"Label: {predicted_label}")
print(f"Raw Probabilities: {prediction.tolist()}")
