import streamlit as st
from PIL import Image
import base64
from pathlib import Path

# Modern color palette
COLOR_PALETTE = {
    "primary": "#6C63FF",       # Vibrant purple - primary brand color
    "secondary": "#FF8066",     # Coral - accent color
    "tertiary": "#4ECDC4",      # Teal - tertiary accent
    "background": "#F9F7FE",    # Light purple tint - background
    "text": "#2A2A72",          # Dark blue - text
    "success": "#59CE8F",       # Green - success messages
    "warning": "#FFBF60",       # Orange - warnings
    "error": "#FF5C5C",         # Red - errors
    "neutral": "#E6E6E6"        # Light gray - neutral elements
}

# Emotion-specific colors that complement the main palette
EMOTION_COLORS = {
    "anger": "#FF5C5C",
    "disgust": "#85B79D", 
    "fear": "#9793FF",
    "happy": "#FFD166",
    "joy": "#FFB347",
    "neutral": "#A3A1BB",
    "sad": "#6C91C2",
    "sadness": "#6C91C2",
    "shame": "#FF9A8B",
    "surprise": "#66D7D1"
}

def set_page_config():
    """Configure the default page settings"""
    st.set_page_config(
        page_title="EmotionSense AI",
        page_icon="🧠",
        layout="wide",
        initial_sidebar_state="expanded", 
        menu_items=None
    )

