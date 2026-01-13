import streamlit as st
from app import get_weather_data


st.title("OpenWeatherMap GUI") # To display the main title on top

st.write("Select a city and a language") # A shorter title below the main title#

# First define available options for cities and languages
cities = ["Berlin", "Paris", "New York"]  
languages = {"English": "eng", "German": "de"}  

selected_city = st.selectbox("Choose a city:", cities) # Letting the user select a city
selected_language = st.selectbox("Choose language:", list(languages.keys())) # Letting the user selecting a language

if st.button("Get Weather Data"): # When the button "Get Weather Data" is clicked...
    weather_data = get_weather_data() # Calls our function from app.py

    # Only display the selected city
    info = weather_data.get(selected_city)
    if info: # From here on indexing to information and dipslaying them...
        st.subheader(selected_city) # Which city was selected?
        st.write(f"Temperature: {info['temperature']} °C") # the temp of that city
        if selected_language == "English": # the weather descriptions of that city
            st.write(f"Weather: {info['weather_en']}")
        else:
            st.write(f"Wetter: {info['weather_de']}")
    else:
        st.write("No data available for this city.")


# Can be run with these statements in the terminal:
# 1. First change the directory to project directory: e.g. cd 01_Projects\0203_WebService_Streamlit (Probably not the best solution...)
# 2. Then run: streamlit run streamlit_gui.py