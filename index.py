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
    st.sidebar("dashboard")