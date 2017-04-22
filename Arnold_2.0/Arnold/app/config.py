from common.constants import INSTANCE_FOLDER_PATH
import os

class BaseConfig(object):
    PROJECT = 'app'

    # Get app root path
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

    DEBUG = False
    TESTING = False

    ADMINS = ['deborahvenuti93@gmail.com']

    SECRET_KEY = '\\xdb\\x13\\x11\\xc9\\x98HH\\xf8\\xcd\\x1b\\x13W\\x10!JP\\xb4N\\xd0\\xa1d\\xb2\\x97\\xad'

class DefaultConfig(BaseConfig):
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    SECRET_KEY = 'boy o boy yet another secret key'

class LocalConfig(DefaultConfig):
    """ Configure local development environment. """
    pass

class StagingConfig(DefaultConfig):
    """ Configure staging environment. """
    pass

class ProdConfig(DefaultConfig):
    """ Configure production environment. """
    pass

def get_config(MODE):
    SWITCH = {
        'LOCAL': LocalConfig,
        'STAGING': StagingConfig,
        'PRODUCTION': ProdConfig
    }
    return SWITCH[MODE]
