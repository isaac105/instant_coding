# -*- coding: utf-8 -*-

from sqlalchemy.pool import NullPool

import json
import os


def get_secret():
    if os.path.exists('.credentials'):
        with open('.credentials') as fp:
            return json.load(fp)
    else:
        raise Exception('cannot find credentials')


class Config(object):
    config = get_secret()

    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = config["secret_key"]
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}".format(**config["db"])
    SQLALCHEMY_ENGINE_OPTIONS = {"poolclass": NullPool}
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False
    SQLALCHEMY_ECHO = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = False
    SQLALCHEMY_ECHO = True
