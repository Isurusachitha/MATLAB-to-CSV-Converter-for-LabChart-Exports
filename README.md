# MATLAB-to-CSV-Converter-for-LabChart-Exports

This repository contains a Python script designed to convert MATLAB exports of LabChart data from ADInstruments into a structured CSV format. LabChart is a powerful data acquisition (DAQ) software used in life science research, enabling the collection and analysis of physiological signals from various sensors connected through PowerLab systems. This tool is particularly useful for researchers and data analysts who need to streamline their data processing workflows. By converting the data into CSV files with event labels, users can easily analyze and visualize their data using various data analysis tools and libraries.This code is based on the information provided by ADInstruments regarding data saving and exporting options in LabChart, which supports various formats including MATLAB and CSV.

#### Features
- **MATLAB Export Compatibility**: Seamlessly convert MATLAB files exported from LabChart.
- **Event Labeling**: Automatically include event labels in the CSV output for better data organization.
- **User-Friendly**: Simple command-line interface for easy usage.
- **Open Source**: Free to use and modify under the  GNU GENERAL PUBLIC LICENSE Version 3.

#### Installation
To install the required packages, run the following command:

```bash
pip install -r requirements.txt
```

#### Usage
To convert a MATLAB file to CSV, use the following command in your terminal:

```bash
python convert_labchart.py input_file.mat output_file.csv
```

### Example Jupyter Notebook

Below is a simple example of how to use the conversion script within a Jupyter Notebook.

```python
# Import necessary libraries
import pandas as pd
import os

# Define the conversion function
def convert_matlab_to_csv(input_file, output_file):
    # Check if the input file exists
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"The file {input_file} does not exist.")
    
    # Load the MATLAB file (This is a placeholder for actual loading logic)
    # data = load_matlab_file(input_file)  # Implement this function based on your needs

    # Example data processing (replace with actual processing logic)
    data = {
        'Time': [0, 1, 2, 3],
        'Sensor1': [10, 20, 30, 40],
        'Event': ['Start', 'Middle', 'Middle', 'End']
    }
    
    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Save to CSV
    df.to_csv(output_file, index=False)
    print(f"Data successfully converted to {output_file}")

# Example usage
input_file = 'data_export.mat'  # Replace with your MATLAB file
output_file = 'converted_data.csv'
convert_matlab_to_csv(input_file, output_file)
```

### Contribution
Contributions are welcome! Please feel free to submit issues or pull requests to improve the functionality or documentation of this project.
