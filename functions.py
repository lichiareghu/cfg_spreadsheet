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


def convert_values(data, values_column):
    """Takes an input dict, converts the value to numbers saves the new value and returns the dict
    inputs: data -> 'Dict'
            values_column -> 'list'
    output: 'Dict''"""
    for row in data:
        row[values_column] = float(row[values_column])
    return data


def collect_data(data, value_column, grouping_column=None):
    """Collect the values from a column and return it
    inputs: data-> dict of keys and values
            value_column-> 'str' type key in data to be used for collecting values
            grouping_column-> 'str' type key to be used for grouping the data to be collected
    outputs: collected_data-> 'dict' with group names as keys and numeric values"""
    collected_data = {}
    df = pd.DataFrame(data)
    df[value_column] = [float(i) for i in df[value_column]]
    if grouping_column:
        groups = set(df[grouping_column])
        for group in groups:
            grp = df.loc[df[grouping_column] == group, value_column].tolist()
            collected_data[group] = grp
    else:
        collected_data[value_column] = df[value_column].tolist()
    return collected_data


def analyse_data(data, values_column, operation, grouping_column=None):
    """Complete analysis and return result
    inputs: data-> dict of column names and values
            values_column-> 'str' type name of the column to be used for numerical calculations
            operation-> 'list' type value representing the names of the operation
            grouping_column-> 'str' type key to be used for grouping the data to be collected
    outputs: result_data-> list of lists arranged in the order [operation,group,result]"""
    # Initialise the result dict
    result_data = []

    # Get the results as list
    workable_data = collect_data(data, values_column, grouping_column)

    # Iterate through the list of operations and get the results
    for op in operation:
        for group, data in workable_data.items():
            result = get_result(data, op)
            result_data.append([op, group, result])

    # Return the data
    return result_data


def collect_numerical(data):
    # collect only float and int values which are not null
    tmp = []
    for item in data:
        if isinstance(item, int) or isinstance(item, float):
            tmp.append(item)
        else:
            tmp.append(0)
    return tmp


def get_result(values, operation):
    """Get the values. Perform the operation. return the result
    inputs: values-> 'list' of values to perform the operation on
            operation-> 'str' type name of the operation
    outputs: result-> 'float' value which is the results of the operation
    """

    result = 0
    values = collect_numerical(values)

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
    total = 0
    for i in range(len(data)):
        total = total + data[i]
    return total



def average(data):
    # input: list of values
    # output: float
    return round(sum(data) / len(data), 2)



def median(data):

    """input: list of values
            output: float
        """
    sorted_data = sorted(data)
    length = len(sorted_data)
    if length % 2 == 0:
        return round((sorted_data[length // 2 - 1] + sorted_data[length // 2]) / 2, 2)
    else:
        return round(sorted_data[length // 2], 2)



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


def percentage_change(data, values_column):
    """
    This function takes a dict of data and a grouping column and a value column. It then returns the percentage change
    input :
    data: dict of values
    grouping_column: str
    values_column: str
    output : dict of values
    """
    list_changes = [0]
    data = convert_values(data, values_column)
    for i in range(1, len(data)):
        previous_month = float(data[i - 1][values_column])
        current_month = float(data[i][values_column])
        if previous_month and previous_month != 0:
            change_as_percentage = round(((current_month - previous_month) / previous_month) * 100, 2)
        else:
            change_as_percentage = 0
        list_changes.append(change_as_percentage)
    return list_changes


def get_profile(df):
    """
    This function collects the data in a dataframe and generates a profile for the data
    :param df: Input data frame
    :return: Dict of summary
    """
    df_numeric = pd.DataFrame(columns=df.columns)
    for i in df.columns:
        df_numeric[i] = collect_numerical(df[i].tolist())
    result = {'Columns': [i for i in df.columns],
              'Data Type': [df[i].dtype.name for i in df],
              'No of values': [len(df[i].dropna()) for i in df],
              'No of missing values': [df[i].isna().sum() for i in df],
              'No of unique values': [len(df[i].unique()) for i in df],
              'Maximum value': [maximum(df_numeric[i].tolist()) for i in df],
              'Minimum value': [minimum(df_numeric[i].tolist()) for i in df],
              'Mean': [round(df[df[i].notna()][i].mean(), 2) if df[i].dtype.name != 'object' else 0 for i in df],
              'Std_dev': [round(df[df[i].notna()][i].std(), 2) if df[i].dtype.name != 'object' else 0 for i in df]
              # ,'Quantile': [df[df[i].notna()][i].quantile([.25, .5, .75])
              # if df[i].dtype.name != 'object' else 0 for i in df]
              }
    return result
