import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="CCTV Monitor Hub", layout="wide")

st.title("📹 Local Town CCTV Monitor Hub")
st.write("Real-time responsive video dashboard player.")

# DATABASE: Simple selections for the menu dropdown
TOWNS_DATABASE = [
    "NASA Space Station Live (YouTube Test)",
    "Bocaue Traffic Info Backup (Facebook App Link)"
]

selected_town = st.selectbox("Select Location Cam:", TOWNS_DATABASE)

if selected_town == "NASA Space Station Live (YouTube Test)":
    st.subheader("📍 Location: NASA Space Station Live")
    
    # HARDCODED PLAYER: Written directly with standard slashes. No dynamic variables!
    # This prevents the mobile phone text filter from combining the letters.
    youtube_iframe = """
    <div style="width:100%; display:flex; justify-content:center;">
        <iframe 
            width="100%" 
            height="280" 
            src="https://youtube.com" 
            style="max-width:500px; border-radius:12px; background:#000; border:none;" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen>
        </iframe>
    </div>
    """
    components.html(youtube_iframe, height=310)
    st.success("📺 Playing inline via static player canvas.")

elif selected_town == "Bocaue Traffic Info Backup (Facebook App Link)":
    st.subheader("📍 Location: Bocaue Traffic (MDRRMO)")
    st.error("🔒 Facebook blocks native inline mobile web streaming.")
    
    # Clean broken-up strings to protect your mobile app link launch
    domain_element = "https://www." + "facebook" + ".com/"
    direct_app_url = domain_element + "BocaueEMS" + "/live"
    
    st.info("Launch the live stream instantly inside your device's native app:")
    st.link_button("📱 Launch Live Feed inside Facebook App", direct_app_url)
    
