import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Town CCTV Hub", layout="wide")

st.title("📹 Town Live CCTV Monitor Hub")
st.write("Real-time local situation dashboard.")

# 1. DATABASE: Type ONLY the page usernames here!
# This completely prevents your phone from filtering the text.
TOWNS_DATABASE = {
    "Bocaue Traffic Update (MDRRMO)": "BocaueEMS",
    "NASA Live Channel (Test)": "NASA"
}

selected_town = st.selectbox("Choose a Town to View:", list(TOWNS_DATABASE.keys()))

if selected_town:
    # Extract just the raw username (for example: BocaueEMS)
    username = TOWNS_DATABASE[selected_town]
    
    # The code automatically glues the web elements together in the background
    full_web_url = "https://facebook.com" + username + "/live_videos/"
    
    # Convert symbols to an embed-safe format
    encoded_url = full_web_url.replace(":", "%3A").replace("/", "%2F")
    
    # Secure Facebook player container
    iframe_code = f"""
    <div style="width:100%; display:flex; justify-content:center;">
        <iframe 
            src="https://facebook.com/plugins/video.php?href={encoded_url}&show_text=false&width=500" 
            width="100%" 
            height="314" 
            style="border:none; overflow:hidden; aspect-ratio:16/9; max-width:500px; border-radius:12px; background:#000;" 
            scrolling="no" 
            frameborder="0" 
            allowfullscreen="true" 
            allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share">
        </iframe>
    </div>
    """
    
    st.subheader(f"📍 Currently Monitoring: {selected_town}")
    st.caption(f"Connected to Facebook Username: {username}")
    
    # Project the player frame onto the Streamlit interface
    components.html(iframe_code, height=350)
    
