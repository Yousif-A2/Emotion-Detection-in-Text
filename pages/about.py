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
        # Mission section
        st.markdown(f"""
        <div class="card-container">
            <h3 style="margin-top: 0; color: {COLOR_PALETTE['primary']};">Our Mission</h3>
            
            <p>
                At EmotionSense AI, our mission is to bridge the gap between text and emotion, providing valuable 
                insights into the emotional content hidden within written communication. We believe that understanding 
                emotions is crucial for enhancing communication, improving customer experiences, and gaining deeper 
                insights into human expression.
            </p>
            
            <div style="display: flex; align-items: center; background: linear-gradient(45deg, {COLOR_PALETTE['primary']}22, {COLOR_PALETTE['secondary']}22);
                        padding: 20px; border-radius: 10px; margin: 20px 0;">
                <div style="font-size: 3rem; margin-right: 20px; color: {COLOR_PALETTE['primary']};">💡</div>
                <div>
                    <h4 style="margin-top: 0; color: {COLOR_PALETTE['text']};">Our Vision</h4>
                    <p style="margin-bottom: 0;">
                        We envision a world where emotional intelligence is seamlessly integrated into digital communication,
                        helping individuals and organizations better understand and respond to the emotional aspects of textual content.
                    </p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # How it works section
        st.markdown(f"""
        <div class="card-container">
            <h3 style="margin-top: 0; color: {COLOR_PALETTE['primary']};">How It Works</h3>
            
            <p>
                EmotionSense AI uses advanced natural language processing and machine learning techniques to analyze and identify
                emotions in textual data. Our system processes text through multiple layers of analysis to extract meaningful
                emotional signals.
            </p>
            
            <div style="display: flex; flex-wrap: wrap; gap: 20px; margin-top: 25px;">
                <div style="flex: 1; min-width: 250px; border-radius: 10px; padding: 20px; background-color: #f9f9f9; 
                            box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
                    <div style="display: flex; align-items: center; margin-bottom: 15px;">
                        <span style="background-color: {COLOR_PALETTE['primary']}; color: white; width: 36px; height: 36px;
                                    border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-right: 15px;">1</span>
                        <h4 style="margin: 0; color: {COLOR_PALETTE['primary']};">Text Preprocessing</h4>
                    </div>
                    <p style="margin: 0; padding-left: 51px;">
                        Raw text is cleaned, tokenized, and normalized to prepare it for analysis. This step removes noise and
                        standardizes the text format.
                    </p>
                </div>
                
                <div style="flex: 1; min-width: 250px; border-radius: 10px; padding: 20px; background-color: #f9f9f9; 
                            box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
                    <div style="display: flex; align-items: center; margin-bottom: 15px;">
                        <span style="background-color: {COLOR_PALETTE['secondary']}; color: white; width: 36px; height: 36px;
                                    border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-right: 15px;">2</span>
                        <h4 style="margin: 0; color: {COLOR_PALETTE['secondary']};">Feature Extraction</h4>
                    </div>
                    <p style="margin: 0; padding-left: 51px;">
                        The system extracts linguistic features, emotional keywords, and contextual patterns that serve as
                        indicators of different emotions.
                    </p>
                </div>
                
                <div style="flex: 1; min-width: 250px; border-radius: 10px; padding: 20px; background-color: #f9f9f9; 
                            box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
                    <div style="display: flex; align-items: center; margin-bottom: 15px;">
                        <span style="background-color: {COLOR_PALETTE['tertiary']}; color: white; width: 36px; height: 36px;
                                    border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-right: 15px;">3</span>
                        <h4 style="margin: 0; color: {COLOR_PALETTE['tertiary']};">Machine Learning Model</h4>
                    </div>
                    <p style="margin: 0; padding-left: 51px;">
                        Our trained machine learning model analyzes these features to classify the text into different
                        emotional categories with a confidence score.
                    </p>
                </div>
                
                <div style="flex: 1; min-width: 250px; border-radius: 10px; padding: 20px; background-color: #f9f9f9; 
                            box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
                    <div style="display: flex; align-items: center; margin-bottom: 15px;">
                        <span style="background-color: {COLOR_PALETTE['primary']}; color: white; width: 36px; height: 36px;
                                    border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-right: 15px;">4</span>
                        <h4 style="margin: 0; color: {COLOR_PALETTE['primary']};">Results Visualization</h4>
                    </div>
                    <p style="margin: 0; padding-left: 51px;">
                        The identified emotions and their probabilities are visualized in an intuitive way, making it easy
                        to understand the emotional content of the text.
                    </p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Applications section
        st.markdown(f"""
        <div class="card-container">
            <h3 style="margin-top: 0; color: {COLOR_PALETTE['primary']};">Applications</h3>
            
            <p>
                Emotion detection in text has a wide range of applications across various industries and use cases.
                Here are some of the key applications of our technology:
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Application cards
        col1, col2 = st.columns(2)
        
        with col1:
            render_card(
                """
                <p>Monitor customer sentiment across social media platforms, review sites, and feedback forms. 
                Identify emotional trends and respond promptly to negative sentiment.</p>
                """,
                "Social Media Sentiment Analysis",
                "📱"
            )
            
            render_card(
                """
                <p>Understand the emotional response to marketing campaigns, product launches, and brand messaging.
                Gain insights into consumer emotions to refine marketing strategies.</p>
                """,
                "Market Research & Consumer Insights",
                "📊"
            )
            
            render_card(
                """
                <p>Enhance chatbots and virtual assistants with emotional intelligence, enabling them to respond 
                appropriately to users' emotional states.</p>
                """,
                "AI Assistants & Chatbots",
                "🤖"
            )
        
        with col2:
            render_card(
                """
                <p>Analyze customer support interactions to identify and prioritize distressed customers.
                Improve response strategies based on emotional context.</p>
                """,
                "Customer Support Optimization",
                "🎯"
            )
            
            render_card(
                """
                <p>Track employee satisfaction and engagement through internal communications.
                Identify potential issues before they affect morale and productivity.</p>
                """,
                "Workplace Analytics",
                "👥"
            )
            
            render_card(
                """
                <p>Enhance content recommendation systems by considering emotional aspects,
                delivering more relevant and engaging content to users.</p>
                """,
                "Content Personalization",
                "📝"
            )
        
        # Contact section
        st.markdown(f"""
        <div class="card-container" style="text-align: center;">
            <h3 style="margin-top: 0; color: {COLOR_PALETTE['primary']};">Get in Touch</h3>
            
            <p>
                Have questions or interested in learning more about EmotionSense AI?
                We'd love to hear from you!
            </p>
            
            <div style="margin: 30px 0; display: flex; justify-content: center; gap: 20px;">
                <div style="padding: 15px 30px; background-color: {COLOR_PALETTE['primary']}; color: white; 
                            border-radius: 50px; font-weight: 500; box-shadow: 0 4px 12px rgba(0,0,0,0.1);">
                    Contact Us
                </div>
                
                <div style="padding: 15px 30px; background-color: white; color: {COLOR_PALETTE['primary']}; 
                            border: 2px solid {COLOR_PALETTE['primary']}; border-radius: 50px; font-weight: 500;">
                    Documentation
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
