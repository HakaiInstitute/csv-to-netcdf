#!/usr/bin/env python

import pandas as pd
import glob
import xarray
import os
import click
import re


def csv_to_netcdf(csv_path, format, out_directory):
    ''' Convert CSV at path <csv_path> to NetCDF using format <format> and
        save to <out_directory> 
    '''
    base_filename = re.sub('.csv$', '.nc', os.path.basename(csv_path))

    df = pd.read_csv(csv_path, index_col=None, header=0)

    xr = xarray.Dataset.from_dataframe(df)

    xr.to_netcdf(out_directory + '/' + base_filename, format=format)


@click.command()
@click.argument('filename')
@click.option('--format', default='NETCDF4', help='NETCDF format. Must be one of NETCDF4, NETCDF4_CLASSIC, NETCDF3_64BIT, NETCDF3_CLASSIC')
@click.option('--dir', default='./', help='Directory to save the .nc files to')
def main(filename, format, dir):
    """Convert CSV to NetCDF """
    csv_to_netcdf('./'+filename, format, dir)


if __name__ == '__main__':
    main()
