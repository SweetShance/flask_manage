from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from manageApp import db, create_app
# import manageApp as app 
app = create_app()

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()