import streamlit as st
import pickle as pkl
import numpy as np

def app():
    
    st.title("Home")

    with open('region_encoder.pkl' , 'rb') as file:
        region_encoder = pkl.load(file)
    with open('sex_encoder.pkl' , 'rb') as file:
        sex_encoder = pkl.load(file)
    with open('smoker_encoder.pkl' , 'rb') as file:
        smoker_encoder = pkl.load(file)
    with open('scaler.pkl'  , 'rb') as file:
        scaler = pkl.load(file)
    with open('model.pkl' , 'rb') as file:
        model = pkl.load(file)

    value1 = st.slider(label = 'Select Age:' , min_value=18 , max_value=65 , value=36 , step = 1)
    value2 = st.selectbox(label='Select Sex:' , options=('male' , 'female'))
    value3 = st.slider(label="Select BMI(Body Mass Index):", min_value=15 , max_value=40 , value = 25 , step = 1)
    value4 = st.slider(label='Select Number of Children:' , min_value=0 , max_value=5 , value=2 , step=1)
    value5 = st.selectbox(label='Did you Smoke?' , options = ('yes' , 'no'))
    value6 = st.selectbox(label='Whats your Region?' , options= ('northeast' , 'northwest' , 'southeast'  , 'southwest'))

    if st.button('Predict'):
        value2 = sex_encoder.transform([value2])
        value5 = smoker_encoder.transform([value5])
        value6 = region_encoder.transform([value6])
        input = np.array([[value1 , value2[0] , value3 , value4 , value5[0] , value6[0]]])
        scaler.transform(input)
        cost = model.predict(input)
        st.success(f'The Predict Medical Cost is {cost[0]}')