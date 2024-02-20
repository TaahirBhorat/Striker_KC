import streamlit as st
iqraam_2023_2024_path = "data/pics/Iqraam Rayners PSL 2023_2024.png"
iqraam_2022_2023_path = "data/pics/Iqraam Rayners PSL 2022_2023.png"
ashley_2023_2024_path = "data/pics/Ashley Du Preez PSL 2023_2024.png"
ashley_2022_2023_path = "data/pics/Ashley Du Preez PSL 2022_2023.png"

# Display the images in two columns

# Add Iqraam Rayners images to the first column
st.markdown("<h1 style='text-align: center;'>Ball receipts heatmaps</h1>", unsafe_allow_html=True)


col1, col2 = st.columns(2)
with col1:
    st.image(iqraam_2023_2024_path, caption='Iqraam Rayners - PSL 2023/2024')
    st.image(iqraam_2022_2023_path, caption='Iqraam Rayners - PSL 2022/2023')

# Add Ashley Du Preez images to the second column
with col2:
    st.image(ashley_2023_2024_path, caption='Ashley Du Preez - PSL 2023/2024')
    st.image(ashley_2022_2023_path, caption='Ashley Du Preez - PSL 2022/2023')

