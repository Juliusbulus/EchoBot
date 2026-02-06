import os

from config.config import Settings

settings = Settings()

STREAM_ID = settings.youtube.STREAM_ID
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    print(PROJECT_ROOT)
