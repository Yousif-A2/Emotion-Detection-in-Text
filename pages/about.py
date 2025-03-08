import streamlit as st
from datetime import datetime

from utils.track_utils import add_page_visited_details, IST
from utils.style_utils import (
    COLOR_PALETTE, 
    render_gradient_header, 
    render_card, 
    render_feature_box
)

def render_about_page():
    """Render the about page of the application"""
    # Add page visit tracking
    add_page_visited_details("About", datetime.now(IST))
    
    # Page header
    render_gradient_header(
        "About EmotionSense AI", 
        "Understanding the science and technology behind our emotion detection system."
    )
    
    # Main layout
    col_space1, main_col, col_space2 = st.columns([1, 10, 1])
    
    with main_col:
    # Mission section - simplified
        st.markdown("""
                        <div class="card-container">
                            <h3 style="margin-top: 0; color: #6C63FF;">Our Mission</h3>
                    <p> At EmotionSense AI, our mission is to bridge the gap between text and emotion, providing valuable 
                                insights into the emotional content hidden within written communication. We believe that understanding 
                                emotions is crucial for enhancing communication, improving customer experiences, and gaining deeper 
                                insights into human expression.
                    </p>
                        </div>
                    """, unsafe_allow_html=True)
        
        # Vision box - as a separate component
        st.markdown("""
        <div class="card-container" style="background-color: #f5f3ff; padding: 20px; border-radius: 10px; margin: 20px 0;">
            <div style="display: flex; align-items: center;">
                <div style="font-size: 3rem; margin-right: 20px; color: #6C63FF;">💡</div>
                <div>
                    <h4 style="margin-top: 0; color: #2A2A72;">Our Vision</h4>
                    <p style="margin-bottom: 0;">
                        We envision a world where emotional intelligence is seamlessly integrated into digital communication,
                        helping individuals and organizations better understand and respond to the emotional aspects of textual content.
                    </p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # How it works section - header only
        st.markdown("""
        <div class="card-container">
            <h3 style="margin-top: 0; color: #6C63FF;">How It Works</h3>
                    <p>
                EmotionSense AI uses advanced natural language processing and machine learning techniques to analyze and identify
                emotions in textual data. Our system processes text through multiple layers of analysis to extract meaningful
                emotional signals.
                    </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Process steps as separate columns
        col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="border-radius: 10px; padding: 20px; background-color: #f9f9f9; box-shadow: 0 2px 10px rgba(0,0,0,0.05); margin-bottom: 20px;">
            <div style="display: flex; align-items: center; margin-bottom: 15px;">
                <span style="background-color: #6C63FF; color: white; width: 36px; height: 36px;
                            border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-right: 15px; text-align: center;">1</span>
                <h4 style="margin: 0; color: #6C63FF;">Text Preprocessing</h4>
            </div>
            <p style="margin: 0; padding-left: 51px;">
                Raw text is cleaned, tokenized, and normalized to prepare it for analysis. This step removes noise and
                standardizes the text format.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="border-radius: 10px; padding: 20px; background-color: #f9f9f9; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
            <div style="display: flex; align-items: center; margin-bottom: 15px;">
                <span style="background-color: #4ECDC4; color: white; width: 36px; height: 36px;
                            border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-right: 15px; text-align: center;">3</span>
                <h4 style="margin: 0; color: #4ECDC4;">Machine Learning Model</h4>
            </div>
            <p style="margin: 0; padding-left: 51px;">
                Our trained machine learning model analyzes these features to classify the text into different
                emotional categories with a confidence score.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="border-radius: 10px; padding: 20px; background-color: #f9f9f9; box-shadow: 0 2px 10px rgba(0,0,0,0.05); margin-bottom: 20px;">
            <div style="display: flex; align-items: center; margin-bottom: 15px;">
                <span style="background-color: #FF8066; color: white; width: 36px; height: 36px;
                            border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-right: 15px; text-align: center;">2</span>
                <h4 style="margin: 0; color: #FF8066;">Feature Extraction</h4>
            </div>
            <p style="margin: 0; padding-left: 51px;">
                The system extracts linguistic features, emotional keywords, and contextual patterns that serve as
                indicators of different emotions.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="border-radius: 10px; padding: 20px; background-color: #f9f9f9; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
            <div style="display: flex; align-items: center; margin-bottom: 15px;">
                <span style="background-color: #6C63FF; color: white; width: 36px; height: 36px;
                            border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-right: 15px; text-align: center;">4</span>
                <h4 style="margin: 0; color: #6C63FF;">Results Visualization</h4>
            </div>
            <p style="margin: 0; padding-left: 51px;">
                The identified emotions and their probabilities are visualized in an intuitive way, making it easy
                to understand the emotional content of the text.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Applications section - header
    st.markdown("""
    <div class="card-container">
        <h3 style="margin-top: 0; color: #6C63FF;">Applications</h3>
                <p>
            Emotion detection in text has a wide range of applications across various industries and use cases.
            Here are some of the key applications of our technology:
                </p>
    </div>
    """, unsafe_allow_html=True)
    
    