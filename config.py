from pydantic import BaseSettings
from functools import lru_cache

# Create subclass of BaseSettings called Settings to create env variables
class Settings(BaseSettings):
    env_name: str = 'Local'
    base_url: str = 'http://localhost:8000'
    db_url: str = 'sqlite:///./shortner.db'

    # 
    # create subclass to load .env file to adjust settings per environment
    #Loads in development env
    #
    class Config:
        env_file = '.env'

# 
# Function returns instances of Settings class to provide caching options
# Add LRU cache stragey with functools using lru_cache decorator for get_settings function
# decortator shows loading setting only once and not for each setting 
# decreases load on compute resources 
#
@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f"### Loading settings for: {settings.env_name}")
    return settings

