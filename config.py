import os 
basedir = os.path.abspath(os.path.dirname(__file__))
class config:
	SECRET_KEY=os.environ.get('SECRET_KEY') or 'hard to guess string'
	SQLALCHEMY_COMMIT_ON_TEARDOWN=True
	FLASKY_MAIL_SUBJECT_PREFIX='[Flasky]'
	FLASKY_MAIL_SENDER='Flasky Admin <mazhouliang_1@163.com>'
	FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN') 

	@staticmethod
	def init_app(app):
		pass
class DevelopmentConfig(config): 
    DEBUG = True 
    MAIL_SERVER = 'smtp.googlemail.com' 
    MAIL_PORT = 587
    MAIL_USE_TLS = True 
    MAIL_USERNAME = 'tywetyty'
    MAIL_PASSWORD = 'mzl830921'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite') 
 
class TestingConfig(config): 
    TESTING = True 
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data-test.sqlite') 
 
class ProductionConfig(config): 
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.sqlite') 
 
config = { 
    'development': DevelopmentConfig, 
    'testing': TestingConfig, 
    'production': ProductionConfig, 
    'default': DevelopmentConfig 
}