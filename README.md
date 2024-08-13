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
python labview_csv_convertor.py input_file.mat output_file.csv
```

### Example Jupyter Notebook



### Contribution
Contributions are welcome! Please feel free to submit issues or pull requests to improve the functionality or documentation of this project.
