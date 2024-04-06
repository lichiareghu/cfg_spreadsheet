import pandas as pd

data = pd.read_csv('D:\CFG_Spreadsheet\cfg_spreadsheet\sales.csv')
print(data[0:2])


import streamlit as st
import pandas as pd
from functions import read_data, collect_data

def main():
    st.title("Spreadsheet Analysis")

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        # Read the filename
        data = read_data(uploaded_file.name)

        # Convert the data to a dataframe
        df = pd.DataFrame(data)

        st.subheader("Sample:")
        st.dataframe(df.head(3))

        # Create a dropdown button with options
        values_column = st.selectbox("Select the values column", df.columns)
        #grouping_column = st.selectbox("Select the grouping column", df.columns)
        #partition_column = st.selectbox("Select the partition column", df.columns)

        # Define the operations
        operations = ['Total', 'Average', 'Median', 'Minimum', 'Maximum']
        operation = st.multiselect("Select the operation", operations)

        # Create a button
        button_clicked = st.button("Calculate")

        # Check if the button is clicked
        if button_clicked:
            # Get the results as dict
            workable_data = collect_data(data, values_column)

            # Convert the results into dataframe
            result_df = pd.DataFrame(workable_data)
            st.write("Collected Data")
            st.dataframe(result_df)

if __name__ == "__main__":
    main()
