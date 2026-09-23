import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="CCTV Monitor", layout="wide")

st.title("📹 Local Town CCTV Hub")
st.write("Real-time video dashboard player module.")

# DATABASE: Keep your simple username handles here!
TOWNS_DATABASE = {
    "Bocaue Traffic (MDRRMO)": "BocaueEMS",
    "NASA Space Stream (Test)": "NASA"
}

selected_town = st.selectbox("Select Location Cam:", list(TOWNS_DATABASE.keys()))

if selected_town:
    username = TOWNS_DATABASE[selected_town]
    
    # 1. Safely construct the raw page path behind the scenes
    site_domain = "https://www." + "facebook" + ".com/"
    full_page_url = site_domain + username
    safe_page_url = full_page_url.replace(":", "%3A").replace("/", "%2F")
    
    # 2. Build the official video feed player plugin configuration
    player_url = "https://www." + "facebook" + ".com" + "/plugins/page.php?href=" + safe_page_url + "&tabs=timeline&width=500&height=400&small_header=true&adapt_container_width=true&hide_cover=true&show_facepile=false"
    
    # 3. ADVANCED INLINE CONTAINER:
    # This sandbox uses standard sandbox flags to block third-party app redirections 
    # and tricks the video container into inline execution.
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
            playsinline="true"
            webkit-playsinline="true"
            sandbox="allow-scripts allow-same-origin allow-presentation"
            allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share">
        </iframe>
    </div>
    """
    
    st.subheader(f"📍 Displaying: {selected_town}")
    
    # Inject the protected player window directly into your app layout
    components.html(iframe_code, height=420)
    
    # Mobile app quick-launch button backup
    st.divider()
    direct_app_url = site_domain + username + "/live"
    st.link_button("📱 Force Open Live Feed in Facebook App", direct_app_url)
    
