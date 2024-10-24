import pandas as pd
import sqlalchemy
import streamlit as st

st.title('Cache ressource')
st.caption('cliquez sur le tableau')

@st.cache_resource
def get_db_sessionmaker():
    engine = sqlalchemy.create_engine('sqlite:////Users/adriencombes/Desktop/lecture_streamlit/streamlit_db.sqlite')
    return engine

@st.cache_data
def fetch_data():
    return pd.read_sql('SELECT * FROM test', get_db_sessionmaker())


data = fetch_data()
selected_data = st.dataframe(data,width=500,selection_mode="single-row")
st.text(selected_data)
