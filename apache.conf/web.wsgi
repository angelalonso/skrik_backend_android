import os, sys
sys.path.append('/var/www/skrik_backend_android/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'skrik.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
