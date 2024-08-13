from os.path import dirname, join as pjoin
import scipy.io as sio
import datetime as dt
import pandas as pd
import numpy as np
import argparse
import os

def labchart_mat_file_to_csv(mat_file_path, csv_file_name):
    """
    Load and process a MATLAB .mat file exported from LabChart to extract channel data and convert it to a pandas DataFrame.

    Parameters:
    mat_file_path (str): Path to the .mat file.
    csv_file_name (str): Desired name for the output CSV file.

    Returns:
    None: Saves the DataFrame as a CSV file in the same directory as the .mat file.
    """
    # Load .mat file contents
    mat_contents = sio.loadmat(mat_file_path)

    # Extracting Matlab file channel data into a dictionary from Matlab .mat file
    channel_data_dict = {}

    for i in range(len(mat_contents.get('titles'))):
        unit_str = mat_contents.get('unittext')[int(mat_contents.get('unittextmap')[i][0])-1].strip()
        key_str = mat_contents.get('titles')[i].strip()
        channel_key = f'{key_str}[{unit_str}]'
        channel_data_dict[channel_key] = mat_contents.get('data')[0][int(mat_contents.get('datastart')[i][0]): int(mat_contents.get('dataend')[i][0])]

    channel_data_df = pd.DataFrame(channel_data_dict)

    # Convert MATLAB time to pandas datetime
    matlab_time = mat_contents.get('blocktimes')[0][0]
    pandas_datetime = dt.datetime.fromordinal(int(matlab_time)) + dt.timedelta(days=matlab_time % 1) - dt.timedelta(days=366)

    # Generate time series
    n_samples = len(channel_data_df)
    max_sampling_rate = np.max(mat_contents['samplerate'])
    time_interval = 1 / max_sampling_rate
    time_series = pd.date_range(start=pandas_datetime, periods=n_samples, freq=f"{time_interval}s")

    channel_data_df['Time'] = time_series

    # Add Event marker comments
    comment_dict = {int(comment[2]): mat_contents['comtext'][int(comment[4] - 1)].strip() for comment in mat_contents['com']}
    channel_data_df['Comment'] = channel_data_df.index.map(comment_dict)

    # Save DataFrame to CSV
    output_path = os.path.join(dirname(mat_file_path), csv_file_name)
    channel_data_df.to_csv(output_path, index=False)
    print(f"Data saved to {output_path}")

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description='Convert a MATLAB .mat file to a CSV file.')
    parser.add_argument('mat_file_path', type=str, help='Path to the input .mat file')
    parser.add_argument('csv_file_name', type=str, help='Name for the output CSV file')

    # Parse arguments
    args = parser.parse_args()

    # Call the conversion function
    labview_mat_file_to_csv(args.mat_file_path, args.csv_file_name)
