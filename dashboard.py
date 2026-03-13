import streamlit as st
import sqlite3
import pandas as pd

conn=sqlite3.connect("data/traders.db")

df=pd.read_sql("SELECT * FROM traders",conn)

st.title("Binance P2P Guardian Dashboard")

st.dataframe(df)