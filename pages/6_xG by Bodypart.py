import streamlit as st
pic1 = "data/pics/bodypart_2223.png"
pic2 = "data/pics/bodypart_2324.png"

st.markdown("<h1 style='text-align: center;'>xG by Bodypart</h1>", unsafe_allow_html=True)


col1, col2 = st.columns(2)
with col1:
    st.image(pic1, caption='xG by bodypart - PSL 2022/2023')
    
# Add Ashley Du Preez images to the second column
with col2:
    st.image(pic2, caption='xG by bodypart - PSL 2023/2024')
    
