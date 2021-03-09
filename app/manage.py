import os
import unittest
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from main.model import user
from main import create_app, db
from blueP import blueprint
fapp = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')

fapp.register_blueprint(blueprint)

fapp.app_context().push()

manager = Manager(fapp)

migrate = Migrate(fapp, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    fapp.run()


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
