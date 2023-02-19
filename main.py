import logging
import os

from flask import Flask

import core
from api.api import api
from database.db_session import db, migration
# from flask_script import Manager

# from app.main.logging import LOGGING_CONFIG

# Flask App Initialization
app = Flask(__name__)
app.config.from_object(core.settings[os.environ.get('APPLICATION_ENV', 'default')])

# Logs Initialization
console = logging.getLogger('console')

# Database ORM Initialization
db.init_app(app)

# Database Migrations Initialization
migration.init_app(app, db)

# Flask API Initialization
api.init_app(app)

# manager = Manager(app)

if __name__ == '__main__':
    app.run()
