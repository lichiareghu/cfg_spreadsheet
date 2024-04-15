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
        collected_data.append(float(value))
    return collected_data


def analyse_data(data, values_column, operation):
    """Complete analysis and return result
    inputs: data-> dict of column names and values
            values_column-> 'str' type name of the column to be used for numerical calculations
            operation-> 'list' type value representing the names of the operation
    outputs: result_data-> Dict with keys as operation and results as values"""
    # Initialise the result dict
    result_data = {}

    # Get the results as list
    workable_data = collect_data(data, values_column)

    # Iterate through the list of operations and get the results
    for op in operation:
        result_data[op] = get_result(workable_data, op)

    # Return the data
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
    # input: list of values
    # output: float
    return sum(data)/len(data)


def median(data):
    # input: list of values
    # output: float
    sorted_data = sorted(data)
    length = len(sorted_data)
    if length % 2 == 0:
        return (sorted_data[length // 2 - 1] + sorted_data[length // 2]) / 2
    else:
        return sorted_data[length // 2]


print(median([4,5]))


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


def range_of_data(data):
    """
    This function takes a list of values and returns the range
    input : list of values
    output : int or float
    """
    return max(data) - min(data)


def variance(data):
    """
    This function takes a list of values and returns the variance
    input : list of values
    output : float
    """
    average = sum(data) / len(data)
    return sum((x - average) ** 2 for x in data) / len(data)


def standard_deviation(data):
    """
    This function takes a list of values and returns the standard deviation
    input : list of values
    output : float
    """
    return variance(data) ** 0.5
