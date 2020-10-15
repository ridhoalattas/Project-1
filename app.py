import warnings
warnings.filterwarnings('ignore')
import streamlit as st
import os
import numpy as np
from PIL import Image, ImageEnhance
from cv2 import cv2
from win32com.client import Dispatch
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array, save_img

model = load_model('weights-improvement-27-0.86_simpleModel.h5')

st.title("Breast Histopathology Prediction")
st.write("Build with Streamlit, Keras, Tensorflow & Python")
st.set_option('deprecation.showfileUploaderEncoding', False)
activites = ["Prediction", "About"]
choice = st.sidebar.selectbox("Select Activities",activites)

if choice=="Prediction" : 
    st.subheader("Please Upload Your Sample")
    img_file=st.file_uploader("Upload File", type=['png', 'jpg', 'jpeg'])
    if img_file is not None : 
        up_img=Image.open(img_file)
        st.image(up_img)
    if st.button("Predict") :
        img=np.asarray(up_img, dtype=np.uint8)
        img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img=np.array(img) / 255.0
        img=cv2.resize(img, (50,50))
        prediction=model.predict(img.reshape(1, 50, 50, 3))
        predict = prediction.argmax(axis=1)[0]
        label = "Patient Negative IDC (-)" if predict == 0 else "Patient Positive (+) IDC"
        st.warning(label)
        st.write(prediction)

elif choice == "About" :         
    st.subheader("This Application is Developed by Achmad Ridho")
