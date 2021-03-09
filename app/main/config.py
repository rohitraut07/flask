""" Flask Configuration """
from os import environ
import logging


class Config:
    """
    Base Config File
    """
    TESTING = True
    DEBUG = True
    ENV = 'development'
    DATABASE_USER = environ.get("DATABASE_USER")
    DATABASE_NAME = environ.get("DATABASE_NAME")
    DATABASE_PASSWORD = environ.get("DATABASE_PASSWORD")
    DATABASE_URI = environ.get("DATABASE_URL")
    DATABASE_PORT = environ.get("DATABASE_PORT")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """
    Development Configuration
    """
    TESTING = True
    DEBUG = True
    ENV = 'development'
    DATABASE_USER = 'postgres'
    DATABASE_NAME = 'mydb3'
    DATABASE_PASSWORD = '3366'
    DATABASE_URI = '127.0.0.1'
    DATABASE_PORT = 5432
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_FILE = "app.log"
    LOG_TYPE = logging.DEBUG
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_URI}:{DATABASE_PORT}/{DATABASE_NAME}"


class ProductionConfig(Config):
    """
    Production Environment Config FIle Configuration
    Environment Required Variable:
        variable         :     operation                 :      example
    ==================================================================================================================
        DATABASE_USER    : export user name              :       "root"
        DATABASE_NAME    : export name                   :       "mydb"
        DATABASE_PASSWORD: export DATABASE_USER password :       "xyz"
        DATABASE_URI     : export database URI            :       dialect+driver://username:password@host:port/database
        DATABASE_PORT    : export port                   :       "5432"
    ==================================================================================================================
    """
    TESTING = False
    DEBUG = False
    ENV = 'production'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATABASE_USER = environ.get("DATABASE_USER")
    DATABASE_NAME = environ.get("DATABASE_NAME")
    DATABASE_PASSWORD = environ.get("DATABASE_PASSWORD")
    DATABASE_URI = environ.get("DATABASE_URI")
    DATABASE_PORT = environ.get("DATABASE_PORT")
    LOG_FILE = "app.log"
    LOG_TYPE = logging.DEBUG
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_URI}:{DATABASE_PORT}/{DATABASE_NAME} "


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
