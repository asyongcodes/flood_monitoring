import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="CCTV Hub", layout="wide")

st.title("📹 Town Live CCTV Monitor Hub")
st.write("Real-time traffic and situation dashboard.")

# DATABASE: Clean user handles to protect against phone text overrides
TOWNS_DATABASE = {
    "Bocaue Traffic (MDRRMO)": "BocaueEMS",
    "NASA Space Feed (Active Test)": "NASA"
}

selected_town = st.selectbox("Select Location Cam:", list(TOWNS_DATABASE.keys()))

if selected_town:
    username = TOWNS_DATABASE[selected_town]
    
    # Rebuild the standard website addresses carefully behind the scenes
    site_domain = "https://www." + "facebook" + ".com/"
    
    # Target the true fallback address format
    clean_target = site_domain + username + "/live_videos/"
    encoded_url = clean_target.replace(":", "%3A").replace("/", "%2F")
    
    # This architecture forces inline embedding to prevent player collapse
    iframe_code = f"""
    <div style="width:100%; display:flex; justify-content:center; align-items:center; background:#000; padding:10px; border-radius:12px;">
        <iframe 
            src="https://facebook.com{encoded_url}&show_text=false&v=v18.0" 
            width="100%" 
            height="280" 
            style="border:none; overflow:hidden; aspect-ratio:16/9; max-width:500px; border-radius:8px;" 
            scrolling="no" 
            frameborder="0" 
            allowfullscreen="true" 
            allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share">
        </iframe>
    </div>
    """
    
    st.subheader(f"📍 Target: {selected_town}")
    
    # Render the native component engine
    components.html(iframe_code, height=310)
    
    # Backup trigger button
    st.divider()
    direct_app_link = site_domain + username + "/live"
    st.link_button("📱 Open Live Feed Directly in Facebook App", direct_app_link)
    
