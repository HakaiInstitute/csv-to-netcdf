#!/usr/bin/env python

import pandas as pd
import glob
import xarray
import os
import click


def csv_to_netcdf(csv_filename, format, out_path):
    base_filename = os.path.basename(csv_filename)

    df = pd.read_csv(csv_filename, index_col=None, header=0)
    xr = xarray.Dataset.from_dataframe(df)

    xr.to_netcdf(out_path + '/' + base_filename + '.nc', format=format)


@click.command()
@click.argument('filename')
@click.option('--format', default='NETCDF4', help='NETCDF format. Must be one of NETCDF4, NETCDF4_CLASSIC, NETCDF3_64BIT, NETCDF3_CLASSIC')
@click.option('--dir', default='./', help='Directory to save the .nc files to')
def main(filename, format, dir):
    """Convert CSV to NetCDF """
    csv_to_netcdf('./'+filename, format, dir)


if __name__ == '__main__':
    main()
