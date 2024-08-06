import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# [Include your functions csdasdalculate_heatmap_frequencies, create_soccer_pitch_with_boxes, plot_heatmap_with_pitch here]
def calculate_heatmap_frequencies(data, grid_size_x, grid_size_y, pitch_length=104, pitch_width=68):
    """
    Calculate the frequencies for the heatmap.
    """
    heatmap = np.zeros((grid_size_y, grid_size_x))
    cell_size_x = pitch_length / grid_size_x
    cell_size_y = pitch_width / grid_size_y

    for _, row in data.iterrows():
        cell_x = min(int(row['spad_x'] // cell_size_x), grid_size_x - 1)
        cell_y = min(int(row['spad_y'] // cell_size_y), grid_size_y - 1)
        heatmap[cell_y, cell_x] += 1

    return heatmap

def create_soccer_pitch_with_boxes(ax, pitch_length=104, pitch_width=68):
    """
    Create a soccer pitch layout with detailed markings (including boxes) on the given Matplotlib axis.
    """
    # Pitch Outline & Centre Line
    ax.plot([0, 0], [0, pitch_width], color="black") # Left sideline
    ax.plot([0, pitch_length], [pitch_width, pitch_width], color="black") # Top goal line
    ax.plot([pitch_length, pitch_length], [pitch_width, 0], color="black") # Right sideline
    ax.plot([pitch_length, 0], [0, 0], color="black") # Bottom goal line
    ax.plot([pitch_length / 2, pitch_length / 2], [0, pitch_width], color="black") # Halfway line

    # Left Penalty Area
    penalty_area_left_x = 16.5
    penalty_area_left_y = 22
    ax.plot([0, penalty_area_left_x], [pitch_width / 2 + penalty_area_left_y, pitch_width / 2 + penalty_area_left_y], color="black") # Top line
    ax.plot([penalty_area_left_x, penalty_area_left_x], [pitch_width / 2 + penalty_area_left_y, pitch_width / 2 - penalty_area_left_y], color="black") # Right line
    ax.plot([penalty_area_left_x, 0], [pitch_width / 2 - penalty_area_left_y, pitch_width / 2 - penalty_area_left_y], color="black") # Bottom line

    # Right Penalty Area
    penalty_area_right_x = pitch_length - 16.5
    ax.plot([pitch_length, penalty_area_right_x], [pitch_width / 2 + penalty_area_left_y, pitch_width / 2 + penalty_area_left_y], color="black") # Top line
    ax.plot([penalty_area_right_x, penalty_area_right_x], [pitch_width / 2 + penalty_area_left_y, pitch_width / 2 - penalty_area_left_y], color="black") # Left line
    ax.plot([penalty_area_right_x, pitch_length], [pitch_width / 2 - penalty_area_left_y, pitch_width / 2 - penalty_area_left_y], color="black") # Bottom line

    # Left 6-yard Box
    six_yard_box_left_x = 5.5
    six_yard_box_left_y = 9.16
    ax.plot([0, six_yard_box_left_x], [pitch_width / 2 + six_yard_box_left_y, pitch_width / 2 + six_yard_box_left_y], color="black") # Top line
    ax.plot([six_yard_box_left_x, six_yard_box_left_x], [pitch_width / 2 + six_yard_box_left_y, pitch_width / 2 - six_yard_box_left_y], color="black") # Right line
    ax.plot([six_yard_box_left_x, 0], [pitch_width / 2 - six_yard_box_left_y, pitch_width / 2 - six_yard_box_left_y], color="black") # Bottom line

    # Right 6-yard Box
    six_yard_box_right_x = pitch_length - 5.5
    ax.plot([pitch_length, six_yard_box_right_x], [pitch_width / 2 + six_yard_box_left_y, pitch_width / 2 + six_yard_box_left_y], color="black") # Top line
    ax.plot([six_yard_box_right_x, six_yard_box_right_x], [pitch_width / 2 + six_yard_box_left_y, pitch_width / 2 - six_yard_box_left_y], color="black") # Left line
    ax.plot([six_yard_box_right_x, pitch_length], [pitch_width / 2 - six_yard_box_left_y, pitch_width / 2 - six_yard_box_left_y], color="black") # Bottom line

    return ax

def plot_heatmap_with_pitch(heatmap, title, grid_size_x, grid_size_y, pitch_length=104, pitch_width=68):
    """
    Plot the heatmap with soccer pitch markings.
    """
    fig, ax = plt.subplots(figsize=(30, 20))
    ax = create_soccer_pitch_with_boxes(ax, pitch_length, pitch_width)

    # Rescale the heatmap to the size of the pitch
    heatmap_rescaled = np.zeros((grid_size_y, grid_size_x))
    for i in range(grid_size_y):
        for j in range(grid_size_x):
            heatmap_rescaled[i, j] = heatmap[int(i * heatmap.shape[0] / grid_size_y), int(j * heatmap.shape[1] / grid_size_x)]


    # Plot the heatmapasdasd
    
    ax.imshow(np.flipud(heatmap_rescaled), extent=(0, pitch_length, 0, pitch_width), interpolation='nearest', cmap='viridis', alpha=0.8)
    ax.set_title(title)
    ax.set_xlabel('Pitch Length')
    ax.set_ylabel('Pitch Width')
    return fig 
# Load your data
#@st.cache_data
#def load_data():
#    return pd.read_csv('data/Fynspadnew.csv')  

#data = load_data()
data = pd.read_csv('data/Fynspadfin.csv')  
# Streamlit UI
st.title('Player Defensive Actions Heatmap')

# Player selection
player_names = data['player'].unique()
player1_name = st.selectbox('Select Player 1:', player_names)
player2_name = st.selectbox('Select Player 2:', player_names)
successful_tackle_indicators = ["Success In Play","Won","Success Out"] 
successful_interception_indicators = ["Success In Play","Won","Success Out"] 

# Filter data and plot heatmaps for selected players
for player_name in [player1_name, player2_name]:
    # Filter for the selected player and defensive actions
    defensive_actions = data[
        (data['player'] == player_name) &
        ((data['type'] == 'Duel') & (data['duel_outcome'].isin(successful_tackle_indicators)) |
        (data['type'] == 'Interception') & (data['interception_outcome'].isin(successful_interception_indicators)) |
        (data['type'] == 'Pressure')) &
        (data['spad_x'].notnull()) & (data['spad_y'].notnull())
    ]

    # Calculate heatmap frequencies
    heatmap_defensive_actions = calculate_heatmap_frequencies(defensive_actions, 16, 11)

    # Plot heatmap with pitch
    plt_defensive_actions = plot_heatmap_with_pitch(heatmap_defensive_actions, f'{player_name} Defensive Actions Heatmap', 16, 11)

    # Display the plot in Streamlit
    st.pyplot(plt_defensive_actions)
