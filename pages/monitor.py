import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
from datetime import datetime, timedelta

from utils.track_utils import (
    add_page_visited_details, 
    view_all_page_visited_details, 
    view_all_prediction_details,
    IST
)
from utils.style_utils import (
    COLOR_PALETTE, 
    EMOTION_COLORS,
    render_gradient_header, 
    render_card,
    create_animated_chart_placeholder
)

# Customize plotly theme
def customize_plotly():
    return {
        'layout': {
            'font': {'family': 'Roboto, Arial, sans-serif'},
            'plot_bgcolor': 'rgba(0, 0, 0, 0)',
            'paper_bgcolor': 'rgba(0, 0, 0, 0)',
            'margin': {'t': 30, 'b': 40, 'l': 30, 'r': 30},
            'colorway': list(EMOTION_COLORS.values()),
            'xaxis': {
                'showgrid': True,
                'gridcolor': '#f0f0f0',
                'zeroline': False,
            },
            'yaxis': {
                'showgrid': True,
                'gridcolor': '#f0f0f0',
                'zeroline': False,
            },
            'hovermode': 'closest',
        }
    }

def render_monitor_page():
    """Render the monitor/analytics page of the application"""
    # Add page visit tracking
    add_page_visited_details("Monitor", datetime.now(IST))
    
    # Page header
    render_gradient_header(
        "Analytics Dashboard", 
        "Track usage patterns and emotion detection metrics."
    )
    
    # Create layout
    col_space1, main_col, col_space2 = st.columns([1, 10, 1])
    
    with main_col:
        # Get data for analytics
        page_analytics = pd.DataFrame(
            view_all_page_visited_details(), 
            columns=['Page Name', 'Time of Visit']
        )
        
        emotion_analytics = pd.DataFrame(
            view_all_prediction_details(), 
            columns=['Rawtext', 'Prediction', 'Probability', 'Time_of_Visit']
        )
        
        # Display summary metrics
        if not page_analytics.empty and not emotion_analytics.empty:
            total_visits = len(page_analytics)
            total_predictions = len(emotion_analytics)
            avg_confidence = emotion_analytics['Probability'].mean() * 100 if total_predictions > 0 else 0
            
            # Calculate most recent visit
            now = datetime.now(IST)
            if not page_analytics.empty:
                page_analytics['Time of Visit'] = pd.to_datetime(page_analytics['Time of Visit'])
                most_recent = (now - page_analytics['Time of Visit'].max()).total_seconds() / 60
                most_recent_str = f"{most_recent:.1f} minutes ago" if most_recent < 60 else f"{most_recent/60:.1f} hours ago"
            else:
                most_recent_str = "N/A"
            
            # Create metrics row
            metrics_cols = st.columns(4)
            
            with metrics_cols[0]:
                st.markdown(f"""
                <div class="card-container" style="text-align: center;">
                    <h1 style="font-size: 2.5rem; margin: 0; color: {COLOR_PALETTE['primary']};">{total_visits}</h1>
                    <p style="margin: 0;">Total Page Visits</p>
                </div>
                """, unsafe_allow_html=True)
                
            with metrics_cols[1]:
                st.markdown(f"""
                <div class="card-container" style="text-align: center;">
                    <h1 style="font-size: 2.5rem; margin: 0; color: {COLOR_PALETTE['secondary']};">{total_predictions}</h1>
                    <p style="margin: 0;">Emotions Analyzed</p>
                </div>
                """, unsafe_allow_html=True)
                
            with metrics_cols[2]:
                st.markdown(f"""
                <div class="card-container" style="text-align: center;">
                    <h1 style="font-size: 2.5rem; margin: 0; color: {COLOR_PALETTE['tertiary']};">{avg_confidence:.1f}%</h1>
                    <p style="margin: 0;">Avg. Confidence</p>
                </div>
                """, unsafe_allow_html=True)
                
            with metrics_cols[3]:
                st.markdown(f"""
                <div class="card-container" style="text-align: center;">
                    <h1 style="font-size: 1.2rem; margin: 0; color: {COLOR_PALETTE['text']};">{most_recent_str}</h1>
                    <p style="margin: 0;">Last Activity</p>
                </div>
                """, unsafe_allow_html=True)

        # Create tabs for different analytics sections
        tab1, tab2 = st.tabs(["📊 Page Analytics", "😀 Emotion Analytics"])
        
        with tab1:
            st.markdown(f"""
            <div class="card-container">
                <h3 style="margin-top: 0;">Page Visit Statistics</h3>
            """, unsafe_allow_html=True)
            
            if not page_analytics.empty:
                # Process page analytics data
                pg_count = page_analytics['Page Name'].value_counts().rename_axis('Page Name').reset_index(name='Visits')
                
                # Create two columns for visualization
                col1, col2 = st.columns(2)
                
                with col1:
                    # Bar chart for page visits using Altair
                    bar_chart = alt.Chart(pg_count).mark_bar().encode(
                        x=alt.X('Visits:Q', title='Number of Visits'),
                        y=alt.Y('Page Name:N', sort='-x', title=None),
                        color=alt.Color('Page Name:N', 
                                        scale=alt.Scale(range=[COLOR_PALETTE["primary"], COLOR_PALETTE["secondary"], COLOR_PALETTE["tertiary"]]),
                                        legend=None),
                        tooltip=['Page Name', 'Visits']
                    ).properties(
                        height=200
                    )
                    
                    st.altair_chart(bar_chart, use_container_width=True)
                
                with col2:
                    # Pie chart using Plotly
                    fig = px.pie(
                        pg_count, 
                        values='Visits', 
                        names='Page Name',
                        hole=0.4,
                        color_discrete_sequence=[COLOR_PALETTE["primary"], COLOR_PALETTE["secondary"], COLOR_PALETTE["tertiary"]]
                    )
                    
                    # Apply custom styling
                    fig.update_layout(**customize_plotly()['layout'])
                    fig.update_traces(textposition='inside', textinfo='percent+label')
                    
                    st.plotly_chart(fig, use_container_width=True)
                
                # Process time data for visits over time
                if len(page_analytics) > 1:
                    st.markdown("""<h4>Visits Over Time</h4>""", unsafe_allow_html=True)
                    
                    # Convert to datetime if it's not already
                    if not pd.api.types.is_datetime64_any_dtype(page_analytics['Time of Visit']):
                        page_analytics['Time of Visit'] = pd.to_datetime(page_analytics['Time of Visit'])
                    
                    # Group by hour
                    page_analytics['hour'] = page_analytics['Time of Visit'].dt.floor('H')
                    visits_by_time = page_analytics.groupby(['hour', 'Page Name']).size().reset_index(name='count')
                    
                    # Create time series chart
                    time_chart = alt.Chart(visits_by_time).mark_line(point=True).encode(
                        x=alt.X('hour:T', title='Time'),
                        y=alt.Y('count:Q', title='Number of Visits'),
                        color=alt.Color('Page Name:N', 
                                        scale=alt.Scale(range=[COLOR_PALETTE["primary"], COLOR_PALETTE["secondary"], COLOR_PALETTE["tertiary"]]))
                    ).properties(
                        height=250
                    )
                    
                    st.altair_chart(time_chart, use_container_width=True)
            else:
                st.info("No page visit data available yet. Start using the app to generate analytics.")
            
            st.markdown("</div>", unsafe_allow_html=True)
        
        with tab2:
            st.markdown(f"""
            <div class="card-container">
                <h3 style="margin-top: 0;">Emotion Detection Analytics</h3>
            """, unsafe_allow_html=True)
            
            if not emotion_analytics.empty:
                # Process emotion analytics data
                emotion_counts = emotion_analytics['Prediction'].value_counts().rename_axis('Emotion').reset_index(name='Count')
                
                # Create custom color scale for emotions
                emotion_colors = [EMOTION_COLORS.get(emotion.lower(), "#ccc") for emotion in emotion_counts['Emotion']]
                
                # Create two columns for visualization
                col1, col2 = st.columns(2)
                
                with col1:
                    # Bar chart for emotions using Altair
                    emotion_bar = alt.Chart(emotion_counts).mark_bar().encode(
                        x=alt.X('Count:Q', title='Number of Occurrences'),
                        y=alt.Y('Emotion:N', sort='-x', title=None),
                        color=alt.Color('Emotion:N', 
                                        scale=alt.Scale(domain=list(emotion_counts['Emotion']), range=emotion_colors),
                                        legend=None),
                        tooltip=['Emotion', 'Count']
                    ).properties(
                        height=250
                    )
                    
                    st.altair_chart(emotion_bar, use_container_width=True)
                
                with col2:
                    # Pie chart using Plotly
                    fig = px.pie(
                        emotion_counts, 
                        values='Count', 
                        names='Emotion',
                        hole=0.4,
                        color='Emotion',
                        color_discrete_map={emotion: EMOTION_COLORS.get(emotion.lower(), "#ccc") for emotion in emotion_counts['Emotion']}
                    )
                    
                    # Apply custom styling
                    fig.update_layout(**customize_plotly()['layout'])
                    fig.update_traces(textposition='inside', textinfo='percent+label')
                    
                    st.plotly_chart(fig, use_container_width=True)
                                    
                # Create histogram for confidence levels    
                st.markdown("""<h4>Confidence Distribution</h4>""", unsafe_allow_html=True)

                try:
                    # Make sure Probability is a numeric column
                    emotion_analytics['Probability'] = pd.to_numeric(emotion_analytics['Probability'], errors='coerce')
                    
                    # Drop any rows with NaN values
                    emotion_analytics_clean = emotion_analytics.dropna(subset=['Probability'])
                    
                    if not emotion_analytics_clean.empty:
                        # Create histogram for confidence levels
                        confidence_hist = alt.Chart(emotion_analytics_clean).mark_bar().encode(
                            x=alt.X('Probability:Q', 
                                    bin=alt.Bin(maxbins=10), 
                                    title='Confidence Level',
                                    scale=alt.Scale(domain=[0, 1])),  # Set domain from 0 to 1
                            y=alt.Y('count()', title='Number of Predictions'),
                            tooltip=[
                                alt.Tooltip('count()', title='Count'), 
                                alt.Tooltip('Probability:Q', title='Confidence', format='.1%')
                            ]
                        ).properties(
                            height=450
                        ).configure_mark(
                            color=COLOR_PALETTE["primary"]
                        )
                        
                        st.altair_chart(confidence_hist, use_container_width=True)
                    else:
                        st.info("No confidence data available for histogram.")
                except Exception as e:
                    st.error(f"Error generating confidence histogram: {e}")
                    # Fallback to a simple text description
                    st.write("Confidence distribution visualization is not available.")
            
                # Display recent predictions
                st.markdown("""<h4>Recent Predictions</h4>""", unsafe_allow_html=True)
                
                # Convert to datetime if needed
                if not pd.api.types.is_datetime64_any_dtype(emotion_analytics['Time_of_Visit']):
                    emotion_analytics['Time_of_Visit'] = pd.to_datetime(emotion_analytics['Time_of_Visit'])
                
                # Sort by time and take the most recent 10
                recent_predictions = emotion_analytics.sort_values('Time_of_Visit', ascending=False).head(10)
                
                # Format for display
                display_df = recent_predictions.copy()
                display_df['Time'] = display_df['Time_of_Visit'].dt.strftime('%Y-%m-%d %H:%M')
                display_df['Confidence'] = (display_df['Probability'].astype(float) * 100).round(1).astype(str) + '%'
                display_df = display_df[['Time', 'Prediction', 'Confidence', 'Rawtext']].rename(columns={'Rawtext': 'Text'})
                
                # Truncate text if too long
                display_df['Text'] = display_df['Text'].apply(lambda x: (x[:50] + '...') if len(x) > 50 else x)
                
                # Display table
                st.dataframe(display_df, use_container_width=True)
            else:
                st.info("No emotion analysis data available yet. Start analyzing text to generate analytics.")
                
            st.markdown("</div>", unsafe_allow_html=True)