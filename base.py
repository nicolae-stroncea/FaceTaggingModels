from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from api.config import config
import os
# https://stackoverflow.com/questions/30115010/using-flask-sqlalchemy-without-flask
app_type = os.getenv("APP_TYPE")
# check type of app. If FLASK_APP, then db connection will be instantiated by app
# otherwise instantiate it with proper settings.
if app_type == "FLASK_APP":
    print("inside Flask App.")
    db = SQLAlchemy() #instantiate db obj
else:
    print("Not in Flask App. Generating SQLALCHEMY configurations.")
    env = os.getenv("FLASK_ENV")
    test_app = Flask('test_app')
    test_app.config['SQLALCHEMY_DATABASE_URI'] = config[env].SQLALCHEMY_DATABASE_URI
    test_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config[env].SQLALCHEMY_TRACK_MODIFICATIONS
    metadata = MetaData()
    db = SQLAlchemy(test_app, metadata=metadata)
