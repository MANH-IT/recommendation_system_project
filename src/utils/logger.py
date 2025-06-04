# src/utils/logger.py
import logging
import os
from src.utils.config import config  # Import configuration

def setup_logger():
    """
    Function to configure logging to both file and console.
    - Output: Configured logger instance
    """
    # Create logger with name "RecommendationSystem"
    logger = logging.getLogger("RecommendationSystem")
    # Set logging level from config
    logger.setLevel(getattr(logging, config['logging']['level']))

    # Create logs directory if it doesn't exist
    log_dir = os.path.dirname(config['logging']['log_file'])
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)
        print(f"Created directory: {log_dir}")

    # Create file handler for logging to file
    file_handler = logging.FileHandler(config['logging']['log_file'])
    file_handler.setLevel(getattr(logging, config['logging']['level']))

    # Create console handler for logging to console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(getattr(logging, config['logging']['level']))

    # Define log format: time - name - level - message
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Initialize logger for use throughout the project
logger = setup_logger()