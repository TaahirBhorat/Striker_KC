import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import plotly.graph_objects as go
import plotly.express as px

####CONSTANTS
pitch_length=104
pitch_width=68



def create_soccer_pitch_with_boxes(pitch_length=104, pitch_width=68):
    """
    Create a soccer pitch layout with detailed markings (including boxes) using Plotly Express.
    """
    fig = px.line(x=[0, 0, pitch_length, pitch_length, 0], y=[0, pitch_width, pitch_width, 0, 0])

    # Left Penalty Area
    penalty_area_left_x = [0, 16.5, 16.5, 0, 0]
    penalty_area_left_y = [pitch_width / 2 + 22, pitch_width / 2 + 22, pitch_width / 2 - 22, pitch_width / 2 - 22, pitch_width / 2 + 22]
    fig.add_trace(px.line(x=penalty_area_left_x, y=penalty_area_left_y).data[0])

    # Right Penalty Area
    penalty_area_right_x = [pitch_length, pitch_length - 16.5, pitch_length - 16.5, pitch_length, pitch_length]
    fig.add_trace(px.line(x=penalty_area_right_x, y=penalty_area_left_y).data[0])

    # Left 6-yard Box
    six_yard_box_left_x = [0, 5.5, 5.5, 0, 0]
    six_yard_box_left_y = [pitch_width / 2 + 9.16, pitch_width / 2 + 9.16, pitch_width / 2 - 9.16, pitch_width / 2 - 9.16, pitch_width / 2 + 9.16]
    fig.add_trace(px.line(x=six_yard_box_left_x, y=six_yard_box_left_y).data[0])

    # Right 6-yard Box
    six_yard_box_right_x = [pitch_length, pitch_length - 5.5, pitch_length - 5.5, pitch_length, pitch_length]
    fig.add_trace(px.line(x=six_yard_box_right_x, y=six_yard_box_left_y).data[0])

    # Halfway Line
    halfway_line_x = [pitch_length / 2, pitch_length / 2]
    halfway_line_y = [0, pitch_width]
    fig.add_trace(px.line(x=halfway_line_x, y=halfway_line_y).data[0])

    # Update layout
    fig.update_layout(
        xaxis=dict(
            range=[0, pitch_length],
            visible=False
        ),
        yaxis=dict(
            range=[0, pitch_width],
            visible=False
        ),
        showlegend=False
    )

    return fig

# data = pd.read_csv('data\South Africa_PSL_2324.csv', low_memory=False)
# xg_data = pd.read_csv('Pages\sbpslevents.csv', low_memory=False)


st.title('PSL 23/24 OP Shot Maps')
#player_choices = data['player_name'].unique()
player_choices = ["Iqraam Rayners", 'Ashley Cupido']

body_part_symbols = {
    'Right Foot': 'circle',
    'Left Foot': 'square',
    'Head': 'triangle-up',
    'Other': 'cross'
}


player_name1 = st.selectbox("Select a Player", player_choices, index=0, key=1, disabled=True)    
# shots_df1 = data[(data['player_name']==player_name1) & (data['type_name'] == 'shot')][['original_event_id','game_id','player_name','start_x','start_y']]
# shots_df1.reset_index(inplace=True, drop=True)
# xg_vals1 = xg_data[(xg_data['type']=='Shot') & (xg_data['player']==player_name1) & (xg_data['shot_type']=='Open Play')][['match_id','id','player','shot_statsbomb_xg','shot_body_part','shot_outcome']]
# xg_vals1.reset_index(inplace=True, drop=True)
# plot_data1 = pd.merge(shots_df1, xg_vals1, left_on='original_event_id', right_on='id', how='inner')
plot_data1 = pd.read_csv("data/iqraamshots.csv")
### FIRST PLOT

fig1 = create_soccer_pitch_with_boxes()

# Add trace for shots
fig1.add_trace(go.Scatter(
    x=plot_data1['start_x'], 
    y=plot_data1['start_y'],
    mode='markers', 
    marker=dict(
        color=plot_data1['shot_statsbomb_xg'], 
        colorscale='Viridis',
        showscale=True,
        cmin=0,
        cmax=0.42,
        colorbar=dict(thickness=5, tickvals=[0, 0.42], ticktext=['Low xG', 'High xG'], outlinewidth=0),
        size=10,
        symbol=[body_part_symbols[bp] for bp in plot_data1['shot_body_part']]  # Mapping symbols based on shot_body_part
    ),
    name='Shots',
    text=[f'xG: {xg:.2f}<br>Body Part: {bp}<br>Shot outcome: {so}' for xg, bp, so in zip(plot_data1['shot_statsbomb_xg'], plot_data1['shot_body_part'],plot_data1['shot_outcome'])],  # Customized hover text
    hoverinfo='text',  # Display text, x, and y on hover
))
fig1.update_layout(plot_bgcolor='lightgrey')

st.plotly_chart(fig1)

### SECOND PLOT

player_name2 = st.selectbox("Select a Player", player_choices, index=1, key=2, disabled=True)    
# shots_df2 = data[(data['player_name']==player_name2) & (data['type_name'] == 'shot')][['original_event_id','game_id','player_name','start_x','start_y']]
# shots_df2.reset_index(inplace=True, drop=True)
# xg_vals2 = xg_data[(xg_data['type']=='Shot') & (xg_data['player']==player_name2) & (xg_data['shot_type']=='Open Play')][['match_id','id','player','shot_statsbomb_xg','shot_body_part','shot_outcome']]
# xg_vals2.reset_index(inplace=True, drop=True)
# plot_data2 = pd.merge(shots_df2, xg_vals2, left_on='original_event_id', right_on='id', how='inner')
plot_data2 = pd.read_csv("data/ashleyshots.csv")

fig2 = create_soccer_pitch_with_boxes()

# Add trace for shots
fig2.add_trace(go.Scatter(
    x=plot_data2['start_x'], 
    y=plot_data2['start_y'],
    mode='markers', 
    marker=dict(
        color=plot_data2['shot_statsbomb_xg'], 
        colorscale='Viridis',
        showscale=True,
        cmin=0,
        cmax=0.42,
        colorbar=dict(thickness=5, tickvals=[0, 0.42], ticktext=['Low xG', 'High xG'], outlinewidth=0),
        size=10,
        symbol=[body_part_symbols[bp] for bp in plot_data2['shot_body_part']]
    ),
    name='Shots',
    text=[f'xG: {xg:.2f}<br>Body Part: {bp}<br>Shot outcome: {so}' for xg, bp, so in zip(plot_data2['shot_statsbomb_xg'], plot_data2['shot_body_part'],plot_data2['shot_outcome'])],  # Customized hover text
    hoverinfo='text',  # Display text, x, and y on hover
))
fig2.update_layout(plot_bgcolor='lightgrey')
st.plotly_chart(fig2)

