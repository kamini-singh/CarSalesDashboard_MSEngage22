import streamlit as st
import utilities.navbar as utl
from pages import car_features, customers,  home_page

st.set_page_config(layout="wide", page_title='Car Data Analysis')
#to hide streamlit deafult hamburger
st.set_option('deprecation.showPyplotGlobalUse', False)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
st.markdown("""
        <style>
               .css-18e3th9 {
                    padding-top: 0rem;
                    padding-bottom: 10rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
               .css-1d391kg {
                    padding-top: 3.5rem;
                    padding-right: 1rem;
                    padding-bottom: 3.5rem;
                    padding-left: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)

utl.inject_custom_css()
utl.navbar_component()


def navigation():
    route = utl.get_current_route()
    if route == "home_page":
        home_page.load_view()
    elif route == "customers":
        customers.load_view()
    elif route == "car_features":
        car_features.load_view()
    elif route == None:
        home_page.load_view()
        
navigation()

