# src/main.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Add root directory to Python Path

from src.data.data_loader import DataLoader
from src.data.preprocessor import Preprocessor
from src.models.collaborative_filtering import CollaborativeFiltering
from src.utils.logger import logger

def main():
    """
    Main function to run the recommendation system.
    - Loads data
    - Loads or trains the model
    - Provides example recommendations
    """
    logger.info("Starting recommendation system")
    
    # Load data
    loader = DataLoader()
    ratings_df = loader.load_ratings()
    movies_df = loader.load_movies()
    
    # Preprocess data
    preprocessor = Preprocessor(ratings_df)
    user_movie_matrix = preprocessor.create_user_movie_matrix()
    
    # Load or train model
    model = CollaborativeFiltering(user_movie_matrix)
    try:
        model.load_model()
    except FileNotFoundError:
        logger.warning("Model not found, training new model")
        model.train()
    
    # Example recommendations
    logger.info("Example recommendations")
    print("Movies similar to movieId=1 (Toy Story):")
    print(model.recommend_movies(1, movies_df))
    
    user_ratings = {1: 5.0, 2571: 4.0}  # User likes Toy Story (5) and The Matrix (4)
    print("\nRecommendations for user with preferences (Collaborative Filtering):")
    print(model.recommend_for_user(user_ratings, movies_df))

if __name__ == "__main__":
    main()