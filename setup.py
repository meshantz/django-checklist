#!/usr/bin/env python
from distutils.core import setup
import os
import checklist

# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

for dirpath, dirnames, filenames in os.walk('checklist'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        # note this assumes every file you are including is under the
        # checklist folder. you will need to modify it if your files are
        # more scattered.
        prefix = dirpath[len('checklist/'):]
        for f in filenames:
            data_files.append(os.path.join(prefix, f))

setup(name='django-checklist',
      version=checklist.get_version().replace(' ','-'),
      author='',
      author_email='meshantz@yahoo.ca',
      url='https://github.com/meshantz/django-checklist',
      description='django app: checklist',
      packages=packages,
      package_dir={'checklist': 'checklist',},
      package_data={'checklist': data_files},
      )

