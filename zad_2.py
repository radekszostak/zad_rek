import streamlit as st
import leafmap.foliumap as leafmap
from geopy.geocoders import Nominatim
if "geolocator" not in st.session_state:
    st.session_state.geolocator = Nominatim(user_agent="streamlit-map")
if "map" not in st.session_state:
    st.session_state.map = leafmap.Map(
        draw_control=False,
        measure_control=False,
        fullscreen_control=False,
        attribution_control=False,
    )
    
st.title("City Map")
st.markdown("Get any city location providing its name")
col1, col2 = st.columns(2)
with col1:
    address = st.text_input('City', 'Kraków', label_visibility="collapsed")
with col2:
    confirm = st.button("Apply")
if address or confirm:
    location = st.session_state.geolocator.geocode(address)
    if location:
        st.session_state.map.set_center(location.longitude, location.latitude, zoom=12)
    else:
        st.warning('Location not found', icon="⚠️")
    st.session_state.map.to_streamlit()

