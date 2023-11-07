#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import requests

# Set your OpenWeatherMap API key here
api_key = 'abb54687f0029b17322ac8ed183fbe14'

# Streamlit app title
st.title("Simple Weather App")

# User input for city
city = st.text_input("Enter a city name:")

if st.button("Get Weather"):
    if city:
        # API request to OpenWeatherMap
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            # Display weather information
            weather_description = data["weather"][0]["description"]
            temperature = data["main"]["temp"] - 273.15  # Convert to Celsius
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            st.write(f"Weather in {city}: {weather_description}")
            st.write(f"Temperature: {temperature:.2f} °C")
            st.write(f"Humidity: {humidity}%")
            st.write(f"Wind Speed: {wind_speed} m/s")
        else:
            st.write("City not found. Please enter a valid city name.")
    else:
        st.write("Please enter a city name.")



# In[ ]:




