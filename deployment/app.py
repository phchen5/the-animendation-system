import pickle
import pandas as pd
import streamlit as st
from streamlit import session_state as session

with open("data/anime_title_list.pkl", "rb") as f:
    animes = pickle.load(f)

@st.cache(persist=True, show_spinner=False, suppress_st_warning=True)
def load_data():
    """
    load and cache data
    :return: tfidf data
    """
    cosine_sim_content = pd.read_csv("../data/cosine_sim_content.csv", index_col=0)
    return cosine_sim_content

def get_recommendations(title, cosine_sim):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    anime_indices = [i[0] for i in sim_scores]
    return anime_features['Name'].iloc[anime_indices]


dataframe = None

st.title("""
Anime Recommendation System
This is an Content Based Recommender System.
 """)


selected_anime = st.selectbox(label="Select an Anime", options=animes)

session.slider_count = st.slider(label="anime_count", min_value=5, max_value=50)

buffer1, col1, buffer2 = st.columns([1.45, 1, 1])

is_clicked = col1.button(label="Recommend")

if is_clicked:
    dataframe = get_recommendations(selected_anime, cosine_sim_content)

if dataframe is not None:
    st.table(dataframe)