from app.extensions.database import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(120), unique=True)
  password = db.Column(db.String(120))

  def save(self):
    db.session.add(self)
    db.session.commit()
  
  def delete(self):
    db.session.delete(self)
    db.session.commit()
  
  def check_password(self, password):
    return self.password == password