def apply_custom_styles():
    """Apply custom CSS to enhance the app's appearance"""
    custom_css = f"""
    <style>
        /* Base styling */
        body {{
            background-color: {COLOR_PALETTE["background"]};
            color: {COLOR_PALETTE["text"]};
            font-family: 'Roboto', sans-serif;
        }}
        
        /* Header styling */
        .main .block-container {{
            padding-top: 2rem;
        }}
        
        h1, h2, h3, h4, h5, h6 {{
            color: {COLOR_PALETTE["primary"]};
            font-weight: 600;
        }}
        
        h1 {{
            font-size: 2.5rem;
            margin-bottom: 1.5rem;
            background: linear-gradient(45deg, {COLOR_PALETTE["primary"]}, {COLOR_PALETTE["secondary"]});
            -webkit-background-clip: text;
        #    -webkit-text-fill-color: transparent;
            padding: 0.5rem 0;
        }}
        
        /* Card-like containers */
        .stExpander {{
            border: none;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
            margin-bottom: 1.5rem;
        }}
        
        /* Button styling */
        .stButton>button {{
            background-color: {COLOR_PALETTE["primary"]};
            color: white;
            border-radius: 50px;
            border: none;
            padding: 0.5rem 2rem;
            font-weight: 500;
            transition: all 0.3s ease;
        }}
        
        .stButton>button:hover {{
            background-color: {COLOR_PALETTE["secondary"]};
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
            transform: translateY(-2px);
        }}
        
        /* Form styling */
        .stTextArea textarea {{
            border-radius: 10px;
            border: 1px solid {COLOR_PALETTE["neutral"]};
            padding: 1rem;
            box-shadow: inset 0 1px 2px rgba(0,0,0,0.05);
        }}
        
        .stTextArea textarea:focus {{
            border-color: {COLOR_PALETTE["primary"]};
            box-shadow: 0 0 0 2px rgba(108, 99, 255, 0.2);
        }}
        
        /* Sidebar styling */
        .css-1d391kg {{
            background-color: white;
            border-right: 1px solid #f0f0f0;
        }}
        
        /* Success box styling */
        .element-container div[data-testid="stVerticalBlock"] div[style*="background-color: rgb("] {{
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
            padding: 1rem !important;
        }}
        
        /* Dataframe styling */
        .dataframe {{
            border-radius: 10px;
            overflow: hidden;
            border: none !important;
        }}
        
        .dataframe th {{
            background-color: {COLOR_PALETTE["primary"]} !important;
            color: white !important;
            font-weight: 500 !important;
        }}
        
        /* Custom divider */
        .custom-divider {{
            height: 3px;
            background: linear-gradient(90deg, {COLOR_PALETTE["primary"]}, {COLOR_PALETTE["secondary"]}, {COLOR_PALETTE["tertiary"]});
            border-radius: 3px;
            margin: 1.5rem 0;
        }}
        
        /* Card container */
        .card-container {{
            background-color: white;
            border-radius: 15px;
            padding: 1.5rem;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            margin-bottom: 1.5rem;
        }}
        
        /* Feature box */
        .feature-box {{
            background-color: white;
            border-left: 4px solid {COLOR_PALETTE["tertiary"]};
            border-radius: 8px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
        }}
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

def render_gradient_header(title, subtitle):
    """Render a gradient header with optional subtitle"""
    # Create the header HTML
    header_html = f"""
    <div style="text-align: center; padding: 1rem 0;">
        <h1 style="font-size: 2.8rem; font-weight: 700; 
            background: linear-gradient(45deg, {COLOR_PALETTE['primary']}, {COLOR_PALETTE['secondary']}); 
            ">
            {title}
        </h1>
    
    """
    
    # Add a divider
    header_html += f"""
    <div style="height: 3px; width: 500px; margin: 0.5rem auto; 
        background: linear-gradient(45deg, {COLOR_PALETTE['primary']}, {COLOR_PALETTE['secondary']});
        border-radius: 3px;"></div>
    """
    
    # Add subtitle if provided
    if subtitle:
        header_html += f"""<div>
        <p style="color: {COLOR_PALETTE['text']}; font-size: 1.2rem; max-width: 700px; margin: 1rem auto;">
            {subtitle}
        </p>
        """
    
    # Close the container div
    header_html += "</div>"
    
    # Render the HTML
    st.markdown(header_html, unsafe_allow_html=True)

def render_card(content, title=None, icon=None):
    """Render content in a card-like container with optional title and icon"""
    card_html = f"""
    <div class="card-container">
    """
    
    if title:
        icon_html = f'<span style="margin-right: 8px;">{icon}</span>' if icon else ''
        card_html += f"""
        <h3 style="color: {COLOR_PALETTE['primary']}; margin-top: 0; margin-bottom: 1rem; display: flex; align-items: center;">
            {icon_html}{title}
        </h3>
        <div class="custom-divider" style="width: 50px; margin: 0 0 1rem 0;"></div>
        """
    
    card_html += f"""
        <div>{content}</div>
    </div>
    """
    
    st.markdown(card_html, unsafe_allow_html=True)

def render_feature_box(title, content, icon=None):
    """Render a feature box with title, content and optional icon"""
    icon_html = f'<span style="font-size: 1.5rem; margin-right: 10px;">{icon}</span>' if icon else ''
    
    feature_html = f"""
    <div class="feature-box">
        <h4 style="color: {COLOR_PALETTE['tertiary']}; margin-top: 0; display: flex; align-items: center;">
            {icon_html}{title}
        </h4>
        <p style="margin-bottom: 0;">{content}</p>
    </div>
    """
    
    st.markdown(feature_html, unsafe_allow_html=True)

def create_animated_chart_placeholder():
    """Create an animated placeholder while charts are loading"""
    placeholder_html = f"""
    <div style="text-align: center; padding: 2rem;">
        <div style="width: 40px; height: 40px; border: 4px solid {COLOR_PALETTE['neutral']}; 
        border-top: 4px solid {COLOR_PALETTE['primary']}; border-radius: 50%; 
        margin: 0 auto; animation: spin 1s linear infinite;"></div>
        <p style="margin-top: 1rem; color: {COLOR_PALETTE['text']};">Generating visualization...</p>
    </div>
    <style>
        @keyframes spin {{
            0% {{ transform: rotate(0deg); }}
            100% {{ transform: rotate(360deg); }}
        }}
    </style>
    """
    
    return st.markdown(placeholder_html, unsafe_allow_html=True)

def get_emotion_icon(emotion):
    """Get the emoji for a given emotion"""
    emotions_emoji_dict = {
        "anger": "😠", 
        "disgust": "🤮", 
        "fear": "😨", 
        "happy": "🤗", 
        "joy": "😂", 
        "neutral": "😐", 
        "sad": "😔", 
        "sadness": "😔", 
        "shame": "😳", 
        "surprise": "😮"
    }
    return emotions_emoji_dict.get(emotion.lower(), "❓")

def create_altair_theme():
    """Create a custom theme for Altair charts"""
    return {
        'config': {
            'background': 'transparent',
            'view': {
                'strokeWidth': 0,
                'height': 300,
            },
            'title': {
                'font': 'Roboto',
                'fontSize': 16,
                'fontWeight': 'bold',
                'color': COLOR_PALETTE['text'],
            },
            'axisX': {
                'labelFont': 'Roboto',
                'titleFont': 'Roboto',
                'titleFontWeight': 'normal',
                'labelFontSize': 12,
                'titleFontSize': 14,
                'labelColor': COLOR_PALETTE['text'],
                'titleColor': COLOR_PALETTE['text'],
                'labelPadding': 10,
                'labelAngle': 0,
            },
            'axisY': {
                'labelFont': 'Roboto',
                'titleFont': 'Roboto',
                'titleFontWeight': 'normal',
                'labelFontSize': 12,
                'titleFontSize': 14,
                'labelColor': COLOR_PALETTE['text'],
                'titleColor': COLOR_PALETTE['text'],
                'grid': True,
                'gridColor': '#f0f0f0',
                'gridWidth': 1,
            },
            'headerRow': {
                'labelFont': 'Roboto',
                'titleFont': 'Roboto',
            },
            'legend': {
                'labelFont': 'Roboto',
                'titleFont': 'Roboto',
                'labelFontSize': 12,
                'titleFontSize': 14,
                'labelColor': COLOR_PALETTE['text'],
                'titleColor': COLOR_PALETTE['text'],
            },
        }
    }
