from setuptools import setup, find_packages
import sys, os

version = '0.3'

setup(name='scodeu',
      version=version,
      description="'Search client for OpenData Euskadi'",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords="'opendata client search'",
      author='Aitzol Naberan',
      author_email='anaberan@codesyntax.com',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'requests',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
