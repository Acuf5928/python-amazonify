from os.path import abspath, dirname, join, normpath

from setuptools import setup


setup(

    # Basic package information:
    name = 'amazonify',
    version = '0.2',
    py_modules = ('amazonify',),

    # Packaging options:
    zip_safe = False,
    include_package_data = True,

    # Package dependencies:
    install_requires = [],

    # Metadata for PyPI:
    author = 'Acuf5928',
    author_email = 'alberto.cuffaro@hotmail.it',
    license = 'UNLICENSE',
    url = 'https://github.com/Acuf5928/python-amazonify',
    keywords = 'amazon affiliate web',
    description = 'The simplest way to build Amazon Affiliate links, in Python.',
    long_description = open(normpath(join(dirname(abspath(__file__)),
        'README.md'))).read()

)
