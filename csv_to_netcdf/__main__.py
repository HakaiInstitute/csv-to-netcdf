#!/usr/bin/env python

import click
from .csv_to_netcdf import csv_to_netcdf


@click.command()
@click.argument('filename')
@click.option('--format', default='NETCDF4', help='NETCDF format. Must be one of NETCDF4, NETCDF4_CLASSIC, NETCDF3_64BIT, NETCDF3_CLASSIC')
@click.option('--dir', default='./', help='Directory to save the .nc files to')
def main(filename, format, dir):
    """Convert CSV to NetCDF """
    csv_to_netcdf('./'+filename, format, dir)


if __name__ == '__main__':
    main()
