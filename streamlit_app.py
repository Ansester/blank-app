import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns

st.title("🎈 Data Science App")
st.write("Hello how are you doing. Welcome to my app")

st.sidebar.title("Select Dataset")

st.image("cat.jpg")


##as Data Visualization

app_mode = st.sidebar.selectbox("Select a page",["01 Introduction","02 Data Visualization"])
df = pd.read_csv("dataset.csv")

if app_mode == "01 Introduction":
    st.write("Let's start exploring the dataset")
    df=pd.read_csv("dataset.csv")

    st.dataframe(df.head(5))

    st.markdown("### Statistics summary of the dataset")




    st.dataframe(df.describe())
elif app_mode == "02 Data Visualization":
    st.write("Hello World")
    df=pd.read_csv("dataset.csv")
    sns.bar_chart("")
