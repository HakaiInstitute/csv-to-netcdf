#!/usr/bin/env python

import pandas as pd
import glob
import xarray
import os
import re


def csv_to_netcdf(csv_path, format, out_directory):
    ''' Convert CSV at path <csv_path> to NetCDF using format <format> and
        save to <out_directory> 
    '''
    base_filename = re.sub('.csv$', '.nc', os.path.basename(csv_path))

    df = pd.read_csv(csv_path, index_col=None, header=0)

    xr = xarray.Dataset.from_dataframe(df)

    xr.to_netcdf(out_directory + '/' + base_filename, format=format)
