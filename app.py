import streamlit as st 
import pandas as pd
import pickle

st.title("Car Price Prediction")

Kms_Driven=st.number_input("How many kilometer the car was driven?")
Present_Price=st.number_input("Enter the Present price of the car.")
submit=st.button("Submit")

with open('modellasso.pkl','rb') as file:  
    model = pickle.load(file)


if submit==True:
    prediction_data=pd.DataFrame({
        'Present_Price':[Present_Price],
                'Kms_Driven':[Kms_Driven]
})
        
    prediction=model.predict(prediction_data)
    st.text_area('Result',prediction)
   
    


	