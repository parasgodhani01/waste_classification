import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array #type:ignore

# Load the pre-trained waste classification model
model = tf.keras.models.load_model('../final_model/ResNet50TransferLearning.h5')  #type:ignore
 
# Waste labels
waste_labels = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']

# Start video capture
cap = cv2.VideoCapture(0)  # Use 0 for default webcam

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for natural interaction
    frame = cv2.flip(frame, 1)

    # Define the region of interest (ROI) for classification
    # You can draw a box at the center where user can place the waste item
    height, width, _ = frame.shape
    box_size = 300
    x1 = width // 2 - box_size // 2
    y1 = height // 2 - box_size // 2
    x2 = x1 + box_size
    y2 = y1 + box_size

    # Draw the rectangle where users should place waste item
    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    roi = frame[y1:y2, x1:x2]

    # Preprocess the ROI for model prediction
    roi_resized = cv2.resize(roi, (384, 384))
    roi_resized = roi_resized.astype("float") / 255.0
    roi_array = img_to_array(roi_resized)
    roi_array = np.expand_dims(roi_array, axis=0)

    # Predict the class
    prediction = model.predict(roi_array)[0]
    label = waste_labels[np.argmax(prediction)]

    # Display label above the box
    cv2.putText(frame, f"Prediction: {label}", (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (36, 255, 12), 2)

    # Show the frame
    cv2.imwrite("output_frame.jpg", frame)
    print(f"Predicted: {label}")

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()
