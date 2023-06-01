import numpy as np
import pandas as pd
import streamlit as st
import pickle
import warnings
warnings.filterwarnings('ignore')


# loading the saved model
loaded_model = pickle.load(open('C:/Users/ankit/OneDrive/Desktop/streamlit_dashboard/trained_model_bike.pkl'
                                , 'rb'))
temp=0
humidity = 0
wind_speed = 0
visibility = 0
solar_radiation = 0
rainfall = 0
snowfall = 0
Hour_1 = 1
Hour_2 = 0
Hour_3 = 0
Hour_4 = 0
Hour_5 = 0
Hour_6 = 0
Hour_7 = 0
Hour_8 = 0
Hour_9 = 0
Hour_10 = 0
Hour_11 = 0
Hour_12 = 0
Hour_13 = 0
Hour_14 = 0
Hour_15 = 0
Hour_16 = 0
Hour_17 = 0
Hour_18 = 0
Hour_19 = 0
Hour_20 = 0
Hour_21 = 0
Hour_22 = 0
Hour_23 = 0
Seasons_Spring = 1
Seasons_Summer = 0
Seasons_Winter = 0
Holiday_NoHoliday=1
Functioning_Day_Yes	=0
weekdays_weekend_1 = 0
month_2 = 1
month_3 = 0
month_4 = 0
month_5 = 0
month_6 = 0
month_7 = 0
month_8 = 0
month_9 = 0
month_10 = 0
month_11 = 0
month_12 = 0

