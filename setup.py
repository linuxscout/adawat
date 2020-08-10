#!/usr/bin/python
# -*- coding=utf-8 -*-
from setuptools import setup

# to install type:
# python setup.py install --root=/
from io import open
def readme():
    with open('README.rst', encoding="utf8") as f:
        return f.read()

setup (name='adawat', version='0.1',
      description="Adawat: Arabic Language Toolkit",
      long_description = readme(),      

      author='Taha Zerrouki',
      author_email='taha.zerrouki@gmail.com',
      url='http://adawat.sourceforge.net/',
      license='GPL',
      package_dir={'adawat': 'adawat'},
      packages=['adawat'],
      install_requires=[ "asmai>=0.1",
                    "mishkal>=0.3",
                    "naftawayh>=0.4",
                    "pyarabic>=0.6.8",
                    "qalsadi>=0.3.6",
                    "repr>=0.3.1",
                    "sylajone>=0.2",
                    "tashaphyne>=0.3.4.1",
            ],         
      include_package_data=True,
      package_data = {
        'aranasyn': ['doc/*.*','doc/html/*', 'data/*.sqlite', 'data/*.sql'],
        },
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: End Users/Desktop',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          ],
    );

