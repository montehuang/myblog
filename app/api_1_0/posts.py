from . import api
from .authentication import auth
from flask import jsonify, url_for
from ..models import Post, Permission
from .decorators import permission_required
# 新的博客
@api.route('/posts/', methods = ['POST'])
@permission_required(Permission.WRITE_ARTICLE)
def new_post():
	post = Post.from_json(request.json)
	post.author = g.current_user

# 获取所有博客信息
@api.route('/posts/')
@auth.login_required
def get_posts():
	posts = Post.query.all()
	return jsonify({'posts' : [post.to_json() for post in posts]})

@api.route('/posts/<int:id>')
@auth.login_required
def get_post(id):
	post = Post.query.get_or_404(id)
	return jsonify(post.to_json())