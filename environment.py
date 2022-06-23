import os
import shutil
import time
from helpers.helper_web import get_browser
from configparser import ConfigParser


def before_all(context):
    config = ConfigParser()
    """ get the Browse variable in the behave.ini"""
    behave_path = (os.path.join(os.getcwd(), 'behave.ini'))
    config.read(behave_path)

    """ Read and user the variable"""
    helper_func = get_browser(config.get('Environment', 'Browser'))
    context.helperfunc = helper_func


def after_all(context):
    context.helperfunc.close()
