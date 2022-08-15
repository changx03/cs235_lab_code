from flask import Blueprint, redirect, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

from app.adapters.repository import people_repo

people_blueprint = Blueprint('people_blueprint', __name__)


@people_blueprint.route('/')
def home():
    # Demo: Render our home page.
    return render_template('home.html')


@people_blueprint.route('/people')
def list_people():
    # Task 1: Render the `people_list.html` template. It takes `people` as a variable.
    return 'Not implemented yet!'


@people_blueprint.route('/people/<int:person_id>')
def person_view(person_id):
    for person in people_repo:
        if person.id == person_id:
            # Task 1: Render the `people_view.html` template. It takes `img_url`,
            # 'firstname' and 'lastname' as variables.
            return 'Not implemented yet!'
    return render_template('404.html')


@people_blueprint.route('/find', methods=['GET', 'POST'])
def find_person():
    # Task 3: Complete this method
    form = SearchForm()
    if form.validate_on_submit():
        # TODO: Read id from the form and redirect to `people_blueprint.person_view`
        return 'Not implemented yet!'
    else:
        # TODO: Render the `people_search.html` template. It takes `form` and
        # `handler_url` as parameters.
        return 'Not implemented yet!'


class SearchForm(FlaskForm):
    # Task 2: Define the variables below using IntegerField and SubmitField
    id = None
    submit = None
