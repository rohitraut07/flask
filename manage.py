import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + os.sep + '..')
import unittest
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from main import create_app
from app import blueprint
import main.model
from app.main.model import user
from main.model.user import Subscription

from main import create_app, db

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run()



@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()
