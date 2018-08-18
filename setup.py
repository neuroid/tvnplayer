from setuptools import find_packages
from setuptools import setup


setup(name='tvnplayer',
      version='0.9.0',
      description='Tiny helper for playing https://player.pl/ content on Linux',
      py_modules=['tvnplayer'],
      install_requires=[
          'docopt',
          'requests',
      ],
      entry_points={
          'console_scripts': [
              'tvnplayer = tvnplayer:main'
          ]
      })
