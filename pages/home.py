import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from datetime import datetime
import joblib

try:
    from utils.track_utils import add_page_visited_details, add_prediction_details, IST
    from utils.style_utils import (
        COLOR_PALETTE, 
        EMOTION_COLORS, 
        render_gradient_header, 
        render_card, 
        get_emotion_icon,
        create_altair_therender_cardme
    )
except ImportError:
    # Fallback to direct imports
    from utils.track_utils import add_page_visited_details, add_prediction_details, IST
    from utils.style_utils import (
        COLOR_PALETTE, 
        EMOTION_COLORS, 
        render_gradient_header, 
        render_card, 
        get_emotion_icon,
        create_altair_theme
    )

# Register the custom theme for Altair charts
alt.themes.register('emotion_theme', create_altair_theme)
alt.themes.enable('emotion_theme')

# Load model function
@st.cache_resource
def load_emotion_model():
    return joblib.load(open("./models/emotion_classifier_pipe_lr.pkl", "rb"))

def predict_emotions(docx, model):
    results = model.predict([docx])
    return results[0]

def get_prediction_proba(docx, model):
    results = model.predict_proba([docx])
    return results

def render_home_page():
    """Render the home page of the Emotion Classification app"""
    # Load the model
    pipe_lr = load_emotion_model()
    
    # Add page visit tracking
    add_page_visited_details("Home", datetime.now(IST))
    
    # Render the header
    render_gradient_header(
        "EmotionSense AI", 
        "Uncover the emotions hidden in your text with our advanced emotion detection technology."
    )
    
    # Main layout with some space on the sides
    col_space1, main_col, col_space2 = st.columns([1, 10, 1])
    
    with main_col:
        # Input card
        st.markdown("""
        <div class="card-container">
            <h3 style="margin-top: 0;">Try It Now</h3>
            <p>Enter any text below to analyze its emotional content.</p>
        </div>
        """, unsafe_allow_html=True)
        
        with st.form(key='emotion_clf_form'):
            raw_text = st.text_area(
                "Type or paste your text here",
                height=150,
                help="Enter the text you want to analyze for emotional content"
            )
            
            # Form submission button with custom styling
            col1, col2, col3 = st.columns([3, 4, 3])
            with col2:
                submit_text = st.form_submit_button(
                    label='Analyze Emotions',
                    use_container_width=True,
                )
        
        # Process text and display results
        if submit_text and raw_text:
            # Predict emotion and probability
            prediction = predict_emotions(raw_text, pipe_lr)
            probability = get_prediction_proba(raw_text, pipe_lr)
            
            # Add prediction to database
            add_prediction_details(raw_text, prediction, np.max(probability), datetime.now(IST))
            
            # Display results in two columns
            col1, col2 = st.columns([1, 1])
            
            with col1:
                # Original text and prediction card
                emoji_icon = get_emotion_icon(prediction)
                emotion_color = EMOTION_COLORS.get(prediction.lower(), COLOR_PALETTE["primary"])
                
                st.markdown(f"""
                <div class="card-container">
                    <h3 style="margin-top: 0;">Your Text</h3>
                    <div style="background-color: #f8f9fa; border-radius: 8px; padding: 15px; margin-bottom: 20px;">
                        {raw_text}
                    </div>
                    
                    <h3>Emotion Detected</h3>
                    <div style="display: flex; align-items: center; margin-bottom: 10px;">
                        <span style="font-size: 2.5rem; margin-right: 15px;">{emoji_icon}</span>
                        <div>
                            <div style="font-size: 1.5rem; font-weight: 600; color: {emotion_color}; text-transform: capitalize;">
                                {prediction}
                            </div>
                            <div style="color: #666; font-size: 0.9rem;">
                                Confidence: {round(np.max(probability) * 100, 1)}%
                            </div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                # Probability visualization card
                st.markdown("""
                <div class="card-container">
                    <h3 style="margin-top: 0;">Emotion Probability Distribution</h3>
                """, unsafe_allow_html=True)
                
                # Create probability dataframe
                proba_df = pd.DataFrame(probability, columns=pipe_lr.classes_)
                proba_df_clean = proba_df.T.reset_index()
                proba_df_clean.columns = ["emotions", "probability"]
                
                # Sort by probability for better visualization
                proba_df_clean = proba_df_clean.sort_values(by="probability", ascending=False)
                
                # Create a custom color scale based on our emotion colors
                emotion_color_scale = alt.Scale(
                    domain=list(proba_df_clean['emotions']),
                    range=[EMOTION_COLORS.get(emotion.lower(), "#ccc") for emotion in proba_df_clean['emotions']]
                )
                
                # Create horizontal bar chart
                chart = alt.Chart(proba_df_clean).mark_bar().encode(
                    x=alt.X('probability:Q', axis=alt.Axis(format='%', title='Probability')),
                    y=alt.Y('emotions:N', sort='-x', axis=alt.Axis(title=None)),
                    color=alt.Color('emotions:N', scale=emotion_color_scale, legend=None),
                    tooltip=['emotions', alt.Tooltip('probability:Q', format='.1%')]
                ).properties(
                    height=300
                ).configure_axis(
                    labelFontSize=12,
                    titleFontSize=14
                )
                
                st.altair_chart(chart, use_container_width=True)
                st.markdown("</div>", unsafe_allow_html=True)
        
        elif submit_text and not raw_text:
            st.warning("Please enter some text to analyze")
        
        # Show features section if no analysis is happening yet
        if not submit_text or not raw_text:
            # First, create the header of the card
            st.markdown("""
            <div class="card-container">
                <h3 style="margin-top: 0;">How It Works</h3>
                <p>Our AI-powered emotion detection system analyzes the subtleties of language to identify the emotions expressed in your text.</p>
            </div>
            """, unsafe_allow_html=True)

            # Then create three separate cards for each step
            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown("""
                <div style="background-color: #f8f9fa; border-radius: 10px; padding: 15px;">
                    <div style="font-size: 1.8rem; margin-bottom: 10px;">📝</div>
                    <h4 style="margin-top: 0;">Input Your Text</h4>
                    <p style="margin-bottom: 0;">Enter any text you'd like to analyze for emotional content.</p>
                </div>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown("""
                <div style="background-color: #f8f9fa; border-radius: 10px; padding: 15px;">
                    <div style="font-size: 1.8rem; margin-bottom: 10px;">⚙️</div>
                    <h4 style="margin-top: 0;">AI Analysis</h4>
                    <p style="margin-bottom: 0;">Our machine learning model identifies emotional patterns in your text.</p>
                </div>
                """, unsafe_allow_html=True)

            with col3:
                st.markdown("""
                <div style="background-color: #f8f9fa; border-radius: 10px; padding: 15px;">
                    <div style="font-size: 1.8rem; margin-bottom: 10px;">📊</div>
                    <h4 style="margin-top: 0;">Emotion Results</h4>
                    <p style="margin-bottom: 0;">View the detected emotions and their probability distribution.</p>
                </div>
                """, unsafe_allow_html=True)
