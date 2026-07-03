
import pickle
import streamlit as st
import pandas as pd
import requests
from urllib.parse import quote
import gdown
import os

# -------------------- Fetch Poster --------------------
def fetch_poster(movie_title):
    url = f"https://www.omdbapi.com/?t={quote(str(movie_title))}&apikey=76c6d4e0"

    try:
        response = requests.get(url)
        data = response.json()

        if data.get("Response") == "True":
            return (
                data.get("Poster", "https://placehold.co/500x750?text=No+Poster"),
                data.get("Year", "N/A"),
                data.get("imdbRating", "N/A"),
            )

    except Exception as e:
        st.error(f"Error: {e}")

    return (
        "https://placehold.co/500x750?text=No+Poster",
        "N/A",
        "N/A",
    )


# -------------------- Recommendation --------------------
def recommend(movie):

    index = movies[movies["title"] == movie].index[0]

    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1],
    )

    names = []
    posters = []
    years = []
    ratings = []

    for i in distances[1:6]:

        title = movies.iloc[i[0]]["title"]

        poster, year, rating = fetch_poster(title)

        names.append(title)
        posters.append(poster)
        years.append(year)
        ratings.append(rating)

    return names, posters, years, ratings


# -------------------- Load Data --------------------
st.header("🎬 Movie Recommendation System")

movies = pickle.load(open("artificats/movi_list.pkl", "rb"))
# similarity = pickle.load(open("artificats/similarity.pkl", "rb"))
if not os.path.exists("artificats/similarity.pkl"):
    url = "https://drive.google.com/file/d/1KVctN_w0h48x3OuculhmlO48yWYQUZmw/view?usp=drive_link"
    gdown.download(url, "artificats/similarity.pkl", quiet=False)

similarity = pickle.load(open("artificats/similarity.pkl", "rb"))

movie_list = movies["title"].values

selected_movie = st.selectbox(
    "Select a movie",
    movie_list,
)

# -------------------- Show Recommendation --------------------
if st.button("Show Recommendation"):

    with st.spinner("Finding movies..."):

        names, posters, years, ratings = recommend(selected_movie)

    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.image(posters[i])
            st.write(f"**{names[i]}**")
            st.caption(f"Year : {years[i]}")
            st.caption(f"IMDb : ⭐ {ratings[i]}")