from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, validationError
from flaskblog.models import User


class RegistrationForm(FlaskForm):
    username = StringField('username',
                           validators=[DataRequired(),Length(min=2,max=20)])
    email=  StringField('email',
                        validators=[DataRequired(),Email()])
    password= PasswordField('password',
                            validators=[DataRequired()])
    confirm_password= PasswordField('confirm password',
                                    validators=[DataRequired(), EqualTo('password')])
    submint= SubmitField('sign up')
    
    def validate_username(self, username):
        user= user.query. filter_by(usrname=username.data).first()
        if user:
            raise validationError('That username is taken. please choose a naother one')
        
    def validate_username(self, email):
        user= user.query. filter_by(email=email.data).first()
        if user:
            raise validationError('That email is taken. please choose a naother one')
      

    
class LoginForm(FlaskForm):
    email=  StringField('email',
                        validators=[DataRequired(),Email()])
    password= PasswordField('password',
                            validators=[DataRequired()])
    remember= BooleanField('remember me')
    submint= SubmitField('login') 
    
    
class UpdateAccountForm(FlaskForm):
    username = StringField('username',
                           validators=[DataRequired(),Length(min=2,max=20)])
    email=  StringField('email',
                        validators=[DataRequired(),Email()])
    
    submint= SubmitField('sign up')
    
    def validate_username(self, username):
        if username.data != current_user.username:
           user= user.query. filter_by(usrname=username.data).first()
           if user:
               raise validationError('That username is taken. please choose a naother one')
        
    def validate_username(self, email):
        if email.data != current_user.email:
           user= user.query. filter_by(email=email.data).first()
           if user:
              raise validationError('That email is taken. please choose a naother one')
      
 
    
    
