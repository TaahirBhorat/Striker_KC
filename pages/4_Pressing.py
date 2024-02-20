from statsbombpy import sb
#from sklearn.preprocessing import StandardScaler
import pandas as pd
import plotly.express as px
import numpy as np
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go
import matplotlib.pyplot as plt


# creds ...


# def getSeasonStats(country, league, season, min_mins_played):
#     # league = 'PSL'
#     # country = 'South Africa'
#     # season = "2023/2024"

#     filtered_comps = sb.competitions(creds=creds)
#     psl_comps = filtered_comps[(filtered_comps['competition_name'] == league) & (filtered_comps['country_name'] == country)]

#     index = psl_comps.index[psl_comps['season_name'] == season][0]

#     comp_id = psl_comps.loc[index]['competition_id']
#     season_id = psl_comps.loc[index]['season_id']

#     player_season = sb.player_season_stats(competition_id=comp_id, season_id=season_id, creds=creds)

#     remove_all = """account_id player_id team_id competition_id player_season_360_minutes season_id season_name country_id birth_date player_female player_first_name player_last_name player_known_name player_weight player_height player_season_minutes secondary_position player_season_shots_faced_90 player_season_goals_faced_90 player_season_np_xg_faced_90 player_season_np_psxg_faced_90 player_season_save_ratio player_season_xs_ratio player_season_gsaa_90 player_season_gsaa_ratio player_season_ot_shots_faced_90 player_season_npot_psxg_faced_90 player_season_ot_shots_faced_ratio player_season_np_optimal_gk_dlength player_season_clcaa player_season_most_recent_match player_season_average_space_received_in player_season_average_fhalf_space_received_in player_season_average_f3_space_received_in player_season_ball_receipts_in_space_10_ratio player_season_ball_receipts_in_space_2_ratio player_season_ball_receipts_in_space_5_ratio player_season_fhalf_ball_receipts_in_space_10_ratio player_season_fhalf_ball_receipts_in_space_2_ratio player_season_fhalf_ball_receipts_in_space_5_ratio player_season_f3_ball_receipts_in_space_10_ratio player_season_f3_ball_receipts_in_space_2_ratio player_season_f3_ball_receipts_in_space_5_ratio player_season_lbp_90 player_season_lbp_completed_90 player_season_lbp_ratio player_season_fhalf_lbp_completed_90 player_season_fhalf_lbp_ratio player_season_f3_lbp_completed_90 player_season_f3_lbp_ratio player_season_fhalf_lbp_90 player_season_f3_lbp_90 player_season_obv_lbp_90 player_season_fhalf_obv_lbp_90 player_season_f3_obv_lbp_90 player_season_lbp_pass_ratio player_season_fhalf_lbp_pass_ratio player_season_f3_lbp_pass_ratio player_season_lbp_received_90 player_season_fhalf_lbp_received_90 player_season_f3_lbp_received_90 player_season_average_lbp_to_space_distance player_season_fhalf_average_lbp_to_space_distance player_season_f3_average_lbp_to_space_distance player_season_lbp_to_space_10_received_90 player_season_fhalf_lbp_to_space_10_received_90 player_season_f3_lbp_to_space_10_received_90 player_season_lbp_to_space_2_received_90 player_season_fhalf_lbp_to_space_2_received_90 player_season_f3_lbp_to_space_2_received_90 player_season_lbp_to_space_5_received_90 player_season_fhalf_lbp_to_space_5_received_90 player_season_f3_lbp_to_space_5_received_90 player_season_average_lbp_to_space_received_distance player_season_fhalf_average_lbp_to_space_received_distance player_season_f3_average_lbp_to_space_received_distance player_season_lbp_to_space_10_90 player_season_fhalf_lbp_to_space_10_90 player_season_f3_lbp_to_space_10_90 player_season_lbp_to_space_2_90 player_season_fhalf_lbp_to_space_2_90 player_season_f3_lbp_to_space_2_90 player_season_lbp_to_space_5_90 player_season_fhalf_lbp_to_space_5_90 player_season_f3_lbp_to_space_5_90"""
#     remove = remove_all.split()
#     player_season = player_season.drop(columns=remove)
#     player_season = player_season[player_season['player_season_90s_played']>min_mins_played]
#     player_season = player_season.fillna(0)
#     return player_season.reset_index(drop=True)

# def removeGoalies(data):
#     data = data[data['primary_position']!="Goalkeeper"]
#     return data.reset_index(drop=True)

