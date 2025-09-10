# config.py
"""
Configuration file for the Multi-Source Data Analysis Agent
"""

# API Settings
OPENAI_MODEL = "gpt-3.5-turbo"
MAX_TOKENS = 500

# Data Processing Settings
MAX_ROWS_DISPLAY = 1000
MAX_FILE_SIZE_MB = 50

# Visualization Settings
DEFAULT_COLOR_PALETTE = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD', '#98D8C8']
MAX_CHARTS_AUTO = 5

# Database Settings (for future expansion)
SQLITE_DB_PATH = "data/analysis.db"

# API Endpoints (for future expansion)
SAMPLE_APIS = {
    "weather": "https://api.openweathermap.org/data/2.5/weather",
    "quotes": "https://api.quotable.io/random",
    "jokes": "https://official-joke-api.appspot.com/random_joke"
}

# File Paths
DATA_FOLDER = "data/"
TEMP_FOLDER = "temp/"

# Error Messages
ERROR_MESSAGES = {
    "no_api_key": "Please provide your OpenAI API key to use AI features",
    "no_data": "Please upload data first",
    "file_too_large": f"File size exceeds {MAX_FILE_SIZE_MB}MB limit",
    "unsupported_format": "Unsupported file format",
    "api_error": "Error connecting to API"
}
