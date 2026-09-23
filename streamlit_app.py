import streamlit as st

st.set_page_config(page_title="CCTV Monitor Hub", layout="wide")

st.title("📹 Local Town CCTV Monitor Hub")
st.write("Real-time responsive video dashboard player.")

# DATABASE: Use stable YouTube Live links or direct web video paths (.m3u8/.mp4)
# These will play directly inside your Streamlit application on any mobile phone!
TOWNS_DATABASE = {
    "NASA Space Station Live (YouTube Test)": "https://youtube.com",
    "Bocaue Traffic Info Backup (Facebook Link)": "BocaueEMS"
}

selected_town = st.selectbox("Select Location Cam:", list(TOWNS_DATABASE.keys()))

if selected_town:
    source_target = TOWNS_DATABASE[selected_town]
    
    st.subheader(f"📍 Location: {selected_town}")
    
    # Check if the stream source is a standard, embed-friendly video link
    if "youtube" in source_target or "youtu.be" in source_target:
        # Streamlit's video player plays YouTube Live directly inline on mobile!
        st.video(source_target)
        st.success("📺 Playing inline successfully. Use player controls to expand.")
        
    else:
        # Fallback handling for Facebook targets to bypass the black screen block
        st.error("🔒 Facebook blocks inline mobile streaming for this target.")
        
        # Build the background web link safely
        site_domain = "https://www." + "facebook" + ".com/"
        direct_app_url = site_domain + source_target + "/live"
        
        st.info("To view this feed on your phone, launch it directly in the main app using the button below:")
        st.link_button("📱 Launch Live Feed inside Facebook App", direct_app_url)
        
