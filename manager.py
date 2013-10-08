from flask.ext.script import Manager

from overshard import create_app
from overshard.extensions import db
app = create_app('settings.py')
manager=Manager(app)

@manager.command
def run():
	app.run()

@manager.command
def create_db():
	db.create_all()

if __name__ =="__main__":
	manager.run()