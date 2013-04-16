from setuptools import setup

import os
import sys


os.putenv('PATH',os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'lib64', 'R', 'bin:',) + os.environ['PATH'])
print(os.environ['PATH'])


setup(name='YourAppName', version='1.0',
      description='OpenShift Python-3.3 Community Cartridge based application',
      author='Erich Morisse', author_email='erich.morisse@gmail.com',
      url='http://www.python.org/sigs/distutils-sig/',

      #  Uncomment one or more lines below in the install_requires section
      #  for the specific client drivers/modules your application needs.
      install_requires=['WebOb',
                        'rpy2',
                        #  'mysql-connector-python',
                        #  'pymongo',
                        #  'psycopg2',
      ],
     )
