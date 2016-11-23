import re
import ast
from setuptools import setup


_version_re = re.compile(r'__version__\s+=\s+(.*)')


with open('sensible/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))


setup(
    name='sensible',
    author='Noah Gift',
    author_email='noah.gift@gmail.com',
    version=version,
    url='http://github.com/nogibjj/sensible',
    packages=['sensible'],
    description='A simple and sensible logging config',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ],
)
