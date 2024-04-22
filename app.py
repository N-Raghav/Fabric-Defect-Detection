import streamlit as st
import numpy as np
from PIL import Image
from ultralytics import YOLO

model_path = r'fabric_defect_detection\runs\classify\train2\weights\best.pt'
class_names = ['Defect Detected', 'No Defect Detected']


model = YOLO(model_path)


def classify_image(image):
    results = model(image, conf=0.5)
    predicted_class_id = results[0].probs.top1
    predicted_class_name = class_names[predicted_class_id]
    predicted_probability = results[0].probs[predicted_class_id]
    return predicted_class_name, predicted_probability


def main():
    st.title("Fabric Defect Detection")
    uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'png'])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        predictions = classify_image(np.array(image))
        predicted_class, probability = predictions
        if predicted_class == 'Defect Detected':
            st.error(f"{predicted_class}")
        else:
            st.success(f"{predicted_class}")


if __name__ == '__main__':
    main()