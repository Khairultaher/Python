import os
import urllib.parse 

class Config(object):
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    # Configure Database URI: 
    connectionString = urllib.parse.quote_plus("DRIVER={SQL Server};SERVER=serverNameOrIP;DATABASE=databaseName;UID=user;PWD=123")
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect=%s" % connectionString 
    SQLALCHEMY_ECHO = True

