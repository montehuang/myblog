import unittest
import time
from app import db
from app.models import User, AnonymousUser, Role, Permission

class UserModelTestCase(unittest.TestCase):
	def test_password_setter(self):
		u = User(password = 'monte')
		self.assertTrue(u.password_hash is not None)

	def test_no_password_getter(self):
		u = User(password = 'monte')
		with self.assertRaises(AttributeError):
			u.password

	def test_password_verification(self):
		u = User(password = 'monte')
		self.assertTrue(u.verify_password('monte'))
		self.assertFalse(u.verify_password('hello'))

	def test_password_salts_are_random(self):
		u = User(password = 'monte')
		u2 = User(password = 'hello')
		self.assertTrue(u.password_hash != u2.password_hash)

	def test_valid_confirmation_token(self):
		u = User(password='cat')
		db.session.add(u)
		db.session.commit()
		token = u.generate_confirmation_token()
		self.assertTrue(u.confirm(token))
	def test_invalid_confirmation_token(self):
		u1 = User(password='cat')
		u2 = User(password='dog')
		db.session.add(u1)
		db.session.add(u2)
		db.session.commit()
		token = u1.generate_confirmation_token()

		self.assertFalse(u2.confirm(token))

	def test_expired_confirmation_token(self):
		u = User(password='cat')
		db.session.add(u)
		db.session.commit()
		token = u.generate_confirmation_token(1)
		time.sleep(2)
		self.assertFalse(u.confirm(token))

	# 测试用户权限
	def test_roles_and_permissions(self):
		Role.insert_roles()
		u = User(email = 'hahaha@sian.com', password = '123')
		self.assertTrue(u.can(Permission.WRITE_ARTICLE))
		self.assertFalse(u.can(Permission.MODERATE_COMMENTS))
	def test_anonymous_user(self):
		u = AnonymousUser()
		self.assertFalse(u.can(Permission.FOLLOW))

	# 测试关注用户
	def test_follow_user(self):
		u1 = User.query.filter_by(username = 'u1').first()
		u2 = User.query.filter_by(username = 'u2').first()
		if u1 is None:
			u1 = User(username = 'u1')
			db.session.add(u1)
			db.session.commit()
		if u2 is None:
			u2 = User(username = 'u2')
			db.session.add(u2)
			db.session.commit()
		self.assertTrue(u1.follow(u2))

	# 测试取消关注
	def test_unfollow_user(self):
		u1 = User.query.filter_by(username = 'u1').first()
		u2 = User.query.filter_by(username = 'u2').first()
		self.assertTrue(u1.unfollow(u2))

	# 测试是否关注某人
	def test_is_following_user(self):
		u1 = User.query.filter_by(username = 'u1').first()
		u2 = User.query.filter_by(username = 'u2').first()
		self.assertTrue(u1.is_following(u2))

	# 测试是否被某人关注
	def test_is_followed_by_user(self):
		u1 = User.query.filter_by(username = 'u1').first()
		u2 = User.query.filter_by(username = 'u2').first()
		self.assertTrue(u2.is_followed(u1))