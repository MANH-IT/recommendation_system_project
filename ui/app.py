import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Add root directory to Python Path

import streamlit as st
from src.data.data_loader import DataLoader
from src.data.preprocessor import Preprocessor
from src.models.collaborative_filtering import CollaborativeFiltering
from src.utils.logger import logger

# Load data and model
logger.info("Initializing web interface")
loader = DataLoader()
ratings_df = loader.load_ratings()
movies_df = loader.load_movies()
preprocessor = Preprocessor(ratings_df)
user_movie_matrix = preprocessor.create_user_movie_matrix()
model = CollaborativeFiltering(user_movie_matrix)
model.load_model()

# Web interface
st.title("Movie Recommendation System")
st.write("Current date: June 04, 2025")

# Movie-based recommendations
st.subheader("Similar Movie Recommendations")
movie_id = st.number_input("Enter movieId (e.g., 1 for Toy Story)", min_value=1)
num_recommendations = st.slider("Number of recommendations", 1, 10, 5)
if st.button("Recommend by Movie"):
    logger.info(f"User requested recommendations for movieId={movie_id}")
    recommendations = model.recommend_movies(movie_id, movies_df, num_recommendations)
    st.write("Recommended movies:")
    st.dataframe(recommendations)

# User preference-based recommendations
st.subheader("Recommendations Based on Preferences")
user_ratings_input = st.text_input("Enter movieId:rating (e.g., 1:5, 2571:4), separated by commas")
if user_ratings_input:
    user_ratings = {}
    for item in user_ratings_input.split(','):
        try:
            movie_id, rating = map(float, item.split(':'))
            user_ratings[int(movie_id)] = rating
        except:
            st.error("Invalid format, example: 1:5, 2571:4")
    if st.button("Recommend by Preferences"):
        logger.info("User requested recommendations based on preferences")
        recommendations = model.recommend_for_user(user_ratings, movies_df, num_recommendations)
        st.write("Recommendations based on preferences:")
        st.dataframe(recommendations)