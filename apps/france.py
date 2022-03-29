import streamlit as st


import plotly.express as px
import pandas as pd
from statistics import mean,stdev
import plotly.graph_objects as go
from copy import deepcopy
import os
import json
from statistics import mean, stdev,median
from datetime import date,timedelta


import numpy as np

import streamlit as st
from multiapp import MultiApp
from apps import chile,france # import your app modules here
from PIL import Image

def indexx(x):
    x.index=range(len(x))
    return x



df=pd.read_excel('chilean_teams.xlsx', engine='openpyxl')
df1=pd.read_excel('data_football_chile.xlsx',dtype={'result':object}, engine='openpyxl')
position=pd.read_excel('chilean_position.xlsx', engine='openpyxl')
del df1['result']
df1=df1.dropna()

def app():
    #'''SIDE BAR'''
    files = os.listdir( './France/Ligue 1' )
    st.title(  'Francia'  )
    for ff in files:
        st.subheader(ff, anchor=None)
        # st.write(os.getcwd())
        image = Image.open('./France/Ligue 1/'+ff)
        st.image(image, caption=ff)
        st.markdown('##')
    # st.sidebar.header('Filtros por equipo')
    # equipo=st.sidebar.multiselect(
    #     'Selecciona a tu equipo:', 
    #     options = files,
    #     default = files[0:2]
    #     )
    # df_selection = df1.query(
    #       'team_name == @equipo' )
    # st.dataframe(df_selection)


    # # MAIN PAGE
    # st.title(':alien: Estadisticas del equipo')
    # st.markdown('##')

    # # TOP KPI's
    # partidos_ganados = len(df_selection[df_selection.points==3])
    # partidos_empatados = len(df_selection[df_selection.points==1])
    # partidos_perdidos = len(df_selection[df_selection.points==0])

    # puntos_promedio_por_partido= ':star:'*round(mean(df_selection.points))


    # left_column, middle_column, right_colum = st.columns(3)

    # with left_column:
    #     st.subheader('Partidos Ganados:')
    #     st.subheader(  f'{partidos_ganados:,}'  )
    # with middle_column:
    #     st.subheader('Partidos Empatados:')
    #     st.subheader(  f'{partidos_empatados}'  )
    # with right_colum:
    #     st.subheader('Partidos Perdidos:')
    #     st.subheader(  f'{partidos_perdidos}'  )
    # st.markdown('---')


    # st.plotly_chart(fig)
    
