from setuptools import setup

import os
import sys

PYCART_DIR = ''.join(['python-', '.'.join(map(str, sys.version_info[:2]))])
sys.path.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi', 'openshift'))
virtenv = PYCART_DIR + '/virtenv/'
os.environ['PYTHON_EGG_CACHE'] = os.path.join(virtenv, 'lib/python2.6/site-packages')
virtualenv = os.path.join(virtenv, 'lib/python2.6/site-packages')
print(virtualenv)
#virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    execfile(virtualenv, dict(__file__=virtualenv))
except:
    pass


setup(name='YourAppName', version='1.0',
      description='OpenShift Python-3.3 Community Cartridge based application',
      author='Erich Morisse', author_email='erich.morisse@gmail.com',
      url='http://www.python.org/sigs/distutils-sig/',

      #  Uncomment one or more lines below in the install_requires section
      #  for the specific client drivers/modules your application needs.
      install_requires=['WebOb',
                        #  'mysql-connector-python',
                        #  'pymongo',
                        #  'psycopg2',
      ],
     )
