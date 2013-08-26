#!/usr/bin/env python

from setuptools import setup, find_packages

from timetable import VERSION

github_url = 'https://github.com/g3rd/django-timetable'

setup(
    name='django-timetable',
    version='.'.join(str(v) for v in VERSION),
    description='An Django app that provides generic calendar functions',
    long_description=open('README.md').read(),
    url=github_url,
    author='Chad Shryock',
    author_email='chad@g3rdmedia.com',
    requires=[
        'Django (>=1.5)',
    ],
    install_requires=[
        'django',
        'django-taggit',
        'django-colorful',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    license='MIT License',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
