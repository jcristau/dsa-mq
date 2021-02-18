#!/usr/bin/python

from distutils.core import setup
import glob

setup(name='dsa-mq',
      version='0.4',
      description='Common libraries for pub/sub messaging in debian',
      author='Stephen Gran',
      author_email='sgran@debian.org',
      url='https://github.com/jcristau/dsa-mq',
      scripts=glob.glob('bin/*'),
      packages=['dsa_mq'],
     )
