
import sys
path = 'home/amir/projects/school'
if path not in sys.path : 
    sys.path.append(path)

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school.settings')

application = get_wsgi_application()
