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


def get_profile(df):
    """
    This function collects the data in a dataframe and generates a profile for the data
    :param df: Input data frame
    :return: Dict of summary
    """
    # Prepare a dataframe to assemble the numerical data alone (The data that can be used for calculations),
    # everything else must return a zero
    df_numeric = pd.DataFrame(columns=df.columns)

    for i in df.columns:
        # Populate the values for df_numeric
        df_numeric[i] = collect_numerical(df[i].tolist())

    # Fill the nan values with zero for ease of calculation
    df_numeric = df_numeric.fillna(0)

    # Populate the results
    result = {'Columns': [i for i in df.columns],
              'Data Type': [df[i].dtype.name for i in df],
              'No of values': [len(df[i].dropna()) for i in df],
              'No of missing values': [df[i].isna().sum() for i in df],
              'No of unique values': [len(df[i].unique()) for i in df],
              'Maximum value': [df_numeric[i].max() for i in df_numeric],
              'Minimum value': [df_numeric[i].min() for i in df_numeric],
              'Mean_func': [round(df_numeric[i].mean(), 2) for i in df_numeric],
              'Variance': [round(variance(df_numeric[i]), 2) for i in df_numeric],
              'Std_dev_func': [round(df_numeric[i].std(), 2) for i in df_numeric],
              'Range': [round(range_of_data(df_numeric[i]), 2) for i in df_numeric]
              #'Quantile': [df_numeric[i].quantile([.25, .5, .75]),
              # if df[i].dtype.name != 'object' else 0 for i in df]
              }

    # Convert the results to dataframe
    result = pd.DataFrame(result, columns=result.keys())
    return result


def collect_numerical(data):
    # collect only float and int values
    tmp = []
    for item in data:
        if (isinstance(item, int) or isinstance(item, float)):
            tmp.append(item)
        else:
            tmp.append(0)
    return tmp


def variance(data):
    """
    This function takes a list of values and returns the variance
    input : list of values
    output : float
    """
    result = 0
    if len(data) != 0:
        average = sum(data) / len(data)
        result = sum((x - average) ** 2 for x in data) / len(data)
    return result


def range_of_data(data):
    """
    This function takes a list of values and returns the range
    input : list of values
    output : int or float
    """
    return max(data) - min(data)


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

    # Convert the results into dataframe
    result_df = pd.DataFrame(result_data, columns=['Operation', 'Group', values_column.capitalize()])

    # Return the data
    return result_df

def get_result(values, operation):
    """Get the values. Perform the operation. return the result
    inputs: values-> 'list' of values to perform the operation on
            operation-> 'str' type name of the operation
    outputs: result-> 'float' value which is the results of the operation
    """

    result = 0
    values = pd.Series(collect_numerical(values))

    if operation == 'Total':
        result = values.sum()  # Write a function to add all values
    if operation == 'Average':
        result = values.mean()  # Write a function to find the average
    if operation == 'Median':
        result = values.median()  # Write a function to find the median
    if operation == 'Minimum':
        result = values.min()  # Write a function to find the Minimum
    if operation == 'Maximum':
        result = values.max()  # Write a function to find the Maximum
    if operation == 'Count':
        result = len(values)
    return result


def save_results(df,filename):
    """
    Saves the results as csv
    :param df: Dataframe containing the results
    :return: "Saved successfully"
    """
    df.to_csv(f"data_files/results/{filename}",index=False)
    return "File saved successfully"

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
    for i in range(1, len(data)):
        previous_month = float(data[i - 1][values_column])
        current_month = float(data[i][values_column])
        if previous_month and previous_month != 0:
            change_as_percentage = round(((current_month - previous_month) / previous_month) * 100, 2)
        else:
            change_as_percentage = 0
        list_changes.append(change_as_percentage)
    return list_changes