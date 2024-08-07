import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Example DataFrame
tsne_df = pd.read_csv("data/pics/tsne.csv")
# Create a color and symbol map for the categories
color_map = {cat: px.colors.qualitative.G10[i % len(px.colors.qualitative.G10)] for i, cat in enumerate(tsne_df['pos_cat'].unique())}
symbol_map = {comp: i for i, comp in enumerate(tsne_df['competition_name'].unique())}

special_players = ['Iqraam Rayners', 'Ashley Cupido']

# Create a custom color mapping function
def get_color(row):
    if row['player_name'] in special_players:
        return 'white'
    return color_map[row['pos_cat']]

# Create a Plotly figure
fig = go.Figure()

for pos_cat in tsne_df['pos_cat'].unique():
    filtered_df = tsne_df[tsne_df['pos_cat'] == pos_cat]
    
    fig.add_trace(go.Scatter(
        x=filtered_df['TSNE1'],
        y=filtered_df['TSNE2'],
        mode='markers',
        name=pos_cat,
        marker=dict(
            size=7,
            color=filtered_df.apply(get_color, axis=1),  # Assign colors using the custom mapping function
            symbol=filtered_df['competition_name'].map(symbol_map),  # Shape by competition name
            showscale=False  # Disable the color scale for each individual trace
        ),
        text=filtered_df.apply(lambda row: f"{row['competition_name']}<br>{row['player_name']}<br>{row['pos_cat']}", axis=1),
        hoverinfo='text'
    ))


# Create a scatter trace for the shape legend
for comp, symbol in symbol_map.items():
    fig.add_trace(go.Scatter(
        x=[None], y=[None],
        mode='markers',
        name=comp,
        marker=dict(size=10, symbol=symbol, color='white'),
        legendgroup='Competition',
        showlegend=True
    ))

# Update layout
fig.update_layout(
    title='',
    xaxis_title='Length',
    yaxis_title='Width',
    legend_title_text='Position',
    legend=dict(itemsizing='constant'),
    paper_bgcolor='#303030',
    plot_bgcolor='#303030',
    font=dict(family='Futura', color='white'),
    title_font=dict(size=20, family='Futura', color='white'),
    xaxis=dict(title_font=dict(size=14, family='Futura', color='white')),
    yaxis=dict(title_font=dict(size=14, family='Futura', color='white'))
)

# Streamlit code to display the plot
st.title('Comparison Visualization')
st.plotly_chart(fig)
