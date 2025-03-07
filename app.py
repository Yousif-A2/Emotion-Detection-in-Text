import streamlit as st
import sys
import os

# Add the current directory to the path so Python can find the modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Now import the modules
try:
    from utils.style_utils import set_page_config, apply_custom_styles, COLOR_PALETTE
    from utils.track_utils import create_page_visited_table, create_emotionclf_table
    from pages.home import render_home_page
    from pages.monitor import render_monitor_page
    from pages.about import render_about_page
except ImportError:
    # If the above imports fail, try direct imports
    from style_utils import set_page_config, apply_custom_styles, COLOR_PALETTE
    from track_utils import create_page_visited_table, create_emotionclf_table
    from home import render_home_page
    from monitor import render_monitor_page
    from about import render_about_page

def main():
    """Main application entry point"""
    # Set page configuration and apply custom styles
    set_page_config()
    apply_custom_styles()
    
    # Create database tables if they don't exist
    create_page_visited_table()
    create_emotionclf_table()
    
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
        
        selected_option = None
        
        # Create custom menu buttons
        for option, details in menu_options.items():
            button_style = (
                f"background-color: {COLOR_PALETTE['primary']}; color: white; border-radius: 8px;" 
                if option == st.session_state.get('current_page', 'Home') 
                else f"background-color: transparent; color: {COLOR_PALETTE['text']}; border-radius: 8px;"
            )
            
            menu_html = f"""
            <div style="padding: 0.5rem 1rem; margin-bottom: 0.5rem; cursor: pointer; {button_style}">
                <div style="display: flex; align-items: center;">
                    <span style="font-size: 1.2rem; margin-right: 10px;">{details['icon']}</span>
                    <div>
                        <div style="font-weight: 500;">{option}</div>
                        <div style="font-size: 0.8rem; opacity: 0.8;">{details['description']}</div>
                    </div>
                </div>
            </div>
            """
            
            if st.markdown(menu_html, unsafe_allow_html=True):
                selected_option = option
        
        # Fallback to standard selectbox (the markdown buttons are for visual styling only)
        choice = st.selectbox(
            "Select Page",
            options=list(menu_options.keys()),
            index=list(menu_options.keys()).index(st.session_state.get('current_page', 'Home')),
            label_visibility="collapsed"
        )
        
        # Update session state
        st.session_state['current_page'] = choice
        
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
    
    # Render the selected page
    if choice == "Home":
        render_home_page()
    elif choice == "Monitor":
        render_monitor_page()
    else:  # About
        render_about_page()

if __name__ == '__main__':
    main()