import csv
import pandas as pd


def read_data(file):
    """ Takes a file path and reads the data in the file into a dict
    input: file-> 'str' value which is the file path
    output: data-> 'dict' value with column names as keys and data as values"""
    data = []
    with open(file, 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)
    return data


def collect_data(data, values):
    """Collect the values from a column and return it
    inputs: data-> dict of keys and values
            values-> 'str' type key in data to be used for collecting values
    outputs: collected_data-> 'list' with numeric values"""
    collected_data = []
    for row in data:
        value = row[values]
        collected_data.append(value)
    return collected_data


def analyse_data(data, values_column, operation):
    """Complete analysis and return result
    inputs: data-> dict of column names and values
            values_column-> 'str' type name of the column to be used for numerical calculations
            operation-> 'str' type value representing the names of the operation
    outputs: result_data-> Dict with keys as operation and results as values"""
    # Initialise the result dict
    result_data = {}

    # Get the results as list
    workable_data = collect_data(data, values_column)

    # Get the results
    result_data[operation] = get_result(workable_data, operation)

    return result_data


def get_result(values, operation):
    """Get the values. Perform the operation. return the result
    inputs: values-> 'list' of values to perform the operation on
            operation-> 'str' type name of the operation
    outputs: result-> 'float' value which is the results of the operation
    """

    result = 0

    if operation == 'Total':
        result = total(values)  # Write a function to add all values
    if operation == 'Average':
        result = average(values)  # Write a function to find the average
    if operation == 'Median':
        result = median(values)  # Write a function to find the median
    if operation == 'Minimum':
        result = minimum(values)  # Write a function to find the Minimum
    if operation == 'Maximum':
        result = maximum(values)  # Write a function to find the Maximum
    return result


def total(data):
    """
    This function takes a list of values and returns the total
    input : list of values
    output : int or float
    """
    return sum(data)

def average(data):
    result = 0
    return result


def median(data):
    result = 0
    return result


def minimum(data):
    """
    This function takes a list of values and returns the minimum
    input : list of values
    output : int or float
    """
    return min(data)


def maximum(data):
    """
    This function takes a list of values and returns the maximum
    input : list of values
    output : int or float
    """
    return max(data)


