#!/usr/bin/env python
import imp
import os
import sys

PYCART_DIR = ''.join(['python-', '.'.join(map(str, sys.version_info[:2]))])


try:
   zvirtenv = os.path.join(os.environ['OPENSHIFT_HOMEDIR'], PYCART_DIR,
                           'virtenv', 'bin', 'activate_this.py')
   exec(compile(open(zvirtenv).read(), zvirtenv, 'exec'),
        dict(__file__ = zvirtenv) )
except IOError:
   pass


def run_simple_httpd_server(app, ip, port=8080):
   from wsgiref.simple_server import make_server
   make_server(ip, port, app).serve_forever()


#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
# 

import os
import sys
 
os.environ['DJANGO_SETTINGS_MODULE'] = 'openshift.settings'
sys.path.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi', 'openshift'))
virtenv = os.environ['APPDIR'] + '/virtenv/'
os.environ['PYTHON_EGG_CACHE'] = os.path.join(virtenv, 'lib/python2.6/site-packages')
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
except:
    pass

from rpy2.robjects import Formula, r
from rpy2.robjects.packages import importr


#
#  main():
#
if __name__ == '__main__':
   ip   = os.environ['OPENSHIFT_INTERNAL_IP']
   port = 8080
   zapp = imp.load_source('application', 'wsgi/application')

   print('Starting WSGIServer on %s:%d ... ' % (ip, port))
   run_simple_httpd_server(zapp.application, ip, port)


rf = importr("randomForest")
iris = r['iris']
fmla = Formula("Species ~ .")
iris_rf = rf.randomForest(fmla, iris)
predict = r('predict')
iris_predict = predict(iris_rf, iris)
iris_predict
