import pandas as pd
import requests
import streamlit as st
import pickle
import time

st.set_page_config(
    page_title="Movie Recommender System",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded",
)


def fetch_poster(movie_id, retries=3, backoff_factor=0.3):
    your_api_key = "36a3c95f8bc7244e7ebafcf8d9b82dfa"
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={your_api_key}&language=en-US"
    for i in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if 'poster_path' in data and data['poster_path']:
                return "https://image.tmdb.org/t/p/w185/" + data['poster_path']
            else:
                return "https://via.placeholder.com/185"
        except requests.exceptions.RequestException as e:
            if i < retries - 1:
                time.sleep(backoff_factor * (2 ** i))
            else:
                st.error(f"Failed to fetch poster after {retries} attempts. Error: {e}")
                return "https://via.placeholder.com/185"


def recommend(movie):
    index = movie_names[movie_names['title'] == movie].index[0]
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_poster = []
    for j in movies_list:
        movie_id = movie_names.iloc[j[0]].movie_id
        recommended_movies.append(movie_names.iloc[j[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_poster


movies_dict = pickle.load(open('01_Recommender_System/Output_file/movies.pkl', 'rb'))
movie_names = pd.DataFrame(movies_dict)
similarity = pickle.load(open('01_Recommender_System/Output_file/similarity.pkl', 'rb'))

st.sidebar.title("Movie Recommender System")
selected_movie_name = st.sidebar.selectbox("Select a Movie", movie_names['title'].values)

st.title('Find Your Next Favorite Movie')
st.markdown("""
    <style>
    .main-title {
        font-size: 2em;
        font-weight: bold;
        text-align: center;
        color: #1a73e8;
    }
    .sub-title {
        font-size: 1.2em;
        text-align: center;
        margin-top: 0px;
    }
    .sidebar-title {
        color: #1a73e8;
        font-weight: bold;
        font-size: 1.5em;
    }
    .recommend-button {
        background-color: #1a73e8;
        color: white;
        font-weight: bold;
        border-radius: 5px;
        padding: 10px;
        cursor: pointer;
        text-align: center;
    }
    .recommend-button:hover {
        background-color: #0c5ab7;
    }
    </style>
    """, unsafe_allow_html=True)

st.sidebar.markdown("<div class='sidebar-title'>Choose Your Movie</div>", unsafe_allow_html=True)

if st.sidebar.button("Recommend"):
    with st.spinner('Fetching recommendations...'):
        names, posters = recommend(selected_movie_name)
        time.sleep(1)

    st.markdown("<div class='main-title'>Recommended Movies</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>Based on your selection</div>", unsafe_allow_html=True)

    col1, col2, col3, col4, col5 = st.columns(5)

    style = """
    <style>
    .movie-title {
        font-size: 13px;
        font-weight: 600;
        text-align: center;
        margin-top: 5px;
        margin-bottom: 10px;
    }
    .movie-poster {
        border-radius: 8px;
    }
    .stImage {
        display: flex;
        justify-content: center;
    }
    .stImage img {
        max-height: 300px;
        border: 2px solid #1a73e8;
        box-shadow: 0px 4px 8px rgba(0,0,0,0.2);
    }
    .movie-genre {
        font-size: 12px;
        color: #757575;
        text-align: center;
        margin-bottom: 10px;
    }
    </style>
    """
    st.markdown(style, unsafe_allow_html=True)

    for idx, col in enumerate([col1, col2, col3, col4, col5]):
        with col:
            st.markdown(f"<div class='movie-title'>{names[idx]}</div>", unsafe_allow_html=True)
            st.image(posters[idx], use_column_width=True, output_format='PNG')
            st.markdown(f"<div class='movie-genre'>Genre: Action, Drama</div>", unsafe_allow_html=True)

st.markdown("""
    <hr style="border:1px solid #f5f5f5">
    <footer>
    <p style="text-align:center;font-size:12px;color:grey;">
        © 2024 Movie Recommender | Powered by Streamlit | Designed by Dilesh Bisen
    </p>
    </footer>
    """, unsafe_allow_html=True)
