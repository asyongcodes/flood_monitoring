import streamlit as st

st.set_page_config(page_title="CCTV Monitor Hub", layout="wide")

st.title("📹 Local Town CCTV Monitor Hub")
st.write("Mobile-optimized situational dashboard control panel.")

st.info("💡 Tip: Because mobile browsers block video embeds inside cloud apps, tap the buttons below to open live streams instantly in their official applications.")

# Create clean sections for organization
st.header("📍 Available Live Feeds")

# Layout Column 1 - Bulacan Local Feeds
with st.container():
    st.subheader("Bocaue Traffic Updates (MDRRMO)")
    st.write("Real-time main road condition streaming feeds.")
    
    # Fragment assembly to safely bypass mobile browser text wrappers
    fb_root = "https://www." + "facebook" + ".com/"
    bocaue_app_url = fb_root + "BocaueEMS" + "/live"
    
    st.link_button("📱 Launch Bocaue Stream on Facebook", bocaue_app_url, use_container_width=True)

st.divider()

# Layout Column 2 - Operational Test Channels
with st.container():
    st.subheader("NASA Space Feed (Dashboard Test)")
    st.write("Global reference live broadcast testing pipeline channel.")
    
    nasa_youtube_url = "https://youtube.com"
    
    st.link_button("📺 Open NASA Live on YouTube", nasa_youtube_url, use_container_width=True)

st.divider()

# How to expand section
with st.expander("➕ How to add more towns from your phone"):
    st.write("1. Open your `app.py` file on GitHub.")
    st.write("2. Copy an existing `with st.container():` block section.")
    st.write("3. Change the text title and swap out the username handle.")
    
