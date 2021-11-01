from flask import Blueprint
from flask.templating import render_template
from flask_login import login_required

blueprint = Blueprint('simple_pages', __name__)

@blueprint.route('/')
@login_required
def index():
  return render_template('simple_pages/index.html')

@blueprint.route('/about')
def about():
  return '<h1>About</h1>'