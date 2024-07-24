import os

class Config:
    """Base configuration class."""
    
    # Flask secret key for signing cookies
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key')

    # SQLAlchemy settings
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///your-database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Other Flask settings can be added here
    # Example:
    # FLASK_ENV = os.environ.get('FLASK_ENV', 'development')
    # DEBUG = os.environ.get('DEBUG', True)

# Configuration for development environment
class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    SQLALCHEMY_ECHO = True  # Print SQL queries to the console

# Configuration for testing environment
class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # Use in-memory database for tests

# Configuration for production environment
class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    # Production-specific settings can be added here

# Dictionary to access the configurations
CONFIGS = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}

# Set the default configuration to 'development'
current_config = CONFIGS.get(os.environ.get('FLASK_ENV', 'development'))