# def getPosCat(data):
#     position_mapping = {'Centre Back': 'CB', 'Left Centre Back': 'CB', 'Right Centre Back': 'CB', 'Left Back': 'FB', 'Right Back': 'FB', 'Left Wing Back': 'FB', 'Right Wing Back': 'FB', 'Left Midfielder': 'M', 'Right Midfielder': 'M', 'Centre Defensive Midfielder': 'M', 'Right Defensive Midfielder': 'M', 'Left Defensive Midfielder': 'M', 'Left Centre Midfielder': 'M', 'Right Centre Midfielder': 'M', 'Centre Attacking Midfielder': 'M', 'Left Attacking Midfielder': 'M', 'Right Attacking Midfielder': 'M', 'Centre Forward': 'F', 'Left Centre Forward': 'F', 'Right Centre Forward': 'F', 'Left Wing': 'W', 'Right Wing': 'W'}
#     data['position_category'] = data['primary_position'].map(position_mapping)
#     # color_mapping = {'CB': 'red', 'FB': 'blue', 'M': 'green', 'F': 'orange', 'W': 'purple'}
#     # data['colour'] = data['position_category'].map(color_mapping)
#     return data


# league = 'PSL'
# country = 'South Africa'
# season = "2023/2024"
# min_mins_played = 5
# psl = getSeasonStats(country, league, season, min_mins_played)
# psl = removeGoalies(psl)
# psl = getPosCat(psl)

exclude_cols = ["player_name",'team_name', 'primary_position', 'competition_name', 'position_category']
# cols_to_standardize = [col for col in psl.columns if col not in exclude_cols]
# cols_to_exclude = [col for col in psl.columns if col in exclude_cols]
# scaler = StandardScaler()
# psl[cols_to_standardize] = scaler.fit_transform(psl[cols_to_standardize])

##########SCATTER PLOT FOR PRESSING ABILITIES
intensity_variables = ['player_season_padj_pressures_90',
                        'player_season_counterpressures_90',
                        'player_season_fhalf_pressures_90', 
                        'player_season_fhalf_counterpressures_90']

effectiveness_variables = ['player_season_padj_tackles_90', 'player_season_padj_interceptions_90',
 'player_season_pressure_regains_90',
'player_season_defensive_action_regains_90',
 'player_season_counterpressure_regains_90',
 'player_season_obv_defensive_action_90',
 'player_season_fhalf_ball_recoveries_90']


# psl_strikers = psl[(psl['position_category']=='F') | (psl['player_name']=='Ashley Du Preez')]
keep_pressure = effectiveness_variables + intensity_variables + exclude_cols
# psl_strikers = psl_strikers[keep_pressure]
new_cols_stand = intensity_variables + effectiveness_variables
# from sklearn.preprocessing import MinMaxScaler
# scaler = MinMaxScaler()
# psl_strikers[new_cols_stand] = scaler.fit_transform(psl_strikers[new_cols_stand])

#psl_strikers.to_csv("data/pressures.csv", index=False)

psl_strikers = pd.read_csv("data/pressures.csv")
col1, col2 = st.columns(2)
with col1:
    st.header('Pressure Variables(p90) weights')
    w1intens = st.slider('Possession adjusted pressures', min_value=0.0, max_value=1.0, value=0.5)
    w2intens = st.slider('Counterpressures', min_value=0.0, max_value=1.0, value=0.5)
    w3intens = st.slider('Opposition half pressures', min_value=0.0, max_value=1.0, value=0.5)
    w4intens = st.slider('Opposition half counterpressures', min_value=0.0, max_value=1.0, value=0.5)

with col2:
    st.header('DA Variables(p90) weights')
    w1effecs = st.slider('Possession adjusted tackles', min_value=0.0, max_value=1.0, value=0.5)
    w2effecs = st.slider('Possession adjusted interceptions', min_value=0.0, max_value=1.0, value=0.5)
    w3effecs = st.slider('Pressure regains', min_value=0.0, max_value=1.0, value=0.5)
    w4effecs = st.slider('Defensive action regains', min_value=0.0, max_value=1.0, value=0.5)
    w5effecs = st.slider('Counterpressure regains', min_value=0.0, max_value=1.0, value=0.5)
    w6effecs = st.slider('Opposition half ball recoveries', min_value=0.0, max_value=1.0, value=0.5)
    w7effecs = st.slider('Defensive OBV', min_value=0.0, max_value=1.0, value=0.5)


psl_strikers['Intensity'] = (
    (w1intens*psl_strikers['player_season_padj_pressures_90']) +
    (w2intens*psl_strikers['player_season_counterpressures_90'])+
    (w3intens*psl_strikers['player_season_fhalf_pressures_90'])+
    (w4intens*psl_strikers['player_season_fhalf_counterpressures_90'])
)

