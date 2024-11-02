import streamlit as st
from streamlit_option_menu import option_menu
import home , about 

class Main :
    def __init__(self):
        self.apps = []
    def add_apps(self,title,function):
        self.apps.append({
            'title' : title , 
            'function' : function
        })
    def run():
        with st.sidebar:
            app = option_menu(
                menu_title='Medical Cost',
                menu_icon = 'heart-pulse',
                options = ['home' , 'about us'],
                icons = ['house-fill','info-circle-fill'],
                default_index=0 , 
                styles = {
                    "Container":{'Padding':'5!important','background-color' : 'blue'},
                        'icon':{'font-size' : '25px'},
                        'nav-link':{'font-size':'20px','text-align':'left','margin':'0px','--hover-color':'blue'},
                        'nav-link-selected':{'background-color':'red'}} 
            )
        if app == 'home':
            home.app()
        if app == 'about us':
            about.app()
    run()