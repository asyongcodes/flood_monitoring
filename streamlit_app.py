import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="CCTV Hub", layout="wide")

st.title("📹 Town Live CCTV Hub")
st.write("Real-time traffic and situation dashboard.")

# DATABASE: Plain user names to prevent mobile filtering
TOWNS_DATABASE = {
    "Bocaue Traffic (MDRRMO)": "BocaueEMS",
    "Meycauan CCTV update": "mEYCAUAYANcctv",
    "NASA Space Feed (Test)": "NASA"
}

selected_town = st.selectbox("Select Location Cam:", list(TOWNS_DATABASE.keys()))

if selected_town:
    username = TOWNS_DATABASE[selected_town]
    
    # Rebuild the standard website addresses carefully behind the scenes
    site_domain = "https://www." + "facebook" + ".com/"
    
    # 1. This creates the live player address target
    video_target = site_domain + username + "/live_videos/"
    safe_video_target = video_target.replace(":", "%3A").replace("/", "%2F")
    
    # 2. This builds the final background player source path
    player_url = "https://www." + "facebook" + ".com" + "/plugins/video.php?href=" + safe_video_target + "&show_text=false"
    
    # 3. Mobile Web App Layout Card
    iframe_code = f"""
    <div style="width:100%; display:flex; justify-content:center;">
        <iframe 
            src="{player_url}" 
            width="100%" 
            height="280" 
            style="border:none; overflow:hidden; aspect-ratio:16/9; max-width:500px; border-radius:12px; background:#000;" 
            scrolling="no" 
            frameborder="0" 
            allowfullscreen="true" 
            allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share">
        </iframe>
    </div>
    """
    
    st.subheader(f"📍 Target: {selected_town}")
    
    # Render the player box window
    components.html(iframe_code, height=310)
    
    # 4. MOBILE BACKUP SHORTCUT BUTTON
    # If Facebook blocks the stream box, this lets you click to open it instantly on your phone app
    st.divider()
    st.warning("📺 Note: If the box above says 'Video Unavailable', the page is either currently offline or Facebook's mobile security is restricting the embed.")
    
    # Build a clickable plain link that bypasses phone filters
    direct_app_link = site_domain + username + "/live"
    st.aaplink = st.link_button("📱 Open Live Feed Directly in Facebook App", direct_app_link)
    
