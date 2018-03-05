from flask_wtf import Form 
from ..models import User
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError

# 登陆表单
class LoginForm(Form):
	email = StringField('邮件', validators=[Required(), Length(1, 64), Email()])
	password = PasswordField('密码', validators=[Required()])
	remember = BooleanField('保持登录')
	submit = SubmitField('登录')

# 注册表单
class RegisterForm(Form):
	email = StringField('邮箱', validators=[Required(), Length(1, 64), Email()])
	username = StringField('用户名', validators=[Required(), Length(1, 64), 
		Regexp('^[A-za-z][A-za-z0-9_.]*$', 0, 'Username must have only letters, numbers, dots or underscores')])

	password = PasswordField('密码', validators=[Required(), EqualTo('password2', message='Passwords must match.')])
	password2 = PasswordField('确认密码', validators=[Required()])
	submit = SubmitField('注册')

	def validate_email(self, field):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError('邮箱已经注册.')

	def validate_username(self, field):
		if User.query.filter_by(username=field.data).first():
			raise ValidationError('用户名已存在.')