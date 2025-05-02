import streamlit as st
from datetime import datetime

from utils.track_utils import add_page_visited_details, IST
from utils.style_utils import COLOR_PALETTE, render_gradient_header, render_card

def render_about_page():
    """Render the about page of the application"""
    # Add page visit tracking
    add_page_visited_details("About", datetime.now(IST))
    
    # Page header
    render_gradient_header(
        "About EmotionSense AI", 
        "Learn more about our emotion detection platform and how it works."
    )
    
    # Main layout with some space on the sides
    col_space1, main_col, col_space2 = st.columns([1, 10, 1])
    
    with main_col:
        # About the app section
        st.markdown("""
        <div class="card-container">
            <h3 style="margin-top: 0;">Our Mission</h3>
            <p>
                EmotionSense AI was created to help people better understand the emotional content of their text communications.
                By leveraging machine learning and natural language processing, we provide insights into the emotions expressed
                in text, helping users communicate more effectively and develop emotional intelligence.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Features section
        st.markdown("""
        <div class="card-container">
            <h3 style="margin-top: 0;">Key Features</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Feature cards in two rows
        row1_col1, row1_col2 = st.columns(2)
        
        with row1_col1:
            st.markdown(f"""
            <div style="background-color: white; border-radius: 10px; padding: 20px; height: 100%; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);">
                <div style="font-size: 2rem; color: {COLOR_PALETTE['primary']}; margin-bottom: 15px;">🔍</div>
                <h4 style="margin-top: 0; color: {COLOR_PALETTE['primary']};">Emotion Detection</h4>
                <p>
                    Our advanced machine learning model analyzes text to identify the primary emotion being expressed,
                    helping you understand the emotional tone of your communications.
                </p>
            </div>
            """, unsafe_allow_html=True)
            
        with row1_col2:
            st.markdown(f"""
            <div style="background-color: white; border-radius: 10px; padding: 20px; height: 100%; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);">
                <div style="font-size: 2rem; color: {COLOR_PALETTE['secondary']}; margin-bottom: 15px;">📊</div>
                <h4 style="margin-top: 0; color: {COLOR_PALETTE['secondary']};">Probability Analysis</h4>
                <p>
                    See the confidence levels for each emotion in your text, giving you a nuanced view of the
                    emotional content beyond just the primary emotion.
                </p>
            </div>
            """, unsafe_allow_html=True)
            
        row2_col1, row2_col2 = st.columns(2)
        
        with row2_col1:
            st.markdown(f"""
            <div style="background-color: white; border-radius: 10px; padding: 20px; height: 100%; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);">
                <div style="font-size: 2rem; color: {COLOR_PALETTE['tertiary']}; margin-bottom: 15px;">💡</div>
                <h4 style="margin-top: 0; color: {COLOR_PALETTE['tertiary']};">Personalized Recommendations</h4>
                <p>
                    Receive tailored suggestions and strategies based on the detected emotions, helping you respond
                    constructively to various emotional states.
                </p>
            </div>
            """, unsafe_allow_html=True)
            
        with row2_col2:
            st.markdown(f"""
            <div style="background-color: white; border-radius: 10px; padding: 20px; height: 100%; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);">
                <div style="font-size: 2rem; color: {COLOR_PALETTE['text']}; margin-bottom: 15px;">📱</div>
                <h4 style="margin-top: 0; color: {COLOR_PALETTE['text']};">Usage Analytics</h4>
                <p>
                    Track your emotion patterns over time and gain insights into your emotional expressions
                    through our comprehensive analytics dashboard.
                </p>
            </div>
            """, unsafe_allow_html=True)
        
        # How it works section
        st.markdown("""
        <div class="card-container">
            <h3 style="margin-top: 0;">How It Works</h3>
            <p>
                EmotionSense AI uses a machine learning model trained on a diverse dataset of emotional text. 
                The system analyzes various linguistic features such as word choice, sentence structure, and context
                to identify the emotional content of your text.
            </p>
            <p>
                Our recommendation engine uses the detected emotions to provide personalized strategies and suggestions 
                to help you navigate different emotional states constructively.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Team or contact section
        st.markdown(f"""
        <div class="card-container">
            <h3 style="margin-top: 0;">Contact Us</h3>
            <div style="display: flex; align-items: center; margin-top: 20px;">
                <div style="background-color: {COLOR_PALETTE['primary']}; color: white; 
                     width: 50px; height: 50px; border-radius: 50%; display: flex; 
                     align-items: center; justify-content: center; font-size: 1.5rem;
                     margin-right: 20px;">
                    ✉️
                </div>
                <div>
                    <h4 style="margin-top: 0; margin-bottom: 5px;">Email Us</h4>
                    <p style="margin: 0;">support@emotionsense.ai</p>
                </div>
            </div>
            
            <div style="display: flex; align-items: center; margin-top: 20px;">
                <div style="background-color: {COLOR_PALETTE['secondary']}; color: white; 
                     width: 50px; height: 50px; border-radius: 50%; display: flex; 
                     align-items: center; justify-content: center; font-size: 1.5rem;
                     margin-right: 20px;">
                    📱
                </div>
                <div>
                    <h4 style="margin-top: 0; margin-bottom: 5px;">Call Us</h4>
                    <p style="margin: 0;">+1 (555) 123-4567</p>
                </div>
            </div>
            
            <div style="margin-top: 30px; text-align: center;">
                <p style="margin-bottom: 5px;">Follow us on social media:</p>
                <div style="display: flex; justify-content: center; gap: 15px;">
                    <div style="width: 40px; height: 40px; background-color: #f8f9fa; 
                         border-radius: 50%; display: flex; align-items: center; 
                         justify-content: center; font-size: 1.2rem;">
                        𝕏
                    </div>
                    <div style="width: 40px; height: 40px; background-color: #f8f9fa; 
                         border-radius: 50%; display: flex; align-items: center; 
                         justify-content: center; font-size: 1.2rem;">
                        📘
                    </div>
                    <div style="width: 40px; height: 40px; background-color: #f8f9fa; 
                         border-radius: 50%; display: flex; align-items: center; 
                         justify-content: center; font-size: 1.2rem;">
                        📸
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Footer
        st.markdown(f"""
        <div style="text-align: center; margin-top: 30px; padding: 20px; 
             border-top: 1px solid #eee; font-size: 0.8rem; color: #666;">
            © {datetime.now().year} EmotionSense AI. All rights reserved.
        </div>
        """, unsafe_allow_html=True)