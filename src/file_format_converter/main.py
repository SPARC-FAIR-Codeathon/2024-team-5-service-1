import argparse
import os
import zipfile

import pandas as pd
import json
import yaml
import h5py
import pyarrow.parquet as pq
import pyarrow.feather as feather
import pickle
import xml.etree.ElementTree as ET
import toml

class FileConverter:
    def __init__(self, input_file):
        self.input_file = input_file
        self.input_format = self._get_file_format(input_file)
        self.data = None

    def _get_file_format(self, filename):
        return filename.split('.')[-1].lower()

    def read_file(self):
        if self.input_format == 'csv':
            self.data = pd.read_csv(self.input_file)
        elif self.input_format == 'xls':
            self.data = pd.read_excel(self.input_file, engine='xlrd')
        elif self.input_format == 'xlsx':
            self.data = pd.read_excel(self.input_file)
        elif self.input_format == 'json':
            with open(self.input_file, 'r') as f:
                self.data = json.load(f)
        elif self.input_format == 'yaml':
            with open(self.input_file, 'r') as f:
                self.data = yaml.safe_load(f)
        elif self.input_format in ['h5', 'hdf5']:
            self.data = pd.read_hdf(self.input_file)
        elif self.input_format == 'parquet':
            self.data = pd.read_parquet(self.input_file)
        elif self.input_format == 'feather':
            self.data = pd.read_feather(self.input_file)
        elif self.input_format == 'pkl':
            with open(self.input_file, 'rb') as f:
                self.data = pickle.load(f)
        elif self.input_format == 'xml':
            tree = ET.parse(self.input_file)
            self.data = tree.getroot()
        elif self.input_format == 'toml':
            with open(self.input_file, 'r') as f:
                self.data = toml.load(f)
        elif self.input_format == 'nwb':
            with h5py.File(self.input_file, 'r') as f:
                self.data = f['data'][:]
        else:
            raise ValueError(f"Unsupported file format: {self.input_format}")

    def write_file(self, output_file):
        output_format = self._get_file_format(output_file)

        if output_format == 'csv':
            self.data.to_csv(output_file, index=False)
        elif output_format in ['xls', 'xlsx']:
            self.data.to_excel(output_file, index=False)
        elif output_format == 'json':
            if isinstance(self.data, pd.DataFrame):
                self.data = self.data.to_dict(orient='records')
            with open(output_file, 'w') as f:
                json.dump(self.data, f, indent=4)
        elif output_format == 'yaml':
            if isinstance(self.data, pd.DataFrame):
                self.data = self.data.to_dict(orient='records')
            with open(output_file, 'w') as f:
                yaml.dump(self.data, f, default_flow_style=False)
        elif output_format in ['h5', 'hdf5']:
            self.data.to_hdf(output_file, key='df', mode='w')
        elif output_format == 'parquet':
            self.data.to_parquet(output_file)
        elif output_format == 'feather':
            self.data.to_feather(output_file)
        elif output_format == 'pkl':
            with open(output_file, 'wb') as f:
                pickle.dump(self.data, f)
        elif output_format == 'xml':
            tree = ET.ElementTree(self.data)
            tree.write(output_file)
        elif output_format == 'toml':
            with open(output_file, 'w') as f:
                toml.dump(self.data, f)
        elif output_format == 'nwb':
            with h5py.File(output_file, 'w') as f:
                f.create_dataset('data', data=self.data)
        else:
            raise ValueError(f"Unsupported output file format: {output_format}")

    def preview(self, num_rows=5):
        if isinstance(self.data, pd.DataFrame):
            return self.data.head(num_rows)
        else:
            return self.data

    def transform(self, transformation_func):
        if isinstance(self.data, pd.DataFrame):
            self.data = transformation_func(self.data)
        else:
            raise ValueError("Data transformations are only supported for tabular data formats.")

    def convert(self, output_file):
        self.read_file()
        self.write_file(output_file)
        print(f"Converted {self.input_file} to {output_file} successfully.")
        # now create a zip of the output file as output.zip
        with zipfile.ZipFile('output.zip', 'w') as z:
            z.write(output_file)
        print(f"Zipped {output_file} to output.zip successfully.")
        # # write output file path to a file
        # with open('log_output_filepath.txt', 'w') as f:
        #     f.write(output_file)

# Example Usage
if __name__ == "__main__":
    # first argument to file is the input file and second argument is the desired output format
    # use argparse to parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='Input file to convert')
    parser.add_argument('output_format', help='Output file format')
    args = parser.parse_args()

    input_file = args.input_file
    output_format = args.output_format
    # trim double quotes if present
    if output_format[0] == '"' and output_format[-1] == '"':
        output_format = output_format[1:-1]

    # get input file name with extension without path
    output_file = f"{os.path.splitext(os.path.basename(input_file))[0]}.{output_format}"
    print(f"Converting {input_file} to {output_format} to produce {output_file}")

    converter = FileConverter(input_file)
    converter.convert(output_file)
