from flask_wtf import FlaskForm, Form
from ..models import Role, User, PostTag
from flask_pagedown.fields import PageDownField
from wtforms import StringField, SubmitField, TextAreaField, SelectField, BooleanField, Field
from wtforms.validators import Required, Length, Email, Regexp, ValidationError
from wtforms.widgets import TextInput

class TagListForm(Field):
	widget = TextInput()
	
	def __init__(self, label=None, validators=None, **kwargs):
		super(TagListForm, self).__init__(label, validators, **kwargs)

	def _value(self):
		if self.data:
			r = u'';
			for obj in self.data:
				r += self.obj_to_str(obj)
				r += ","
			return r
		else:
			return u''

	def process_formdata(self, valuelist):
		if valuelist:
			tags = self._remove_duplicates([x.strip() for x in valuelist[0].split(',')])
			self.data = [self.str_to_obj(tag) for tag in tags if tag != ""]
		else:
			self.data = None

	def pre_validate(self, form):
		pass

	@classmethod
	def _remove_duplicates(cls, seq):
		d = {}
		for item in seq:
			if item.lower() not in d:
				d[item.lower()] = True
				yield item

	@classmethod
	def str_to_obj(cls, tag):
		tag_obj = PostTag.query.filter_by(body=tag).first()
		if tag_obj is None:
			tag_obj = PostTag(body=tag)
		return tag_obj

	@classmethod
	def obj_to_str(cls, obj):
		if obj:
			return obj.body
		else:
			return u''


class NameForm(Form):
	name = StringField('你的名字?', validators = [Required()])
	submit = SubmitField('提交')

class EditProfileForm(Form):
	name = StringField('真名', validators = [Length(0,64)])
	location = StringField('位置', validators = [Length(0,64)])
	about_me = TextAreaField('个人简介')
	submit = SubmitField('提交')

class NewEditProfileForm(Form):
	all_info = PageDownField("博客内容", validators = [Required()])
	submit = SubmitField("提交")

class EditProfileAdminForm(Form):
	email = StringField('邮箱', validators = (Required(), Length(1, 64), Email()))
	username = StringField('用户名', validators = (Required(), Length(1, 64), 
		Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Usename must have only letters, numbers, dots or underscores')))
	confirmed = BooleanField('确定')
	role = SelectField('角色', coerce = int)
	name = StringField('真名', validators = [Length(0, 64)])
	location = StringField('位置', validators = [Length(0, 64)])
	about_me = TextAreaField('个人简介')
	submit = SubmitField('提交')

	def __init__(self, user, *args, **kwargs):
		super(EditProfileAdminForm, self).__init__(*args, **kwargs)
		self.role.choices = [(role.id, role.name) for role in Role.query.order_by(Role.name).all()]
		self.user = user

	def validate_email(self, field):
		if field.data != self.user.email and \
			User.query.filter_by(email = field.data).first():
			raise ValidationError('Email already registered.')

	def validate_username(self, field):
		if field.data != self.user.username and \
			User.query.filter_by(username = field.data).first():
			raise ValidationError('Username already in use.')

class PostForm(FlaskForm):
	body = PageDownField("博客内容", validators = [Required()])
	title = StringField("博客标题", validators = [Required()])
	brief = StringField("编辑简述", validators = [Required()])
	edittime = StringField("编辑时间")
	tags = TagListForm(u'标签', validators=[Required()])
	submit = SubmitField('提交')

class CommentForm(FlaskForm):
	body = PageDownField("", validators = [Required()])
	submit = SubmitField('提交')