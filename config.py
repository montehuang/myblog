#coding:utf8

import os
import pymysql
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guss'
	SQLALCHEMY_COMMIT_ON_TEARDOWN = True
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	MAIL_SERVER = 'smtp.qq.com'  # 邮件服务器地址
	MAIL_DEBUG = True
	MAIL_PORT = 465               # 邮件服务器端口
	#MAIL_USE_TLS = True          # 启用 TLS
	MAIL_USE_SSL = True          # 启用 TLS
	MAIL_USERNAME = os.environ.get('FLASKY_MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('FLASKY_MAIL_PASSWORD')
	FLASKY_MAIL_SENDER = os.environ.get('FLASKY_MAIL_USERNAME') or 'hqzmonte@sina.com'
	FLASKY_MAIL_SUBJECT_PREFIX = 'monte blog'
	FLASKY_ADMIN = os.environ.get('FLASKY_MAIL_USERNAME') 
	FLASK_POSTS_PER_PAGE = 10
	FLASKY_FOLLOWERS_PER_PAGE = 10
	FLASKY_COMMENTS_PER_PAGE = 10
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
