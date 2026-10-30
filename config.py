import os
from decouple import config

# Get the absolute path of the directory where this configuration file is located
BASE_DIR = os.path.dirname(os.path.realpath(__file__))


# Base configuration class holding settings common to all environments
class Config:
    # Secret key used for session security (Note: currently set to a literal string instead of using decouple like config('SECRET_KEY'))
    SECRET_KEY=("SECRET_KEY")

# Development configuration class inheriting from the base Config
class DevConfig(Config):
    # Sets the SQLAlchemy database URI to a local SQLite database file located inside a 'database' folder relative to BASE_DIR
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "database/dev.db")

# Production configuration placeholder (inherits from Config, ready for production-specific settings)
class ProdConfig(Config):
    pass

# Testing configuration placeholder (inherits from Config, ready for testing-specific settings)
class TestConfig(Config):
    pass