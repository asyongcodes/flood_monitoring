import streamlit as st

# 1. Set up the web application page configuration
st.set_page_config(
    page_title="Town CCTV Monitor Hub", 
    page_icon="📹", 
    layout="wide"
)

st.title("📹 Town Live CCTV Monitor Hub")
st.write("Real-time local situation dashboard sourced from Facebook Live pages.")

# 2. Database of your tracked towns 
# Replace the URLs below with the actual Facebook live links of your target pages.
TOWNS_DATABASE = {
    "Town A (BOCAUE)": "https://www.facebook.com/share/v/1JFnziSGSj/",
    "Town B (MARILAO)": "https://www.facebook.com/share/v/18Fz8cJMNp/",
    "Town C (MEYCAUAN)": "https://www.facebook.com/share/v/1BeUxaGnUU/",
    "Town D (VALENZUELA)": "https://www.facebook.com/share/v/1BoCccfAoR/"
}

# 3. Sidebar interface for easy control on mobile devices
st.sidebar.header("Dashboard Configuration")
view_mode = st.sidebar.radio("Display Mode", ["Grid View (All Feed)", "Single Town View"])

# Helper function to construct a Facebook Responsive Iframe
def get_facebook_iframe(video_url):
    # Encodes the URL automatically so Facebook can read it inside the iframe plug-in
    encoded_url = video_url.replace(":", "%3A").replace("/", "%2F")
    
    iframe_code = f"""
    <iframe 
        src="https://facebook.com{encoded_url}&show_text=false&width=560" 
        width="100%" 
        height="315" 
        style="border:none; overflow:hidden; border-radius:10px; aspect-ratio: 16/9;" 
        scrolling="no" 
        frameborder="0" 
        allowfullscreen="true" 
        allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share">
    </iframe>
    """
    return iframe_code

# 4. Rendering Logic
if view_mode == "Grid View (All Feed)":
    # Creates a responsive multi-column grid layout
    # On desktop it shows columns, on mobile Streamlit stacks them vertically automatically
    cols = st.columns(2) 
    
    for index, (town_name, fb_url) in enumerate(TOWNS_DATABASE.items()):
        # Alternate items between column 0 and column 1
        with cols[index % 2]:
            st.subheader(town_name)
            # Embed the HTML code using Streamlit's HTML component
            st.components.v1.html(get_facebook_iframe(fb_url), height=320)
            st.divider()

elif view_mode == "Single Town View":
    # Let the user pick one specific town from a drop-down menu (ideal for slower mobile networks)
    selected_town = st.sidebar.selectbox("Select Town Cam", list(TOWNS_DATABASE.keys()))
    
    st.header(f"📍 Currently Monitoring: {selected_town}")
    fb_url = TOWNS_DATABASE[selected_town]
    st.components.v1.html(get_facebook_iframe(fb_url), height=450)
  
