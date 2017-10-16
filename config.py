import os
import pymysql
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guss'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	MAIL_SERVER = 'smtp.sina.com'  # 邮件服务器地址
	MAIL_PORT = 25               # 邮件服务器端口
	MAIL_USE_TLS = True          # 启用 TLS
	# MAIL_USE_SSL = True          # 启用 TLS
	MAIL_USERNAME = os.environ.get('FLASKY_MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('FLASKY_MAIL_PASSWORD')
	FLASKY_MAIL_SENDER = os.environ.get('FLASKY_MAIL_USERNAME')
	FLASKY_MAIL_SUBJECT_PREFIX = 'monte blog'
	# MAIL_USERNAME = "865824187@qq.com"
	# MAIL_PASSWORD = "lecydmmxbsqtbbij"
	MAIL_USERNAME = 'hqzmonte@sina.com'
	MAIL_PASSWORD = 'hqz032340'
	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///'+basedir+'/flasky.db'
	DEBUG = True

class TestingConfig(Config):
	TESTING = True

class ProductionConfig(Config):
	pass

config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'production': ProductionConfig,

	'default': DevelopmentConfig,
}