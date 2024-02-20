import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
st.set_page_config(
    page_title="LB Scouting",
    page_icon="⚽️"
)

st.title("Main Page")

st.write('Here find the the first 3 steps in our sample scouting for a LB in the PSL')
st.subheader('Step 1: Identify top players')
st.write('Click on the Find tab to determine the top LBs by attacking and defensive quality')
st.subheader('Step 2: Understand the overall game of the top PSL LBs')
st.write('Click on the Compare tab to understand how your LB differs in quality and capabilities with top LBs at a more granular level')
st.subheader('Step 3: Summarise the information for referencing back')
st.write('Click on the Summarise tab to quickly see the overall atributes of the LBs identified')
st.subheader('Step 4: Delve deeper into understanding the exact nature and quality of players actions')
st.write("Here we show the exact actions and quality of each identified LB to examine every on ball action, contact us to take the next step in the scouting journey")

