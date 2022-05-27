from pydantic import BaseSettings

# Create subclass of BaseSettings called Settings to create env variables
class Settings(BaseSettings):
    env_name: str = 'Local'
    base_url: str = 'http://localhost:8000'
    db_url: str = 'sqlite:///./shortner.db'

# 
# Function returns instances of Settings class to provide caching options
#
def get_settings() -> Settings:
    settings = Settings()
    print(f"### Loading settings for: {settings.env_name}")
    return settings

