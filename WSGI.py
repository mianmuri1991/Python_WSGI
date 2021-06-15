import os
import sys
from dotenv import load_dotenv
path = '/home/<username>/<project name>'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = '<project name>.settings'

project_folder = os.path.expanduser('~/<project name>')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
application = WhiteNoise(get_wsgi_application())