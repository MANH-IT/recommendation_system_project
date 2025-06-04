# src/train.py
import sys
import os

# Thêm thư mục gốc của dự án vào Python Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Bây giờ Python sẽ tìm thấy package 'src'

from src.data.data_loader import DataLoader
from src.data.preprocessor import Preprocessor
from src.models.collaborative_filtering import CollaborativeFiltering
from src.utils.logger import logger

def train():
    logger.info("Bắt đầu huấn luyện mô hình")
    
    # Tải dữ liệu
    loader = DataLoader()
    ratings_df = loader.load_ratings()
    
    # Tiền xử lý
    preprocessor = Preprocessor(ratings_df)
    user_movie_matrix = preprocessor.create_user_movie_matrix()
    
    # Huấn luyện mô hình
    model = CollaborativeFiltering(user_movie_matrix)
    model.train()

if __name__ == "__main__":
    train()