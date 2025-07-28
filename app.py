import streamlit as st
from api.weather_api import get_weather_data
from utils.formatter import format_weather
from datetime import datetime, timedelta


st.set_page_config(page_title="🌦️ Weather Dashboard", layout="wide")

st.divider(width= 200)
st.title("🌤️ Weather Forecast App")
st.divider(width= 200)


city = st.text_input("📍 Enter City", width= 300 )
get_details = st.button("Get Details")



if city and get_details:
    data = get_weather_data(city)

    if data:
        format_data = format_weather(data)
        
         # box1 
        with st.container(border=True):
            st.markdown("##### Quick glance")
            
            # checking units for temp
            # code here

            col1,col2,col3,col4 = st.columns(4)

            with col1:
                st.metric(label = "🌡️ Temperature",value = f"{format_data['current']['temp_c']} °C ", border=True)
                st.metric(label = "🌡️ Wind Direction",value = f"{format_data['current']['wind_dir']} ", border=True)

            with col2:
                st.metric(label = "💧 Humidity", value= f"{format_data['current']['humidity']} %",border=True)
                st.metric(label = "💧 Condition", value= f"{format_data['current']['condition']} %",border=True)

            with col3:
                st.metric(label = " feelslike",value = f"{format_data['current']['feelslike_c']}°C", border=True)
                st.metric(label = " UV index",value = f"{format_data['current']['uv_index']}", border=True)

            with col4:
                st.metric(label = "💧 Wind Speed", value= f"{format_data['current']['wind_kph']} kph",border=True)
                st.metric(label = "💧 Visibility", value= f"{format_data['current']['vis_km']} kph",border=True)
            st.markdown(
                f"""
                <div style='font-size: 0.9rem; color: #555; text-align: center;'>
                    🕒 Local Time: <strong>{format_data['location']['localtime']}</strong>;
                </div>
                """, unsafe_allow_html=True
                )
        epa_index = format_data['air_quality']['us_epa_index']
        epa_mapping = {

            1: ("Good", "🟢", "#00e400"),
            2: ("Moderate", "🟡", "#ffff00"),
            3: ("Unhealthy for Sensitive Groups", "🟠", "#ff7e00"),
            4: ("Unhealthy", "🔴", "#ff0000"),
            5: ("Very Unhealthy", "🟣", "#8f3f97"),
            6: ("Hazardous", "🟤", "#7e0023"),
        }
        label, emoji, bg_color = epa_mapping.get(epa_index, ("Unknown", "❓", "#cccccc"))

        # ========== 📦 Box 2: Air Quality ==========
        with st.container(border=True):

            st.markdown("#### 🧪 Air Quality Details")


            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric("🌫️ PM2.5", f"{round(format_data['air_quality']['pm2_5'], 1)} µg/m³", border= True)
                st.metric("🌀 PM10", f"{round(format_data['air_quality']['pm10'], 1)} µg/m³", border= True)

            with col2:
                st.metric("🚭 CO", f"{round(format_data['air_quality']['CO'], 1)} µg/m³", border= True)
                st.metric("🧪 NO₂", f"{round(format_data['air_quality']['no2'], 1)} µg/m³", border= True)

            with col3:
                st.metric("🌐 O₃", f"{round(format_data['air_quality']['o3'], 1)} µg/m³", border= True)
                st.metric("🌋 SO₂", f"{round(format_data['air_quality']['so2'], 1)} µg/m³", border= True)

            with col4:
                
                st.metric(
                label="🏥 AQI",
                value=f"{epa_index}",
                delta=f"{emoji} {label}",
                border= True,
                help="Based on US EPA index (1 = Good, 6 = Hazardous)")

                st.markdown("</div>", unsafe_allow_html=True)
       
       
        with st.container():
            col1,col2,col3 = st.columns(3)

            with col1:
                st.metric("🌅 Sunrise", format_data['astro']['sunrise'], border= True)
                st.metric("🌅 sunset", format_data['astro']['sunset'], border= True)
            with col2:
                st.metric("🌙 moonrise", format_data['astro']['moonrise'], border= True)
                st.metric("🌙 moonset", format_data['astro']['moonset'], border= True)
            with col3:
                st.metric("moon_phase", format_data['astro']['moon_phase'], border = True)



                