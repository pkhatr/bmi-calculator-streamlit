import streamlit as st
import pandas as pd

#st.set_page_config(layout='wide')

st.markdown('<H1 style="text-align: center;">HEALTH CONDITION CALCULATOR</H1>', unsafe_allow_html=True)
#st.title('HEALTH CONDITION CALCULATOR')
st.markdown('<p style="text-align: center;">Know your Body Mass Index (BMI), Body Fat Percentage, Basal Metabolic Rate (BMR), and Ideal Weight</p>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([2, 1, 3])

with col1:
    # Get User Input
    st.markdown('<H3 style="color: rgb(100, 52, 58); font-style: italic;">Inputs</H3>', unsafe_allow_html=True)
    gender = st.selectbox('Gender', ['Male', 'Female'])
    age = st.number_input('Age', min_value=1, step=1, value=25)
    st.write('Height')
    ft = st.number_input('feet', min_value=0, step=1, max_value=12, value=5)
    inch = st.number_input('inch', min_value=0, step=1, max_value=11, value=0)
    wt = st.number_input('Weight (lbs)', min_value=0.1, step=0.1, value=120.0)

#Calculate bmi
bmi = 703 * wt / (ft*12 + inch)**2

# Calculate body fat percentage 
if gender == 'Male' and age >=18:
    bfp = 1.20 * bmi + 0.23 * age - 16.2
elif gender == 'Female' and age >= 18:
    bfp = 1.20 * bmi + 0.23 * age - 5.4
elif gender == 'Male' and age < 18:
    bfp = 1.51 * bmi - 0.70 * age - 2.2
else:
    bfp = 1.51 * bmi - 0.70 * age + 1.4

# Calculate bmr
if gender == 'Male':
    bmr = 10 * (wt * 0.453592) + 6.25 * 2.54 * (ft * 12 + inch) - 5 * age + 5
else:
    bmr = 10 * (wt * 0.453592) + 6.25 *2.54 * (ft * 12 + inch) - 5 * age - 161

# Calculate ideal weight range(idw_min, idw_max)
idw_min = 18.5 * (ft*12 + inch)**2 / 703
idw_max = 25 * (ft*12 + inch)**2 / 703

with col3:
    st.markdown('<H3 style="color: rgb(100, 52, 58); font-style: italic;">Results</H3>', unsafe_allow_html=True)
    st.write(pd.DataFrame({'Metrics': ['BMI', 'Body Fat', 'BMR', 'Ideal Weight'], 
    'Values': [str(round(bmi, 1)) + ' kg/m\u00b2', str(round(bfp, 1)) + '%', str(round(bmr, 1)) + ' calories/day', '{} - {} lbs'.format(round(idw_min, 1), round(idw_max, 1))]}))

    # Final observation
    if(bmi < 16):
        st.error('Condition: Extremely Underweight')
    elif(bmi >= 16 and bmi < 18.5):
        st.warning('Condition: Underweight')
    elif(bmi >= 18.5 and bmi < 25):
        st.success('Condition: Healthy')       
    elif(bmi >= 25 and bmi < 30):
        st.warning('Condition: Overweight')
    elif(bmi >= 30):
        st.error('Condition: Extremely Overweight')
    st.markdown('<p style="font-weight:bold;">Note:</p>', unsafe_allow_html=True)
    st.write('Healthy BMI range: 18.5 - 25 kg/m\u00b2')