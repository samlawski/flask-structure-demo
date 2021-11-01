from flask_login import LoginManager
from app.authentication.models import User

login_manager = LoginManager()
login_manager.login_view = 'authentication.login'

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)