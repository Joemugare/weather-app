import streamlit as st
import requests

# Set your OpenWeatherMap API key here
api_key = 'abb54687f0029b17322ac8ed183fbe14'

# Streamlit app title
st.title("Mugare 5-Day Weather Forecast :earth_africa:")

# User input for city
city = st.text_input("Enter a city name:")

if st.button("Get Weather"):
    if city:
        # API request to OpenWeatherMap
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"
        response = requests.get(url)
        data = response.json()

        if data["cod"] == "200":
            # Display weather information for the next 5 days
            forecasts = data["list"]
            
            for forecast in forecasts:
                # Extract and display weather information for each day
                date = forecast["dt_txt"]
                weather_description = forecast["weather"][0]["description"]
                temperature = forecast["main"]["temp"] - 273.15  # Convert to Celsius
                humidity = forecast["main"]["humidity"]
                wind_speed = forecast["wind"]["speed"]

                # Define emojis based on weather descriptions
                emoji = ""
                if "light rain" in weather_description.lower():
                    emoji = "🌦️ :partly_sunny_rain:"
                elif "humidity" in weather_description.lower():
                    emoji = "🌫️ :foggy:"
                elif "overcast clouds" in weather_description.lower():
                    emoji = "☁️ :sun_behind_cloud:"
                elif "broken clouds" in weather_description.lower():
                    emoji = "🌥️ :barely_sunny:"

                st.write(f"Date: {date}")
                st.write(f"Weather: {weather_description} {emoji}")
                st.write(f"Temperature: {temperature:.2f} °C 🌡️")
                st.write(f"Humidity: {humidity}% 🌟")
                st.write(f"Wind Speed: {wind_speed} m/s 🌪️")
                st.write("---")
        else:
            st.write("City not found. Please enter a valid city name. 🌩️")
    else:
        st.write("Please enter a city name. 🌧️")
