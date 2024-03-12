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

st.write('Here find the first 3 steps in our sample scouting for a striker in the PSL with a focus on comparing Iqraam Rayners to Ashley Du Preez')
st.write("Click through the tabs to explore how to compare/scout with respect to: finishing, pressing, off-ball movement and on-ball contributions")

