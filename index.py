<<<<<<< HEAD
import streamlit as st
import sklearn
import joblib
import numpy as np
from textblob import TextBlob
import pandas as pd
import altair as alt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def index():
    st.title("Sentiment Analysis on Review on Sociolla")
    st.subheader("Tugas Akhir Aplikasi Web")
    st.write("Sentiment Analysis on Review on Sociolla")
    st.markdown("dashboard")
    st.sidebar("dashboard")

def page1():
    st.markdown("hal analisis sentimen")
=======
import streamlit as st
import sklearn
import joblib
import numpy as np
from textblob import TextBlob
import pandas as pd
import altair as alt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# def main() :
#     st.title("Sentiment Analysis on Review on Sociolla")
#     st.subheader("Web App Major")

#     menu = ["page1", "Dashboard"]
#     choice = st.sidebar.selectBox("Dashboard", dashboard)

#     if choice == "Dashboard":
#         st.subheader("Dashboard")
#         with st.form("nlpForm"):
#             raw_text = st.text_area("")

def index():
    st.title("Sentiment Analysis on Review on Sociolla")
    st.subheader("Tugas Akhir Aplikasi Web")
    st.write("Sentiment Analysis on Review on Sociolla")
    st.markdown("dashboard")
    st.sidebar("dashboard")

def page1():
    st.markdown("hal analisis sentimen")
>>>>>>> c4775b48ea1c664d7f366f7e7216c059b5beed4a
    st.sidebar("dashboard")