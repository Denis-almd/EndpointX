
from front import sidebar_manager as sm
import streamlit as st

class MainContent:
    
    st.set_page_config(
        page_title="EndpointX", 
        layout="wide", 
        initial_sidebar_state="expanded"
        )
    
    def __init__(self):
        self.sidebar = sm.SidebarManager()
        
    def render(self):
        self.render_sidebar()
        
    def render_sidebar(self):
        self.sidebar.render_sidebar()
    
        
if __name__ == "__main__":
    print(__file__)  # This will print: front/main_content.py