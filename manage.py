from jobplus.app import create_app
from flask import render_template
from flask_script import Manager, Shell
from flask_migrate import MigrateCommand

from jobplus.models import *
app = create_app('development')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

manager = Manager(app)
def context():
    return {
        'db':db,'User': User
    }
manager.add_command('shell', Shell(make_context=context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

