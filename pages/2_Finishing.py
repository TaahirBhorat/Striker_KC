import streamlit as st
import plotly.express as px
import pandas as pd

# Load your data
def main():
    st.title('PSL Strikers Analysis')

    df = pd.read_csv("data/Through_Balls_Received_Per_90_Updated.csv")

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

    # Filter for players with more than 400 minutes
    df_filtered = df[df['player_season_minutes'] > 400]

    # Calculate the difference between actual goals and expected goals
    df_filtered['Goals_minus_xG'] = df_filtered['player_season_goals_90'] - df_filtered['player_season_np_xg_90']

    # Create the Plotly scatter plot
    df_filtered['highlighted_names'] = df_filtered.apply(
    lambda row: row['player_name'] if row['player_name'] in ['Iqraam Rayners', 'Ashley Cupido'] else '', axis=1)

    fig = px.scatter(df_filtered, x='player_season_np_xg_90', y='player_season_goals_90',
                     text='highlighted_names', hover_data=['Goals_minus_xG', 'team_name'],
                     #labels={'player_season_np_xg_90': 'NP xG/90', 'player_season_goals_90': 'Goals/90'},
                     title='NP xG/90 vs Goals/90')

    # Adding mean lines
    mean_x = df_filtered['player_season_np_xg_90'].mean()
    mean_y = df_filtered['player_season_goals_90'].mean()
    fig.add_hline(y=mean_y, line_dash="dash", line_color="green")
    fig.add_vline(x=mean_x, line_dash="dash", line_color="red")

    # Adjusting layout for readability
    fig.update_traces(textposition='top center')
    fig.update_layout(showlegend=False)

    # Display the plot
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()