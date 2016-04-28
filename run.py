#!/usr/bin/env python
import os
#from app package import the create_app factory which actually creates the app object (with specified config) and db
from app import create_app, db
from app.models import User

#hard coded development config
if __name__ == '__main__':
    config_name = os.environ.get('FLASK_CONFIG') or 'development'
    print(' * Loading configuration "{0}"'.format(config_name))
    app = create_app(config_name)
    
    #here db is being created at runtime
    # we need to specify which app instance to use
    # context are trick Flask uses to enable context variabels such as session or request to be activate during a reuqest cycle. This is a different use for context, by getting application context from application instance, we setup that application to be the known application for this block. So when we use db inside this block, db will know which application we are using, so it will go the find db for that app and create the db just fine. If you run db outside of active application context being in place, then db will not know which application to go and not know whcih db to initialize. Again, this all goes back to not having that global app object that you typically see in simpler Flask projects because have that create_app() factory function setup in app/__init__.py
    with app.app_context():
        db.create_all()
        if app.config['DEBUG'] and \
                User.query.filter_by(username='john').first() is None:
            User.register('john', 'cat')
    app.run()
