import streamlit as st

st.header('🎈 Welcome to the Celebration App! 🎈')

if st.button('🎉 Celebrate!'):
    st.balloons()
    st.snow()
    st.toast('Party time!', icon='🎊')