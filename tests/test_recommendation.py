import unittest
from src.data.data_loader import DataLoader
from src.data.preprocessor import Preprocessor
from src.models.collaborative_filtering import CollaborativeFiltering

class TestRecommendation(unittest.TestCase):
    """
    Class to test the recommendation functionality.
    """
    def setUp(self):
        # Set up data and model before each test
        loader = DataLoader()
        ratings_df = loader.load_ratings()
        movies_df = loader.load_movies()
        preprocessor = Preprocessor(ratings_df)
        self.user_movie_matrix = preprocessor.create_user_movie_matrix()
        self.movies_df = movies_df
        self.model = CollaborativeFiltering(self.user_movie_matrix)
        self.model.train()

    def test_recommend_movies(self):
        """
        Test the recommend_movies function.
        - Verifies the correct number of recommendations is returned
        """
        recommendations = self.model.recommend_movies(1, self.movies_df, num_recommendations=5)
        self.assertEqual(len(recommendations), 5)

if __name__ == '__main__':
    unittest.main()