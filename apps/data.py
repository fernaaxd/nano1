import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets
df = pd.read_excel('chilean_teams.xlsx', engine='openpyxl')
df1=pd.read_excel('data_football_chile.xlsx',dtype={'result':object}, engine='openpyxl')
position=pd.read_excel('chilean_position.xlsx', engine='openpyxl')
del df1['result']
df1=df1.dropna()

def app():

    #'''SIDE BAR'''
    st.sidebar.header('Filtros por equipo')
    equipo=st.sidebar.multiselect(
        'Selecciona a tu equipo:', 
        options=['Colo Colo','Palestino','Nublense'],
        default=['Colo Colo']
        )
    df1=pd.read_excel('data_football_chile.xlsx',dtype={'result':object}, engine='openpyxl')
    del df1['result']
    st.dataframe(df1)

    st.title('Data')

    st.write("This is the `Data` page of the multi-page app.")

    st.write("The following is the DataFrame of the `iris` dataset.")

    iris = datasets.load_iris()
    X = pd.DataFrame(iris.data, columns = iris.feature_names)
    Y = pd.Series(iris.target, name = 'class')
    df = pd.concat([X,Y], axis=1)
    df['class'] = df['class'].map({0:"setosa", 1:"versicolor", 2:"virginica"})

    st.write(df)
