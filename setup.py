import os
import re

from setuptools import setup


PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_ENTRY_FILE = 'downloader.py'


def get_project_version():
    filename = os.path.join(PROJECT_ROOT, PROJECT_ENTRY_FILE)
    pattern = r"^__version__ = '(.*?)'$"
    with open(filename) as f:
        return re.search(pattern, f.read(), re.MULTILINE).group(1)


setup(
    name='py-downloader',
    version=get_project_version(),
    description='A simple CLI file downloader',
    author='Adarsh Krishnan',
    author_email='adarshk7@gmail.com',
    py_modules=['py-downloader'],
    license=open('LICENSE').read(),
    platforms='any',
    install_requires=[
        'requests>=1.0',
        'click>=7.0'
    ]
)
