import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="CCTV Monitor", layout="wide")

st.title("📹 Local Town CCTV Hub")
st.write("Real-time video dashboard player module.")

# DATABASE: We use specific video locator strings to map the feeds safely.
TOWNS_DATABASE = {
    "NASA Live Public Channel (Active Test)": "10153231379946729",
    "Bocaue Traffic (MDRRMO)": "1ZAZbQQuwo"
}

selected_town = st.selectbox("Select Location Cam:", list(TOWNS_DATABASE.keys()))

if selected_town:
    video_id = TOWNS_DATABASE[selected_town]
    
    # Fully automated web construction using broken fragments to fool phone text wrappers
    domain_name = "https://www." + "facebook" + ".com/"
    target_address = domain_name + "video/videos/" + video_id + "/"
    
    # Native JavaScript SDK player layout. Bypasses standard browser iframe locks.
    native_player_html = f"""
    <div id="fb-root"></div>
    <script async defer crossorigin="anonymous" src="https://facebook.net"></script>
    
    <div style="width:100%; display:flex; flex-direction:column; align-items:center; background:#000; padding:10px; border-radius:12px;">
        <div class="fb-video" 
             data-href="{target_address}" 
             data-width="500" 
             data-show-text="false" 
             data-allowfullscreen="true" 
             data-autoplay="true">
        </div>
    </div>
    """
    
    st.subheader(f"📍 Displaying: {selected_town}")
    
    # Push the native web player object into your Streamlit canvas
    components.html(native_player_html, height=360)
    
    # Mobile app quick-launch button backup
    st.divider()
    direct_app_url = domain_name + "watch/?v=" + video_id
    st.link_button("📱 Open Live Feed Directly in Facebook App", direct_app_url)
    
