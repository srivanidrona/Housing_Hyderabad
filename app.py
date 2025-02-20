import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
model_path="C:\CLG\PROJECTS\houseprice\models\house_pricehyd.pkl" 
with open(model_path, 'rb') as file:
    model = pickle.load(file)
amenities_list = ['Resale', 'MaintenanceStaff', 'Gymnasium',
                  'ShoppingMall', 'Intercom', 'SportsFacility', 'ATM', 'School',
                  'PowerBackup', 'StaffQuarter', 'Cafeteria', 'WashingMachine',
                  'Gasconnection', 'AC', 'Wifi', 'BED', 'Microwave', 'GolfCourse',
                  'Wardrobe']

location_list = [
    "Nizampet", "Hitech City", "Manikonda", "Alwal", "Kukatpally", "Gachibowli", "Tellapur", "Kokapet", "Hyder Nagar", "Mehdipatnam", "Narsingi", "Khajaguda Nanakramguda Road", "Madhapur", "Puppalaguda", 
    "Begumpet", "Banjara Hills", "AS Rao Nagar", "Pragathi Nagar Kukatpally", "Miyapur", "Mallampet", "Nanakramguda", "Attapur", "West Marredpally", "Kompally", "Sri Nagar Colony", "Hakimpet", "Pocharam", 
    "Nagole", "LB Nagar", "Meerpet", "Kachiguda", "Masab Tank", "Kondapur", "Saroornagar", "Uppal Kalan", "Mallapur", "Rajendra Nagar", "Beeramguda", "Moosapet", "Bachupally", "Toli Chowki", "Lakdikapul",
    "Tarnaka", "Kistareddypet", "Hafeezpet", "Shaikpet", "Amberpet", "Kapra", "Trimalgherry", "Habsiguda", "Sanath Nagar", "Darga Khaliz Khan", "Kothaguda", "Balanagar", "Jubilee Hills", "Raidurgam", 
    "Murad Nagar", "Chandanagar", "East Marredpally", "Aminpur", "Gajularamaram", "Serilingampally", "Malkajgiri", "Mettuguda", "Venkat Nagar Colony", "Kondakal", "Gopanpally", "Somajiguda", 
    "Nallagandla Gachibowli", "Krishna Reddy Pet", "Bolarum", "Zamistanpur", "Madhura Nagar", "Ghansi Bazaar", "Chintalakunta", "Chinthal Basthi", "Nallakunta", "Bowenpally", "Bandlaguda Jagir", 
    "Boduppal", "Neknampur", "Appa Junction Peerancheru", "Ambedkar Nagar", "Vanasthalipuram", "Moula Ali", "Gandipet", "Nacharam", "Appa Junction", "Qutub Shahi Tombs", "Abids", "Dilsukh Nagar",
    "Quthbullapur", "Sainikpuri", "KTR Colony", "Bollaram", "Karmanghat", "Gajulramaram Kukatpally", "Uppal", "Cherlapalli", "Himayat Nagar", "Rhoda Mistri Nagar", "Chintalmet", "Hitex Road", "ECIL",
    "Boiguda", "ECIL Main Road", "ECIL Cross Road", "Rajbhavan Road Somajiguda", "Ramachandra Puram", "TellapurOsman Nagar Road", "Mansoorabad", "KRCR Colony Road", "Pragati Nagar", "Padmarao Nagar",
    "Paramount Colony Toli Chowki", "BK Guda Internal Road", "Muthangi", "Yapral", "Narayanguda", "Kollur", "Bachupally Road", "Old Bowenpally", "Adibatla", "Methodist Colony", "Ameerpet",
    "ALIND Employees Colony", "Khizra Enclave", "Medchal", "Dammaiguda", "Suchitra", "Whitefields", "Mayuri Nagar",]

location_encoder = LabelEncoder()
location_encoder.fit(location_list)
def encode_amenities(selected_amenities):
    encoded_amenities = [1 if amenity in selected_amenities else 0 for amenity in amenities_list]
    return encoded_amenities


st.title('House Price Prediction')
st.header('Hyderabad')

area_input = st.number_input('Area (Square Feet)', min_value=0)
location_input = st.selectbox('Location', location_list)

selected_amenities = st.multiselect('Select Amenities', amenities_list, default=[])

if st.button('Predict Price'):
    encoded_amenities = encode_amenities(selected_amenities)
    location_input_encoded = location_encoder.transform([location_input])[0]
    features = [[location_input_encoded, area_input] + encoded_amenities]

    
    prediction = round(model.predict(features)[0])
    lb = prediction
    ub = prediction
    st.subheader(f'Predicted Price: ₹{prediction}')
    st.write(f'Estimated Range: ₹{lb} - ₹{ub}')
