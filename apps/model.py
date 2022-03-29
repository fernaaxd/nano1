import streamlit as st
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report


import plotly.express as px
import pandas as pd
from statistics import mean,stdev
import plotly.graph_objects as go
from copy import deepcopy

import json
from statistics import mean, stdev,median
from datetime import date,timedelta

import streamlit as st
from multiapp import MultiApp
from apps import home, data, model # import your app modules here

def indexx(x):
    x.index=range(len(x))
    return x


df=pd.read_excel('chilean_teams.xlsx', engine='openpyxl')
df1=pd.read_excel('data_football_chile.xlsx',dtype={'result':object}, engine='openpyxl')
position=pd.read_excel('chilean_position.xlsx', engine='openpyxl')
del df1['result']
df1=df1.dropna()

def app():
    st.title('Model')

    st.write('This is the `Model` page of the multi-page app.')

    st.write('The model performance of the Iris dataset is presented below.')

    # Load iris dataset
    iris = datasets.load_iris()
    X = iris.data
    Y = iris.target

    # Model building
    st.header('Model performance')
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier()
    clf.fit(X_train, Y_train)
    score = clf.score(X_test, Y_test)
    st.write('Accuracy:')
    st.write(score)
