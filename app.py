
import plotly.express as px
import pandas as pd
from statistics import mean,stdev
import plotly.graph_objects as go
from copy import deepcopy
import os
import json
from statistics import mean, stdev,median
from datetime import date,timedelta
from os import listdir

import streamlit as st
from multiapp import MultiApp
from apps import chile, france

def indexx(x):
    x.index=range(len(x))
    return x


st.set_page_config(page_title='Eventos en el futbol 🤴',
	              page_icon='🤴',
	              layout='wide' )

app = MultiApp()
# df=pd.read_excel('chilean_teams.xlsx', engine='openpyxl')
# df1=pd.read_excel('data_football_chile.xlsx',dtype={'result':object}, engine='openpyxl')
# position=pd.read_excel('chilean_position.xlsx', engine='openpyxl')
# del df1['result']
# df1=df1.dropna()


#st.markdown("""
## Multi-Page App
#This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps)
#framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar).
# Also check out his [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4).
#""")

st.markdown("""
# Partidos en en el mundo.
""")



# Add all your application here
app.add_app("Chile", chile.app)
app.add_app("Francia", france.app)

# The main app
app.run()
