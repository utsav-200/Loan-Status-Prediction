# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 00:38:33 2023

@author: KIIT
"""

import numpy as np
import pickle 
import streamlit as st

#Loading The Model 
loaded_model=pickle.load(open('D:/Data Science/Projects/Loan Status Prediction/trained_model.sav','rb'))

#Creating a function for loan status prediction 
def loan_prediction(input_data):
    #Assuming The Input as a list of string objects 
    input_data = [str(x) for x in input_data]   
    
    #Converting Categorical variables into numerical 
    gender_mapping = {'Male': 0, 'Female': 1}
    input_data[0] = gender_mapping.get(input_data[0], -1)
    
    married_mapping = {'No': 0, 'Yes': 1}
    input_data[1] = married_mapping.get(input_data[1], -1)
    
    education_mapping={'Graduate':0,'Not Graduate':1}
    input_data[3] = education_mapping.get(input_data[3], -1)
    
    self_mapping={'No':0,'Yes':1}
    input_data[4] = self_mapping.get(input_data[4], -1)
    
    Property_mapping={'Rural':0,'Semiurban':1,'Urban':2}
    input_data[10] = Property_mapping.get(input_data[10], -1)
    #changing the data into numpy array 
    input_data_as_array=np.asarray(input_data)

    #reshape the array as we are predicting for one instance 
    input_data_reshaped=input_data_as_array.reshape(1,-1)
    #predictijg
    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)

    if(prediction[0]==0):
        return 'Loan Is Not Approved'
    else:
        return 'Loan Is Approved'
    
#using The Streamlit Library To create the function 
def main():
    #Giving The title to webpage 
    st.title('Loan Status Prediction')
    
    #Getting The Input From user 
    
    Gender = st.selectbox('Gender Of The Person', ('Male', 'Female'))
    Married = st.selectbox('Wether a Person Is Married Or Not', ('No', 'Yes'))
    Dependents = st.number_input('Are There Any Dependents', min_value=0, step=1)
    Education = st.selectbox('Educated Or Not', ('Graduate', 'Not Graduate'))
    Self_Employed = st.selectbox('Self Employed Or Not', ('No', 'Yes'))
    ApplicantIncome = st.number_input('Income', min_value=0)
    CoapplicantIncome = st.number_input('Coapplicant Income', min_value=0)
    LoanAmount = st.number_input('Loan Amount', min_value=0)
    Loan_Amount_Term = st.number_input('Time', min_value=0)
    Credit_History = st.selectbox('Credit History', ('0.0', '1.0'))
    Property_Area = st.selectbox('Area Of The Property', ('Rural', 'Semiurban', 'Urban'))

    
    #Code For Prediction
    status=''
    
    #creating a button
    if st.button('Loan Status Prediction'):
        status=loan_prediction([Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome	,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area])
    
    
    st.success(status)
    
if __name__=='__main__':
    main()