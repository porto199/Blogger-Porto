from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    name = StringField('User Name / E-mail:', validators=[DataRequired()])
    pwd = PasswordField('Password:', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
class ResetPwdForm(FlaskForm):
    email = EmailField('Email:', validators=[DataRequired()])
    pwd = PasswordField('Password:', validators=[DataRequired()])
    pwd_2 = PasswordField('Repeat Password:', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
class RegisterForm(FlaskForm):
    name = StringField('Name:', validators=[DataRequired()])
    user = StringField('User:', validators=[DataRequired()])
    email = EmailField('Email:', validators=[DataRequired()])
    pwd = PasswordField('Password:', validators=[DataRequired()])
    pwd_2 = PasswordField('Repeat Password:', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
class Blog_Post(FlaskForm):
    title = StringField('Title:', validators=[DataRequired()])
    theme = StringField('Theme:', validators=[DataRequired()])
    content = TextAreaField('Content:')
