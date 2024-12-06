import streamlit as st
import pickle
import numpy as np

# import the model
model = pickle.load(open('model.pkl', 'rb'))
df = pickle.load(open('df1.pkl', 'rb'))

#homepage with input box
st.title("Heart Disease Predictor")

age = st.number_input('Age', step=1)

sex = st.selectbox('Sex',df['sex'].unique())

cpt = st.selectbox('Chest pain type',df['chest_pain_type'].unique())

rbp = st.number_input('resting_blood_pressure', step=1)

ch = st.number_input('cholesterol', step=1)

fbs = st.selectbox('fasting_blood_sugar',df['fasting_blood_sugar'].unique())

re = st.selectbox('resting_electrocardiogram',df['resting_electrocardiogram'].unique())

mhr = st.number_input('max_heart_rate_achieved	', step=1)

eia = st.selectbox('exercise_induced_angina',df['exercise_induced_angina'].unique())

sd= st.number_input('Agest_depression', step=0.1)

ss = st.selectbox('st_slope',df['st_slope'].unique())

mv = st.selectbox('num_major_vessels',df['num_major_vessels'].unique())

th= st.selectbox('thalassemia',df['thalassemia'].unique())

#main button
if st.button('Predict Disease'):
    sex = 1 if(sex=='male') else 0


    if cpt=="asymptomatic":
        cpt=0
    elif cpt=="atypical angina":
        cpt=1
    elif cpt=="non-anginal pain":
        cpt=2
    else:
        cpt=3


    fbs = 1 if(fbs=='lower than 120mg/ml') else 0

    if re=="ST-T wave abnormality":
        re=0
    elif re=="normal":
        re=2
    else:
        re=1


    eia = 1 if(eia=='yes') else 0


    if ss=="downsloping":
        ss=0
    elif ss=="upsloping":
        ss=2
    else:
        ss=1


    if th=="fixed defect":
        th=0
    elif th=="normal":
        th=1
    else:
        th=2
    
#shape the query for prediction
    query = np.array([age, sex, cpt, rbp, ch, fbs, re, mhr, eia, sd, ss, mv, th])   #by default it is a column matrix
    query = query.reshape(1,13)     #convert into row matrix

    ans = model.predict(query)[0]
    ans = "YES" if ans==1 else "NO"

    st.title("Heart Disease Found: " + ans)