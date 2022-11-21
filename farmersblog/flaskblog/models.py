from datetime import datetime
from flaskblog import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_manager(user_id):
    return User.query.get(int(user_id))




class User(db.Model, UserMixin):
    id= db.column(db.Integer, primary_key=True)
    username = db.column(db.string(20), unique= True, nullable=  False)
    email = db.column(db.string(120), unique= True, nullable=  False)
    image_file = db.column(db.string(20), nullable=  False, default= 'default.jpg')
    password = db.column(db.string(60), nullable=  False)
    posts= db.relationship('post',backref= 'author', Lazy=True)
    
    def __repr__(self):
        return f"user('{self.username}', '{self.email}', '{self.image_file}')"
    
    
class post(db.Model): 
    id= db.column(db.integer, primary_key=True)
    title= db.column(db.string(100), nullable=  False) 
    date_posted= db.column(db.DateTime, nullable= False, default= datetime.utcnow)
    content= db.column(db.Text, nullable=False)
    user_id= db.column(db.interger, db.Foreignkey('user.id'), nullable= False)
    
    
    def __repr__(self):
        return f"post('{self.title}', '{self.date_posted}')"
    
    
    
    