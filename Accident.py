import streamlit as st
import pandas as pd
import pickle
st.title("Welcome to Accident Data Analysis")
st.sidebar.header('User Input Parameters')

def user_input():
    lc = st.sidebar.selectbox('Light_Conditions',('Daylight', 'Darkness - no lighting', 'Darkness - lights lit',
                                                 'Darkness - lights unlit', 'Darkness - lighting unknown'))
    nc = st.sidebar.number_input("Number_of_Casualties",min_value=0,max_value=30,step=1)
    nv = st.sidebar.number_input("Number_of_Vehicles",min_value=0,max_value=30,step=1)
    pf = st.sidebar.selectbox('Police_Force',('Strathclyde', 'Cumbria', 'Cheshire', 'Northumbria','North Yorkshire',
                                              'West Yorkshire','Staffordshire','Warwickshire', 'Leicestershire',
                                              'Cambridgeshire', 'Norfolk','Hampshire', 'Kent', 'Sussex', 'Avon and Somerset',
                                              'Gloucestershire', 'North Wales', 'Gwent', 'South Wales','Grampian', 'Tayside', 
                                              'Fife', 'Lothian and Borders', 'Central','Dumfries and Galloway', 'Metropolitan Police',
                                              'City of London','Lancashire', 'Merseyside', 'Greater Manchester', 'Durham',
                                              'South Yorkshire', 'Humberside', 'Cleveland', 'West Midlands','West Mercia',
                                              'Derbyshire', 'Nottinghamshire', 'Lincolnshire','Northamptonshire', 'Suffolk',
                                              'Bedfordshire', 'Hertfordshire','Essex', 'Thames Valley', 'Surrey', 'Devon and Cornwall',
                                              'Wiltshire', 'Dorset', 'Dyfed-Powys', 'Northern'))
    rsc = st.radio("Road_Surface_Conditions",['Dry', 'Wet or damp', 'Frost or ice', 'Flood over 3cm. deep','Snow'])
    rt = st.sidebar.selectbox("Road_Type",('Single carriageway', 'Dual carriageway', 'One way street','Roundabout', 'Slip road'))
    sl = st.sidebar.number_input("Speed_limit",min_value=0,max_value=120,step=10)
    ur = st.radio("Urban_or_Rural_Area",['Rural', 'Urban'])
    wc = st.sidebar.selectbox('Weather_Conditions',('Fine no high winds', 'Fine + high winds', 'Raining no high winds','Other',
                                                 'Fog or mist', 'Raining + high winds','Snowing + high winds', 'Snowing no high winds'))
    vt = st.sidebar.selectbox('Vehicle_Type',('Car', 'Motorcycle 125cc and under', 'Motorcycle 50cc and under',
                                                    'Goods 7.5 tonnes mgw and over','Bus or coach (17 or more pass seats)',
                                                    'Van / Goods 3.5 tonnes mgw or under', 'Taxi/Private hire car',
                                                    'Minibus (8 - 16 passenger seats)', 'Agricultural vehicle','Motorcycle over 500cc',
                                                    'Motorcycle over 125cc and up to 500cc','Goods over 3.5t. and under 7.5t', 'Other vehicle'))
    am = st.sidebar.number_input("Accident_Month",min_value=0,max_value=12,step=1)
    ah = st.sidebar.number_input("Accident_Hours",min_value=0,max_value=24,step=1)
    
    data = {'Light_Conditions' : lc,
            'Number_of_Casualties' : nc,
            'Number_of_Vehicles' : nv,
            'Police_Force' : pf,
            'Road_Surface_Conditions' : rsc,
            'Road_Type' : rt,
            'Speed_limit' : sl,
            'Urban_or_Rural_Area' : ur,
            'Weather_Conditions' : wc,
            'Vehicle_Type' : vt,
            'Accident_Month' : am,
            'Accident_Hours' : ah}
    
    features = pd.DataFrame(data,index=[0])
    return features

df = user_input()
st.write(df)

with open(file = "Accident_Analysis_set_Final_model.sav",mode="rb") as a2:
    model = pickle.load(a2)
    
prediction = model.predict(df)

st.subheader('Predicted Result')

st.write(prediction)
st.write(prediction[0])
