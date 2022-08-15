import json
import os
from pathlib import Path

from flask import Flask
from flask_wtf.csrf import CSRFProtect

import app.adapters.repository as repository
from app.models.person import Person


def load_data():
    path_root = Path(os.getcwd()).absolute()
    path_data = os.path.join(path_root, 'nz_data.json')
    people = []
    with open(path_data) as file:
        data = json.loads(file.read())
        for row in data:
            people.append(
                Person(row['id'],
                       row['first_name'],
                       row['last_name'],
                       row['source']
                       ))
    print(f'The pseudo database contains {len(people)} people.')
    return people


def create_app():
    app = Flask(__name__)

    # Apply the CSRFProtect extension
    csrf = CSRFProtect()
    csrf.init_app(app)

    # Load configuration from `config.py`
    app.config.from_object('config.DevConfig')

    # Load data
    people = load_data()
    repository.people_repo = repository.PeopleRepository(*people)

    with app.app_context():
        from app.blueprints.people_blueprint import people_blueprint
        app.register_blueprint(people_blueprint)

    return app
