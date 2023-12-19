import streamlit as st
from streamlit_option_menu import option_menu
import about,homepage,mains,sugg 
st.set_page_config(
    page_title="Delusional World",
    layout="wide",
)
class MultiApp:
    def __init__(self):
        self.apps=[]
    def add_app(self,title,function):
        self.apps.append({
            "title":title,
            "function":function
        })    
    def run():
        with st.sidebar:
            app=option_menu(
                menu_title='WANDER HERE',
                options=['Home','About','App','Suggestions'],
                menu_icon='cast',
                icons=['house','exclamation-circle-fill','phone','phone'],
                default_index=0,
                styles={
                    "container": {"padding": "0!important", "background-color": "#000000"},
        "icon": {"color": "blueviolet", "font-size": "25px"}, 
        "nav-link": {"font-size": "20px", "text-align": "left", "margin":"5px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "yellow"},
                }


            )    
        if app=='Home':
            homepage.app()
        if app=='About':
            about.app()
        if app=='App':
            mains.app()   
        if app=='Suggestions':
            sugg.app()           
    run()                 
              
