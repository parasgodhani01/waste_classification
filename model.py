import numpy as np
from tensorflow.keras.preprocessing import image #type:ignore
import os
from tensorflow.keras.models import load_model #type:ignore

# Load model (adjust the path based on your project structure)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "final_model", "ResNet50TransferLearning.h5")

model = load_model(MODEL_PATH)
# Class labels (update if needed)
class_names = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']

def predict(img_path):
    if not os.path.isfile(img_path):
        raise ValueError(f"Invalid image path: {img_path}")

    try:
        img = image.load_img(img_path, target_size=(384, 384))  
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0

        predictions = model.predict(img_array)
        label_index = np.argmax(predictions[0])
        label = class_names[label_index]
        confidence = predictions[0][label_index]
        return label, confidence

    except Exception as e:
        raise RuntimeError(f"Error in prediction: {str(e)}")
