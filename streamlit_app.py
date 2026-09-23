import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="CCTV Monitor", layout="wide")

st.title("📹 Local Town CCTV Hub")
st.write("Real-time video dashboard player module.")

# DATABASE: Only type the short text names here. No web addresses!
TOWNS_DATABASE = {
    "Bocaue Traffic (MDRRMO)": "BocaueEMS",
    "NASA Space Stream (Test)": "NASA"
}

selected_town = st.selectbox("Select Location Cam:", list(TOWNS_DATABASE.keys()))

if selected_town:
    # 1. Isolate the target username (e.g., BocaueEMS)
    username = TOWNS_DATABASE[selected_town]
    
    # 2. Build the exact full page link safely behind the scenes
    site_domain = "https://www." + "facebook" + ".com/"
    full_page_url = site_domain + username
    
    # 3. Clean characters for the system player parameters
    safe_page_url = full_page_url.replace(":", "%3A").replace("/", "%2F")
    
    # 4. Use the official Facebook Page Plugin player instead of video player
    # This automatically shows their Live stream feed if they are online!
    player_url = "https://www." + "facebook" + ".com" + "/plugins/page.php?href=" + safe_page_url + "&tabs=timeline&width=500&height=400&small_header=true&adapt_container_width=true&hide_cover=true&show_facepile=false"
    
    # 5. Mobile Web App Layout Card
    iframe_code = f"""
    <div style="width:100%; display:flex; justify-content:center; align-items:center;">
        <iframe 
            src="{player_url}" 
            width="100%" 
            height="400" 
            style="border:none; overflow:hidden; width:500px; height:400px; border-radius:12px; background:#fff;" 
            scrolling="no" 
            frameborder="0" 
            allowfullscreen="true" 
            allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share">
        </iframe>
    </div>
    """
    
    st.subheader(f"📍 Displaying: {selected_town}")
    
    # Load player view directly onto the screen canvas
    components.html(iframe_code, height=420)
    
    # Mobile app quick-launch button backup
    st.divider()
    direct_app_url = site_domain + username + "/live"
    st.link_button("📱 Open Live Feed Directly in Facebook App", direct_app_url)
    
