import numpy as np
import os
from tensorflow.keras.preprocessing import image 
from tensorflow.keras.models import load_model 

model = load_model("final_model/ResNet50TransferLearning.h5")
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
