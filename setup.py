from setuptools import find_packages
from setuptools import setup

setup(
    entry_points={
        'paste.app_factory': 'main=pyramid_app:main',
    },
    install_requires=[
        'pyramid',
        'waitress',
    ],
    name='pyramid_app',
)
