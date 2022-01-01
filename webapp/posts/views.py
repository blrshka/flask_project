from flask import  abort, Blueprint, blueprints, render_template, current_app

from webapp.posts.models import Post

blueprint = Blueprint('post', __name__, url_prefix='/posts')

@blueprint.route("/")
def post():
    title = 'Posts'
    post_list = Post.query.order_by(Post.title).all()
    return render_template('posts/post.html', page_title=title, post_list=post_list)


@blueprint.route('/<int:id>')
def single_news(id):
    my_post = Post.query.filter(Post.id == id).first()
    if not my_post:
        abort(404)
    return render_template('posts/single_post.html', page_title=my_post.title, post=my_post)