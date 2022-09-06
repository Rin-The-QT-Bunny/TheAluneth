from setuptools import setup

setup(
   name='Aluneth',
   version='0.1.0',
   author='ZongjingLi',
   author_email='ysun697@gatech.edu',
   packages=['package_name', 'package_name.test'],
   scripts=['bin/script1','bin/script2'],
   url='http://pypi.python.org/pypi/PackageName/',
   license='LICENSE.txt',
   description='Come child, lets wrech havoc.',
   long_description=open('README.txt').read(),
   install_requires=[
   ],
)