psl_strikers['Effectiveness'] = (
    (w1effecs*psl_strikers['player_season_padj_tackles_90']) +
    (w2effecs*psl_strikers['player_season_padj_interceptions_90']) +
    (w3effecs*psl_strikers['player_season_pressure_regains_90']) +
    (w4effecs*psl_strikers['player_season_defensive_action_regains_90']) +
    (w5effecs*psl_strikers['player_season_counterpressure_regains_90']) +
    (w6effecs*psl_strikers['player_season_fhalf_ball_recoveries_90'])+
    (w7effecs*psl_strikers['player_season_obv_defensive_action_90'])
)


########JUST PLOTTING########
psl_strikers['selected'] = psl_strikers['player_name'].apply(lambda x: 'green' if x in ['Iqraam Rayners', 'Ashley Du Preez', 'Ranga Piniel Chivaviro', 'Khanyisa Mayo'] else 'red')

x_filtered = psl_strikers['Effectiveness']
y_filtered = psl_strikers['Intensity']
names_filtered = psl_strikers['player_name']


fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x_filtered,
    y=y_filtered,
    mode='markers',
    marker=dict(
        color=psl_strikers['selected'], 
        #colorscale='Viridis',
        showscale=False,
        size=10
    ),
    #text=names_filtered,
    text=[f'{name}<br>Defensive Actions p90: {effec:.2f}<br>Pressures p90: {intens:.2f}' for name, effec, intens in zip(psl_strikers['player_name'],psl_strikers['Effectiveness'], psl_strikers['Intensity'])],  # Customized hover text
    hoverinfo='text'
))
# Calculate and plot the mean lines for the filtered data
mean_x_filtered = x_filtered.mean()
mean_y_filtered = y_filtered.mean()
x_min, x_max = x_filtered.min(), x_filtered.max()
y_min, y_max = y_filtered.min(), y_filtered.max()
fig.add_shape(type="line", x0=mean_x_filtered, y0=y_min-100, x1=mean_x_filtered, y1=y_max+100, line=dict(color="red", dash="dash"),)
fig.add_shape(type="line", x0=x_min-100, y0=mean_y_filtered, x1=x_max+100, y1=mean_y_filtered, line=dict(color="green", dash="dash"),)
text_coordinates = [
    (mean_x_filtered + 0.6, mean_y_filtered + 0.6),
    (mean_x_filtered - 0.6, mean_y_filtered + 0.6),
    (mean_x_filtered - 0.6, mean_y_filtered - 0.6),
    (mean_x_filtered + 0.6, mean_y_filtered - 0.6)
]
# Add annotations for text in each quadrant
quadrant_texts = ['Many DAs<br>Many pressures', 'Low DAs<br>Many pressures',
                   'Low DAs<br>Low pressures', 'Many DAs<br>Low pressures']
for i, (x, y) in enumerate(text_coordinates):
    fig.add_annotation(
        x=x,
        y=y,
        font=dict(size=18, color='black'),
        text=quadrant_texts[i],
        showarrow=False,
        xanchor='center',
        yanchor='bottom'
    )
for i, (x, y, name) in enumerate(zip(x_filtered, y_filtered, names_filtered)):
    fig.add_annotation(
        x=x,
        y=y + 0.04,
        text=name,
        font=dict(size=13, color='black'),  # Set text color to black
        showarrow=False,
        xanchor='center',
        yanchor='bottom'
    )

fig.update_layout(title='PSL Strikers: Defensive Actions p90 vs Pressures p90',
                  xaxis=dict(
        title='Defensive Actions p90',
        title_font=dict(size=20),  # Adjust the font size here
        tickfont=dict(size=16),  # Adjust the tick font size here
    ),
    yaxis=dict(
        title='Pressures p90',
        title_font=dict(size=20),  # Adjust the font size here
        tickfont=dict(size=16),  # Adjust the tick font size here
    ),
    xaxis_range=[-0.1, x_max+0.5],  # Adjusting x-axis range
    yaxis_range=[-0.1, y_max+0.5], 
    plot_bgcolor='lightgrey')


st.plotly_chart(fig)

data = {
    'Variable': ['Possession adjusted pressures', 'Counterpressures','Opposition half pressures','Opposition half counterpressures',
                 'Possession adjusted tackles','Possession adjusted interceptions','Pressure regains','Defensive action regains',
                 'Counterpressure regains','Opposition half ball recoveries','Defensive OBV'],
    'Description': ['Pressures adjusted for team possession', 'Pressures exerted within 5 seconds of a turnover', "Pressures exerted in opposition's half", "Counterpressures exerted in opposition's half",
                    'Tackles adjusted for team possession', 'Interceptions adjusted for team possession', 'Player wins the ball back within 5 seconds of pressuring',"Player wins ball back within 5 seconds of making defensive action",
                    'Player wins ball back within 5 seconds of counterpressuring an opponent',"Player recovers the ball in opposition's half", "Quality of tackles"]
}
df = pd.DataFrame(data)

st.table(df)

