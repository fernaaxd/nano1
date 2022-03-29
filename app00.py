import plotly.express as px
import streamlit as st
import pandas as pd
from statistics import mean,stdev
import plotly.graph_objects as go
from copy import deepcopy

import json
from statistics import mean, stdev,median
from datetime import date,timedelta
def indexx(x):
    x.index=range(len(x))
    return x

st.set_page_config(page_title='Nano Team',
	              page_icon=':soccer:',
	              layout='wide' )

df=pd.read_excel('chilean_teams.xlsx', engine='openpyxl')
df1=pd.read_excel('data_football_chile.xlsx',dtype={'result':object}, engine='openpyxl')
position=pd.read_excel('chilean_position.xlsx', engine='openpyxl')
del df1['result']
df1=df1.dropna()


PASS = st.text_input("", 'hola')

if PASS=='hola0':


    #'''SIDE BAR'''
    st.sidebar.header('Filtros por equipo')
    equipo=st.sidebar.multiselect(
        'Selecciona a tu equipo:', 
        options=df['team_name'].unique(),
        default=['Colo Colo','Palestino','Nublense']
        )



    df_selection = df1.query(
          'team_name == @equipo' )
    st.dataframe(df_selection)


    # MAIN PAGE
    st.title(':alien: Estadisticas del equipo')
    st.markdown('##')

    # TOP KPI's
    partidos_ganados = len(df_selection[df_selection.points==3])
    partidos_empatados = len(df_selection[df_selection.points==1])
    partidos_perdidos = len(df_selection[df_selection.points==0])

    puntos_promedio_por_partido= ':star:'*round(mean(df_selection.points))


    left_column, middle_column, right_colum = st.columns(3)

    with left_column:
        st.subheader('Partidos Ganados:')
        st.subheader(  f'{partidos_ganados:,}'  )
    with middle_column:
        st.subheader('Partidos Empatados:')
        st.subheader(  f'{partidos_empatados}'  )
    with right_colum:
        st.subheader('Partidos Perdidos:')
        st.subheader(  f'{partidos_perdidos}'  )
    st.markdown('---')

    fig = go.Figure()

    for k,team in enumerate(df_selection.team_name.unique()):
     color=indexx(position[position.team_name==team]).loc[0,'color']   
     if k<=40:
        df_team=indexx(df1[df1.team_name==team])
        fig.add_trace(go.Scatter(
            x=['Fecha '+str(j+1) for j in df_team.index],
            y=list( df_team.acumulate_points  ),
            mode="lines",
            name=team,
            line=dict(color=color)

        ))

    fig.update_traces(mode='lines')

    st.plotly_chart(fig)

