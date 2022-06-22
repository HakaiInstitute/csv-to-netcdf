#!/usr/bin/env python

from distutils.core import setup

setup(name='csv_to_netcdf',
      version='0.1',
      description='Convert CSV to NetCDF',
      url='https://github.com/HakaiInstitute/csv-to-netcdf',
      packages=['csv_to_netcdf'],

      install_requires=[
          'certifi==2019.11.28',
          'cftime==1.1.0',
          'Click==7.0',
          'netCDF4==1.5.3',
          'numpy==1.22.0',
          'pandas==1.0.1',
          'python-dateutil==2.8.1',
          'pytz==2019.3',
          'six==1.14.0',
          'xarray == 0.15.0'
      ]

      )