def main():

    # giving a title
    st.title('Bike Sharing Demand Prediction')

    # getting the input data from the user
    temp = st.text_input('Temperature in Celsius')
    humidity = st.text_input('Humidity %')
    wind_speed = st.text_input('Windspeed in m/s')
    visibility = st.text_input('Visibility')
    solar_radiation = st.text_input('Solar radiation in MJ/m2')
    rainfall = st.text_input('rainfall in mm')
    snowfall = st.text_input('snowfall in cm')
    hours = st.radio("Hour of the day", ("0 = 12:00 am", "1 = 1:00 am", "2 = 2:00 am",'3 = 3:00 am','4 = 4:00 am',
                                         '5 = 5:00 am',"6 = 6:00 am","7 = 7:00 am","8 = 8:00 am","9 = 9:00 am",
                                         "10 = 10:00 am","11 = 11:00 am","12 = 12:00 pm","13 = 1:00 pm","14 = 2:00 pm",
                                         "15 = 3:00 pm","16 = 4:00 pm","17 = 5:00 pm","18 = 6:00 pm","19 = 7:00 pm",
                                         "20 = 8:00 pm","21 = 9:00 pm","22 = 10:00 pm","23 = 11:00 pm"))
    if (hours == "0 = 12:00 am"):
        Hour_1 = 1
        Hour_2 = 0
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 0

    if (hours == "1 = 1:00 am"):
        Hour_1 = 0
        Hour_2 = 1
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 0

    if (hours == "2 = 2:00 am"):
        Hour_1 = 0
        Hour_2 = 0
        Hour_3 = 1
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 0

    if (hours == "3 = 3:00 am"):
        Hour_1 = 0
        Hour_2 = 0
        Hour_3 = 0
        Hour_4 = 1
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 0

    if (hours == "4 = 4:00 am"):
        Hour_1 = 0
        Hour_2 = 0
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 1
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 0

    if (hours == "5 = 5:00 am"):
        Hour_1 = 0
        Hour_2 = 0
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 1
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 0

    if (hours == "6 = 6:00 am"):
        Hour_1 = 0
        Hour_2 = 0
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 1
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 0

    if (hours == "7 = 7:00 am"):
        Hour_1 = 0
        Hour_2 = 0
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 1
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 0

    if (hours == "8 = 8:00 am"):
        Hour_1 = 0
        Hour_2 = 0
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 1
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 0

    if (hours == "9 = 9:00 am"):
        Hour_1 = 0
        Hour_2 = 0
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 1
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 0

    if (hours == "10 = 10:00 am"):
        Hour_1 = 0
        Hour_2 = 0
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 1
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 0

    if (hours == "11 = 11:00 am"):
        Hour_1 = 0
        Hour_2 = 1
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 1
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 0

    if (hours == "12 = 12:00 am"):
        Hour_1 = 0
        Hour_2 = 0
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 1
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 0

    if (hours == "13 = 1:00 pm"):
        Hour_1 = 0
        Hour_2 = 0
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 1
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 0

    if (hours == "14 = 1:00 pm"):
        Hour_1 = 0
        Hour_2 = 0
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 1
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 0

    if (hours == "15 = 3:00 pm"):
        Hour_1 = 0
        Hour_2 = 0
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 1
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 0

    if (hours == "16 = 4:00 pm"):
        Hour_1 = 0
        Hour_2 = 0
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 1
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 0

    if (hours == "17 = 5:00 pm"):
        Hour_1 = 0
        Hour_2 = 0
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 1
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 0

    if (hours == "18 = 6:00 pm"):
        Hour_1 = 0
        Hour_2 = 0
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 1
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 0

    if (hours == "19 = 7:00 pm"):
        Hour_1 = 0
        Hour_2 = 0
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 1
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 0

    if (hours == "20 = 8:00 pm"):
        Hour_1 = 0
        Hour_2 = 0
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 1
        Hour_22 = 0
        Hour_23 = 0

    if (hours == "21 = 9:00 pm"):
        Hour_1 = 0
        Hour_2 = 0
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 1
        Hour_23 = 0

    if (hours == "22 = 10:00 pm"):
        Hour_1 = 0
        Hour_2 = 1
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 1

    if (hours == "23 = 11:00 pm"):
        Hour_1 = 0
        Hour_2 = 1
        Hour_3 = 0
        Hour_4 = 0
        Hour_5 = 0
        Hour_6 = 0
        Hour_7 = 0
        Hour_8 = 0
        Hour_9 = 0
        Hour_10 = 0
        Hour_11 = 0
        Hour_12 = 0
        Hour_13 = 0
        Hour_14 = 0
        Hour_15 = 0
        Hour_16 = 0
        Hour_17 = 0
        Hour_18 = 0
        Hour_19 = 0
        Hour_20 = 0
        Hour_21 = 0
        Hour_22 = 0
        Hour_23 = 0

    Seasons_Spring = st.radio("Season", ("0 = Spring", "1 = Summer", "2 = Winter", "3 = Autumn"))
    if (Seasons_Spring == "0 = Spring"):

        Seasons_Winter = 0
        Seasons_Summer = 0
        Seasons_Spring = 1

    if (Seasons_Spring == "1 = Summer"):
        Seasons_Winter = 0
        Seasons_Summer = 1
        Seasons_Spring = 0

    if (Seasons_Spring == "2 = Winter"):
        Seasons_Winter = 1
        Seasons_Summer = 0
        Seasons_Spring = 0

    if (Seasons_Spring == "3 = Autumn"):
        Seasons_Winter = 0
        Seasons_Summer = 0
        Seasons_Spring = 0

    Holiday_NoHoliday= st.radio("Select Whether Holiday or not Holiday:", ('1', '0'))
    if (Holiday_NoHoliday == '1'):
        st.info("Holiday")
    else:
        st.info("No Holiday")

    Functioning_Day_Yes = st.radio("Select Whether Functioning Day or Not:", ('1', '0'))
    if (Functioning_Day_Yes == '1'):
        st.info("Functional Day")
    else:
        st.info("Non Functional Day")

    weekdays_weekend_1 = st.radio("Select Whether Weekdays or weekend:", ('1', '0'))
    if (weekdays_weekend_1 == '1'):
        st.info("weekend")
    else:
        st.info("weekdays")

    months = st.radio("Month of the year", ("0 = Jan", "1 = Feb", "2 = Mar",'3 = April','4 = May',
                                         '5 = Jun',"6 = Jul","7 = Aug","8 = Sep","9 = Oct",
                                         "10 = Nov","11 = Dec"))
    if (months == "0 = Jan"):
        month_2 = 0
        month_3 = 0

        month_4 = 0
        month_5 = 0
        month_6 = 0
        month_7 = 0
        month_8 = 0
        month_9 = 0
        month_10 = 0
        month_11 = 0
        month_12 = 0

    if (months == "1 = Feb"):
        month_2 = 1
        month_3 = 0

        month_4 = 0
        month_5 = 0
        month_6 = 0
        month_7 = 0
        month_8 = 0
        month_9 = 0
        month_10 = 0
        month_11 = 0
        month_12 = 0

    if (months == "2 = Mar"):
        month_2 = 0
        month_3 = 1

        month_4 = 0
        month_5 = 0
        month_6 = 0
        month_7 = 0
        month_8 = 0
        month_9 = 0
        month_10 = 0
        month_11 = 0
        month_12 = 0

    if (months == "3 = April"):
        month_2 = 0

        month_3 = 0
        month_4 = 1
        month_5 = 0
        month_6 = 0
        month_7 = 0
        month_8 = 0
        month_9 = 0
        month_10 = 0
        month_11 = 0
        month_12 = 0

    if (months == "4 = May"):
        month_2 = 0

        month_3 = 0
        month_4 = 0
        month_5 = 1
        month_6 = 0
        month_7 = 0
        month_8 = 0
        month_9 = 0
        month_10 = 0
        month_11 = 0
        month_12 = 0

    if (months == "5 = June"):
        month_2 = 0

        month_3 = 0
        month_4 = 0
        month_5 = 0
        month_6 = 1
        month_7 = 0
        month_8 = 0
        month_9 = 0
        month_10 = 0
        month_11 = 0
        month_12 = 0

    if (months == "6 = Jul"):
        month_2 = 0

        month_3 = 0
        month_4 = 0
        month_5 = 0
        month_6 = 0
        month_7 = 1
        month_8 = 0
        month_9 = 0
        month_10 = 0
        month_11 = 0
        month_12 = 0

    if (months == "7 = Aug"):
        month_2 = 0

        month_3 = 0
        month_4 = 0
        month_5 = 0
        month_6 = 0
        month_7 = 0
        month_8 = 1
        month_9 = 0
        month_10 = 0
        month_11 = 0
        month_12 = 0

    if (months == "8 = Sep"):
        month_2 = 0

        month_3 = 0
        month_4 = 0
        month_5 = 0
        month_6 = 0
        month_7 = 0
        month_8 = 0
        month_9 = 1
        month_10 = 0
        month_11 = 0
        month_12 = 0

    if (months == "9 = Oct"):
        month_2 = 0

        month_3 = 0
        month_4 = 0
        month_5 = 0
        month_6 = 0
        month_7 = 0
        month_8 = 0
        month_9 = 0
        month_10 = 1
        month_11 = 0
        month_12 = 0

    if (months == "10 = Nov"):
        month_2 = 0

        month_3 = 0
        month_4 = 0
        month_5 = 0
        month_6 = 0
        month_7 = 0
        month_8 = 0
        month_9 = 0
        month_10 = 0
        month_11 = 1
        month_12 = 0

    if (months == "11 = Dec"):
        month_2 = 0

        month_3 = 0
        month_4 = 0
        month_5 = 0
        month_6 = 0
        month_7 = 0
        month_8 = 0
        month_9 = 0
        month_10 = 0
        month_11 = 0
        month_12 = 1

# creating a button for Prediction

    if st.button('Bike Sharing Demand Result'):
        demand_prediction = loaded_model.predict([[temp,humidity,wind_speed,visibility,solar_radiation,rainfall,snowfall,Hour_1,
                                                   Hour_2,Hour_3,Hour_4,Hour_5,Hour_6,Hour_7,Hour_8,Hour_9,Hour_10,Hour_11,Hour_12,
                                                   Hour_13,Hour_14,Hour_15,Hour_16,Hour_17,Hour_18,Hour_19,Hour_20,Hour_21,Hour_22,
                                                   Hour_23,Seasons_Spring,Seasons_Summer,Seasons_Winter,Holiday_NoHoliday,Functioning_Day_Yes,
                                                   weekdays_weekend_1,month_2,month_3,month_4,month_5,month_6,month_7,month_8,month_9,
                                                   month_10,month_11,month_12]])

        output = round(demand_prediction[0])
        st.success("Bike Count is {}".format(output))


if __name__ == '__main__':
    main()





