import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="CCTV Monitor Hub", layout="wide")

st.title("📹 Local Town CCTV Monitor Hub")
st.write("Real-time responsive video dashboard player.")

# DATABASE: We use the universal YouTube embed IDs here. 
# For example, in a YouTube link, the text after "v=" is the clean video ID.
TOWNS_DATABASE = {
    "NASA Space Station Live (YouTube Test)": "jPTD2gnZwgE",
    "Bocaue Traffic Info Backup (Facebook)": "BocaueEMS"
}

selected_town = st.selectbox("Select Location Cam:", list(TOWNS_DATABASE.keys()))

if selected_town:
    source_target = TOWNS_DATABASE[selected_town]
    
    st.subheader(f"📍 Location: {selected_town}")
    
    # Check if the target is our YouTube video ID
    if source_target == "jPTD2gnZwgE":
        # Universal HTML5 YouTube Player (Bypasses mobile browser cookie blockers)
        youtube_iframe = f"""
        <div style="width:100%; display:flex; justify-content:center;">
            <iframe 
                width="100%" 
                height="280" 
                src="https://youtube.com{source_target}?rel=0&playsinline=1" 
                style="max-width:500px; border-radius:12px; background:#000; border:none;" 
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                allowfullscreen>
            </iframe>
        </div>
        """
        components.html(youtube_iframe, height=310)
        st.success("📺 Playing via universal mobile player layout.")
        
    else:
        # Fallback handling for Facebook targets to bypass the black screen block
        st.error("🔒 Facebook blocks inline mobile streaming for this target.")
        
        # Build the background web link safely
        site_domain = "https://www." + "facebook" + ".com/"
        direct_app_url = site_domain + source_target + "/live"
        
        st.info("To view this feed on your phone, launch it directly in the main app using the button below:")
        st.link_button("📱 Launch Live Feed inside Facebook App", direct_app_url)
        
