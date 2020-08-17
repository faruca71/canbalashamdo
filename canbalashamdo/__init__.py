# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 13:04:28 2020
@author: fabio
Da inicio al modulo views
"""

from flask import Flask
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = '7110cfae51a4b5bf97be6534caef9ae4bb9bdcb33i80af008f90b2oa5d1616bf3'
login_manager = LoginManager()
login_manager.init_app(app) # app is a Flask object
login_manager.login_view = "login"


import canbalashamdo.views

