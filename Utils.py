from os.path import dirname, join as pjoin
import scipy.io as sio
import datetime as dt
import pandas as pd
import numpy as np


def labchart_mat_file_to_csv(file_path):
    """
    Load and process a MATLAB .mat file exported from LabChart  to extract channel data and convert it to a pandas DataFrame.

    Parameters:
    file_path (str): Path to the .mat file.

    Returns:
    pd.DataFrame: DataFrame containing the channel data, time series, and comments.
    """
    mat_contents = sio.loadmat(r'C:\Users\herathi1\Documents\IsuruSachitha_Files\Research_Data_Repository\Healthy Control Data\Test_001_NIBM_Sensor_Posture\Test_001_NIBM_Sensor_Posture\Test_001_RecordedMatlab.mat')

    # Extracting Matlab file channel data into a dictionary from Matlab .mat file
    channel_data_dict = {}

    for i in range(len(mat_contents.get('titles'))):

        unit_str = mat_contents.get('unittext')[int(mat_contents.get('unittextmap')[i][0])-1].strip()
        key_str = mat_contents.get('titles')[i].strip()
        channel_key = f'{key_str}[{unit_str}]'
        channel_data_dict [channel_key] = mat_contents.get('data')[0][ int(mat_contents.get('datastart')[i][0]) : int(mat_contents.get('dataend')[i][0]) ]

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

    return channel_data_df
