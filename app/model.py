import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array #type:ignore
from tensorflow.keras.applications.resnet50 import preprocess_input #type:ignore
import numpy as np
import os

MODEL_PATH = os.path.normpath("Models/ResNet50_Transfer_Learning/ResNet50TransferLearning.h5")
model = tf.keras.models.load_model(MODEL_PATH) #type:ignore

CLASS_NAMES = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']

def predict(image_path):
    image = load_img(image_path, target_size=(384, 384))
    image_array = img_to_array(image)
    image_array = np.expand_dims(image_array, axis=0)
    image_array = preprocess_input(image_array)  

    predictions = model.predict(image_array)[0]
    predicted_index = np.argmax(predictions)
    predicted_label = CLASS_NAMES[predicted_index]
    confidence = predictions[predicted_index]

    print("Raw predictions:", predictions)  
    return predicted_label, confidence
