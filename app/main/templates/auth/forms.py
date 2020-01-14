from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import Required, Email, EqualTo
# from ..models import User
from wtforms import ValidationError

# class UpdateProfile(FlaskForm):
#     bio = TextAreaField('Tell us about you.',validators = [Required()])
#     submit = SubmitField('Submit')
    
class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')
    
class CommentsForm(FlaskForm):
    comment = TextAreaField('Leave a comment',validators=[Required()])
    submit = SubmitField('Comment')