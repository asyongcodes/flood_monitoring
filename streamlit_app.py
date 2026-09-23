import streamlit as st
from streamlit_player import st_player

st.set_page_config(page_title="CCTV Monitor Hub", layout="wide")

st.title("📹 Local Town CCTV Hub")
st.write("Stream directly within the web app canvas.")

# DATABASE: Clean user handles to protect against phone text overrides
TOWNS_DATABASE = {
    "Bocaue Traffic (MDRRMO)": "BocaueEMS",
    "NASA Space Feed (Active Test)": "NASA"
}

selected_town = st.selectbox("Select Location Cam:", list(TOWNS_DATABASE.keys()))

if selected_town:
    username = TOWNS_DATABASE[selected_town]
    
    # 1. Rebuild the destination address using broken segments
    web_domain = "https://www." + "facebook" + ".com/"
    stream_source_url = web_domain + username + "/live"
    
    st.subheader(f"📍 Feed Layer: {selected_town}")
    
    # 2. Advanced Player Core Engine Execution
    # This component captures the underlying stream assets and renders them 
    # directly on the app canvas, bypassing Facebook's native app redirects.
    try:
        st_player(
            url=stream_source_url,
            height=300,
            playback_rate=1.0,
            muted=True
        )
    except Exception as e:
        st.error("Streaming container initialization encountered an issue loading this source.")

    # Mobile app quick-launch button backup
    st.divider()
    st.caption(f"Source Connection Path: {stream_source_url}")
    st.link_button("📱 Force Open Live Feed in Facebook App", stream_source_url)
    
