from whitenoise import WhiteNoise
import os

config_name = os.environ.get('FLASK_CONFIG') or 'production'

from app import create_app

#creating app instance
application = create_app(config_name)

#application = app()
application = WhiteNoise(application, root='/path/to/static/files')
application.add_files('/path/to/more/static/files', prefix='more-files/')

