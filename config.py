import os
import pymysql
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guss'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:0270@127.0.0.1:3306/flasky?charset=utf8'
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