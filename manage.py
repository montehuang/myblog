import os
from app import create_app, db
from app.models import Role, User
from flask_script import Manager

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

manager = Manager(app)

@manager.shell
def make_shell_context():
	return dict(app=app, db=db, User=User, Role=Role)
	
if __name__ == '__main__':
	manager.run()
