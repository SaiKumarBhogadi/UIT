'''
#python 3.11.9
import imp
import os
import sys


sys.path.insert(0, os.path.dirname(__file__))

wsgi = imp.load_source('wsgi', 'manage.py')
application = wsgi./home/cmikivni/uit/uitech/uit/wsgi.py'''


#Python 3.12.4

import importlib.util
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

spec = importlib.util.spec_from_file_location('wsgi', 'manage.py')
wsgi = importlib.util.module_from_spec(spec)
spec.loader.exec_module(wsgi)

from uit.wsgi import application
