import os

class Config:
    '''
    General configuration of parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://motinga:Access@localhost/pitch_ME'
    DEBUG = True

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


#Add test config here

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
# 'test':TestConfig
}

