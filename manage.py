import os
from app import create_app, db
from app.models import Role, User, Permission, Post, Follow, Alembic
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from tests.test_user_models import UserModelTestCase

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

manager = Manager(app)
migrate = Migrate(app, db)

@manager.shell
def make_shell_context():
	return dict(app=app, db=db, User=User, Role=Role, Permission=Permission, Post = Post, Alembic = Alembic, test = UserModelTestCase)

manager.add_command('db', MigrateCommand)

@manager.command
def profile(length = 25, profile_dir = None):
	from werkzeug.contrib.profiler import ProfilerMiddleware
	app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions = [length], profile_dir = profile_dir)
	app.run()
	
if __name__ == '__main__':
	manager.run()
