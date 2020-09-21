from flask import Blueprint, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

import people_web_app.adapters.repository as repo
from people_web_app import Person

people_blueprint = Blueprint(
    'people_bp', __name__
)

class SearchForm(FlaskForm):
    person_id = IntegerField('Person id')
    submit = SubmitField('Find')

@people_blueprint.route('/')
def home():
    return render_template(
        'home.html',
        find_person_url=url_for('people_bp.find_person'),
        list_people_url=url_for('people_bp.list_people')
    )


@people_blueprint.route('/list')
def list_people():
    html_page = render_template('list_people.html', people=repo.repo_instance, person=Person)
    return html_page


@people_blueprint.route('/find', methods=['GET', 'POST'])
def find_person():
    form = SearchForm()

    if form.validate_on_submit():
        try:
            data = request.form.get('person_id.data')
            for person in repo.repo_instance:
                if data in person:
                    match = person
            html_page = render_template('list_person.html', person=Person)
            return html_page



