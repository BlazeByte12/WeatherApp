import streamlit as st
import requests
import base64

API = "http://127.0.0.1:8000/api"

st.set_page_config(
    page_title="Weather App",
    page_icon="🌤",
    layout="centered"
)

#slika
def get_base64_image(path):
    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode()

bg = get_base64_image("header_bg.jpg")

#hero css /sve
st.markdown(
    f"""
    <style>

    /* REMOVE STREAMLIT TOP PADDING */
    .block-container {{
        padding-top: 0rem;
    }}

    header {{ visibility: hidden; }}

    /* FULL WIDTH HERO */
    .hero-wrapper {{
        width: 100vw;
        margin-left: calc(-50vw + 50%);
        background-image: url("data:image/jpg;base64,{bg}");
        background-size: cover;
        background-position: center;
        padding: 45px 0;
    }}

    .hero-content {{
        max-width: 1100px;
        margin: auto;
        padding: 0 20px;
        color: white;
    }}

    .hero-content h1 {{
        font-size: 42px;
        margin-bottom: 8px;
        text-shadow: 2px 2px 6px rgba(0,0,0,0.7);
    }}

    .hero-content p {{
        font-size: 18px;
        max-width: 600px;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.7);
        opacity: 0.95;
    }}

    </style>
    """,
    unsafe_allow_html=True
)

#header
st.markdown(
    """
    <div class="hero-wrapper">
        <div class="hero-content">
            <h1>OpenWeather</h1>
            <p>Weather forecasts, nowcasts and history in a fast and elegant way</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

#input
st.markdown("<br>", unsafe_allow_html=True)
city = st.text_input("🌍 Enter city name", placeholder="e.g. London")

#weather
if st.button("📍 Current Weather", use_container_width=True):
    r = requests.get(f"{API}/weather/current", params={"city": city})

    if r.ok:
        d = r.json()

        st.subheader(f"📍 Current Weather in {city}")
        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("🌡 Temperature (°C)", d.get("temperature", "N/A"))
            st.metric("🤔 Feels Like", d.get("feels_like", "N/A"))
            st.metric("💧 Humidity (%)", d.get("humidity", "N/A"))
            st.metric("☀️ UV Index", d.get("uv_index", "N/A"))

        with col2:
            st.metric("🌬 Wind (km/h)", d.get("wind_speed", "N/A"))
            st.metric("🧭 Direction", d.get("wind_direction", "N/A"))
            st.metric("🔽 Pressure", d.get("pressure", "N/A"))
            st.metric("👁 Visibility", d.get("visibility", "N/A"))

        st.info(f"☁️ **Condition:** {d.get('condition', 'N/A')}")

    else:
        st.error("❌ Error fetching current weather")

#3 dana forecasttt
st.divider()

if st.button("📅 3-Day Forecast", use_container_width=True):
    r = requests.get(f"{API}/weather/forecast", params={"city": city})

    if r.ok:
        st.subheader("📅 3-Day Weather Forecast")

        for day in r.json():
            with st.container(border=True):
                col1, col2 = st.columns([1, 2])
                with col1:
                    st.markdown(f"### {day['date']}")
                with col2:
                    st.markdown(
                        f"""
                        🌡 **{day['min_temp']}°C – {day['max_temp']}°C**  
                        ☁️ {day['condition']}
                        """
                    )
    else:
        st.error("❌ Error fetching forecast")

#historija
st.divider()

if st.button("📈 Weather History", use_container_width=True):
    r = requests.get(f"{API}/weather/history", params={"city": city})

    if r.ok:
        st.subheader("📈 Temperature History (3 Days)")
        st.image(r.json()["graph"], use_container_width=True)
    else:
        st.error("❌ Error loading weather history")

#footer
st.divider()
st.markdown(
    "<p style='text-align:center;color:gray;'>Made with ❤️ using FastAPI & Streamlit</p>",
    unsafe_allow_html=True
)
