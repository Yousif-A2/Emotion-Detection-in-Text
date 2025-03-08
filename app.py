import streamlit as st
import sys
import os

# Add the current directory to the path so Python can find the modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Now import the modules

from utils.style_utils import set_page_config, apply_custom_styles, COLOR_PALETTE
from utils.track_utils import create_page_visited_table, create_emotionclf_table
from pages.home import render_home_page
from pages.monitor import render_monitor_page
from pages.about import render_about_page

def main():
    """Main application entry point"""
    # Set page configuration and apply custom styles
    set_page_config()
    apply_custom_styles()
    
    # Create database tables if they don't exist
    create_page_visited_table()
    create_emotionclf_table()
    
    # st.markdown("""
    # <style>
    #     [data-testid="stSidebarNav"] {
    #         display: none;  /* Hides sidebar navigation items */
    #     }
    # </style>
    # """, unsafe_allow_html=True)
    hide_streamlit_style = """
        <style>
        
        [data-testid="stSidebarNav"] {
            display: none;  /* Hides sidebar navigation items */
        }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>

        """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

    # Create custom sidebar
    with st.sidebar:
        st.markdown(f"""
        <div style="text-align: center; padding: 1.5rem 0; margin-bottom: 20px;">
            <h1 style="margin: 0; font-size: 1.8rem; background: linear-gradient(45deg, {COLOR_PALETTE['primary']}, {COLOR_PALETTE['secondary']});
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                EmotionSense AI
            </h1>
            <div style="height: 3px; width: 50px; margin: 8px auto; 
            background: linear-gradient(90deg, {COLOR_PALETTE['primary']}, {COLOR_PALETTE['secondary']});
            border-radius: 3px;"></div>
            <p style="margin: 0; font-size: 0.9rem; color: {COLOR_PALETTE['text']};">
                Emotion Detection Platform
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Navigation menu with custom styling
        st.markdown("<p style='font-weight: 500; margin-bottom: 10px;'>Navigation</p>", unsafe_allow_html=True)
        
        # Define menu options with icons
        menu_options = {
            "Home": {"icon": "🏠", "description": "Analyze text emotions"},
            "Monitor": {"icon": "📊", "description": "View analytics"},
            "About": {"icon": "ℹ️", "description": "Learn about the app"}
        }

        # Initialize session state if needed
        if 'current_page' not in st.session_state:
            st.session_state['current_page'] = 'Home'

        # Create custom styled buttons for navigation
        for option, details in menu_options.items():
            # Determine if this option is the active page
            is_active = option == st.session_state.get('current_page', 'Home')
            
            # For active button, just display styled HTML
            if is_active:
                st.markdown(f"""
                <div style="background-color: {COLOR_PALETTE['primary']}; color: white; border-radius: 8px; padding: 0.5rem 1rem; margin-bottom: 0.5rem;">
                    <div style="display: flex; align-items: center;">
                        <span style="font-size: 1.2rem; margin-right: 10px;">{details['icon']}</span>
                        <div>
                            <div style="font-weight: 500;">{option}</div>
                            <div style="font-size: 0.8rem; opacity: 0.8;">{details['description']}</div>
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            # For inactive buttons, use a regular Streamlit button
            else:
                btn_label = f"{details['icon']} {option}"
                if st.button(btn_label, key=f"btn_{option}", use_container_width=True):
                    st.session_state['current_page'] = option
                    st.rerun()  # Rerun the app to update the UI

        # App info section
        st.markdown("""<br>""", unsafe_allow_html=True)
        st.markdown(f"""
        <div style="background-color: {COLOR_PALETTE['background']}; border-radius: 8px; padding: 1rem; margin-top: 2rem;">
            <p style="font-size: 0.8rem; margin-bottom: 0.5rem; font-weight: 500;">About the App</p>
            <p style="font-size: 0.8rem; margin: 0; color: {COLOR_PALETTE['text']}; opacity: 0.8;">
                EmotionSense AI analyzes text to detect emotions using machine learning.
            </p>
            <div style="height: 1px; background-color: #eee; margin: 0.8rem 0;"></div>
            <p style="font-size: 0.8rem; margin: 0; color: {COLOR_PALETTE['text']}; opacity: 0.8;">
                Version 2.0
            </p>
        </div>
        """, unsafe_allow_html=True)
    # Render the selected page based on session state
    if st.session_state['current_page'] == "Home":
        render_home_page()
    elif st.session_state['current_page'] == "Monitor":
        render_monitor_page()
    else:  # About
        render_about_page()

if __name__ == '__main__':
    main()