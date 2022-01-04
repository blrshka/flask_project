from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

from webapp.posts.models import Post

class PostForm(FlaskForm):
    post_title =  StringField('Тема', validators=[DataRequired()], render_kw={"class": "form-control"})
    post_text = StringField('Текст поста', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить!', render_kw={"class": "btn btn-primary"})

