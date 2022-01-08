from flask import  abort, Blueprint, blueprints, render_template, current_app, flash, redirect, request, url_for
from flask_login import current_user, login_required

from webapp.db import db
from webapp.posts.forms import PostForm
from webapp.posts.models import Post
from webapp.utils import get_redirect_target

blueprint = Blueprint('post', __name__, url_prefix='/posts')

@blueprint.route("/")
def post():
    title = 'Посты пользователей'
    post_list = Post.query.filter(Post.text.isnot(None)).order_by(Post.created.desc()).all()
    return render_template('posts/post.html', page_title=title, post_list=post_list)


@blueprint.route('/<int:id>')
def single_post(id):
    my_post = Post.query.filter(Post.id == id).first()
    if not my_post:
        abort(404)
    return render_template('posts/single_post.html', page_title=my_post.title, post=my_post)

@blueprint.route('new_post')
def new_post():
    title = 'Новый пост'
    form = PostForm()
    return render_template('posts/new_post.html', page_title=title, form=form)

@blueprint.route('/add', methods=['POST'])
@login_required
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.post_title.data,text=form.post_text.data, user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        flash('Пост успешно добавлен')
        return redirect(url_for('post.post'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Ошибка в заполнении поля "{}": - {}'.format(
                    getattr(form, field).label.text,
                    error
                ))
    return redirect(get_redirect_target())
    