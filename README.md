# CSV to NetCDF converter

This is a simple Python3 to convert CSV to NetCDF using xarray

## Installation

If needed, install virtualenv.

- `pip install virtualenv --user`

From this directory, run:

- `virtualenv -p python3 venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`

## Running

- `python csv_to_netcdf myfile.csv`

This will create a file myfile.nc in the same directory
options:

- `--format`
  NETCDF format. Must be one of NETCDF4, NETCDF4_CLASSIC, NETCDF3_64BIT, NETCDF3_CLASSIC

- `--dir`
  Directory to save the .nc files to
