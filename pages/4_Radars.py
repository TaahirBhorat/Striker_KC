import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from matplotlib import cm
from matplotlib.colors import to_hex



# Display the image and text above the sidebar
st.sidebar.markdown(
    """
    <div style='text-align: center; margin-top: -10px;'>
        <h2 style='margin-bottom: 0;'>xBall</h2>
    </div>
    """,
    unsafe_allow_html=True
)
# Load your data
file_path = 'data/Through_Balls_Received_Per_90_Updated.csv'
df = pd.read_csv(file_path, sep=",")
def map_filter_rank(df, min_90s_played):
    # Define the mapping dictionary
    position_map = {
        'Center Forward': 'CF',
        'Left Wing': 'LW',
        'Right Wing': 'RW',
        'Left Back': 'LB',
        'Right Back': 'RB',
        'Center Midfield': 'M',
        'Left Midfield': 'LW',
        'Left Midfielder': 'LW',
        'Right Midfield': 'RW',
        'Right Midfielder': 'RW',
        'Defensive Midfielder': 'DM',
        'Attacking Midfielder': 'M',
        'Center Back': 'CB',
        'Goalkeeper': 'GK',
        'Left Centre Back': 'CB',
        'Right Centre Back': 'CB',
        'Left Defensive Midfielder': 'DM',
        'Right Defensive Midfielder': 'DM',
        'Centre Attacking Midfielder': 'M',
        'Centre Defensive Midfielder': 'DM',
        'Left Wing Back': 'LW',
        'Right Wing Back': 'RW',
        'Right Forward': 'RW',
        'Left Forward': 'LW',
        'Centre Forward': 'CF',
        'Left Centre Midfielder': 'M',
        'Left Centre Forward': 'CF',
        'Right Centre Forward': 'CF',
        'Right Centre Midfielder': 'M',
        'Left Attacking Midfielder': 'M',
        'Right Attacking Midfielder': 'M'
    }

    # Map the primary_position to position
    df['position'] = df['primary_position'].map(position_map)
    df = df[df['position']=="CF"]
    df = df[df['player_season_90s_played']>7]

selected_cols = ['player_season_np_xg_per_shot', 'player_season_np_xg_90', 'player_season_np_shots_90', 'player_season_goals_90','player_season_obv_pass_90', 'player_season_op_xa_90', 
                 'player_season_op_key_passes_90','player_season_touches_inside_box_90', 'player_season_obv_dribble_carry_90','player_season_turnovers_90', 'player_season_padj_pressures_90', 
                 'player_season_aerial_wins_90', 'player_season_counterpressure_regains_90', 'through balls received per 90', 'player_name']

df = df[selected_cols]
# Updating column names by removing 'player_season_' prefix


df.columns = [col.replace('player_season_', '') for col in df.columns]

# Define categories and their colors
categories = {
    'Finishing': ['np_xg_per_shot', 'np_xg_90', 'np_shots_90', 'goals_90'],
    'Passing': ['obv_pass_90', 'op_xa_90', 'op_key_passes_90'],
    'Dribbling': ['touches_inside_box_90', 'obv_dribble_carry_90'],
    'Off_ball': ['turnovers_90', 'padj_pressures_90', 'aerial_wins_90', 'counterpressure_regains_90', 'through balls received per 90']
}
category_colors = {'Finishing': 'skyblue', 'Passing': 'forestgreen', 'Dribbling': 'chocolate', 'Off_ball': 'purple'}

# Create a list of all columns in the DataFrame that are not in any category
other_columns = [col for col in df.columns if all(col not in attrs for attrs in categories.values())]

# Flatten categories into a single list of columns in the desired order
ordered_columns = [col for group in categories.values() for col in group]

# Ensure that all columns in 'ordered_columns' exist in 'df' to avoid KeyErrors
ordered_columns = [col for col in ordered_columns if col in df.columns]

# Reorder columns within categories and keep other columns
df_ordered = df[ordered_columns + other_columns]

# Calculate mean and standard deviation for each attribute
attributes_mean = df_ordered.mean(numeric_only=True)
attributes_std = df_ordered.std(numeric_only=True)

# Define a fixed set of 15 distinct colors
distinct_colors = [
    '#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF', '#00FFFF',
    '#800000', '#008000', '#000080', '#808000', '#800080', '#008080',
    '#C0C0C0', '#808080', '#FF8080'
]

# Apply CSS to expand the plot container to full width
st.markdown(
    """
    <style>
    .reportview-container .main .block-container{
        padding-left: 1rem;
        padding-right: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit app
def main():
    st.title("Player Performance Comparison")
    st.subheader("PSL Strikers")

    # Input for selecting multiple players, limit to 15 players
    # options=df_ordered['player_name'].unique()
    selected_players = st.multiselect('Select up to 15 players to highlight',options = ['Ashley Cupido', 'Iqraam Rayners'] , max_selections=15)

    # Assign colors to selected players
    player_colors = {player: distinct_colors[i] for i, player in enumerate(selected_players)}

    # Creating a Plotly figure
    fig = go.Figure()

    # Plotting each player
    for player in df_ordered['player_name'].unique():
        if player not in selected_players:  # Skip highlighted players
            player_data = df_ordered[df_ordered['player_name'] == player].select_dtypes(include=np.number)
            std_from_mean = (player_data.iloc[0] - attributes_mean) / attributes_std

            # Adding a scatter trace for each player with showlegend=False
            fig.add_trace(go.Scatter(x=std_from_mean.values, y=std_from_mean.index,
                                     mode='markers', marker=dict(color='grey', size=10),
                                     name="player", text=[player]*len(std_from_mean),
                                     hoverinfo='text', showlegend=False))

    # Highlighting specific players
    for player in selected_players:
        player_data = df_ordered[df_ordered['player_name'] == player].select_dtypes(include=np.number)
        std_from_mean = (player_data.iloc[0] - attributes_mean) / attributes_std

        # Adding a scatter trace for highlighted players
        fig.add_trace(go.Scatter(x=std_from_mean.values, y=std_from_mean.index,
                                 mode='markers', marker=dict(color=player_colors[player], size=15),
                                 name=player, text=[player]*len(std_from_mean),
                                 hoverinfo='text'))

    # Adding average line
    fig.add_shape(type="line", x0=0, y0=-1, x1=0, y1=len(attributes_mean),
                  line=dict(color="white", width=2, dash="dash"))

    # Setting layout properties
    fig.update_layout(title="Player Performance Comparison",
                      xaxis_title="Standard Deviation from Mean",
                      yaxis=dict(tickmode='array', tickvals=list(range(len(attributes_mean))), ticktext=attributes_mean.index),
                      autosize=True,
                      margin=dict(l=50, r=50, t=100, b=50),
                      height=800,
                      width=2000)  # Increase width to ensure full-width display

    # Adding category annotations
    y_positions = {attr: idx for idx, attr in enumerate(attributes_mean.index)}
    for category, attrs in categories.items():
        for attr in attrs:
            if attr in y_positions:
                fig.add_annotation(x=-9, y=y_positions[attr],  # Adjust x-coordinate for left alignment
                                   text=category,
                                   showarrow=False,
                                   xanchor='left',  # Anchor text to the left
                                   align='left',
                                   font=dict(color=category_colors[category]))

    # Display the plot in Streamlit
    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
