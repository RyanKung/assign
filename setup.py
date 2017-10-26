# coding:utf8

import os
import codecs
import re
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
_CWD = os.path.dirname(__file__)

NAME = 'assign'
DESCRIPTION = 'A Black Magic for support obj.__assign__ method'
AUTHOR = 'ryankung'
EMAIL = 'ryankung@ieee.org'


def read(*parts):
    # intentionally *not* adding an encoding option to open, See:
    #   https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    return codecs.open(os.path.join(here, *parts), 'r').read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name=NAME,
    description=DESCRIPTION,
    long_description=open(os.path.join(here, 'readme.md')).read(),
    version=find_version('assign', '__init__.py'),
    packages=find_packages(exclude=['examples', 'tests', 'docs']),
    install_requires=[],
    package_dir={'': '.'},
    author=AUTHOR,
    author_email=EMAIL,
    license="MIT",
    platforms=['any'],
    url="",
    classifiers=["Intended Audience :: Developers",
                 "Programming Language :: Python",
                 "Topic :: Software Development :: Libraries :: Python Modules"],
    include_package_data=True
)
