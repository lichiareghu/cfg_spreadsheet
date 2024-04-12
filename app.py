import streamlit as st
import pandas as pd
from functions import read_data, analyse_data


def main():
    st.title("Spreadsheet Analysis")

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:

        # Read the filename into a dict
        data = read_data(f'data_files/{uploaded_file.name}')

        # Convert the data to a dataframe
        df = pd.DataFrame(data)

        # Display the sample data
        st.subheader("Sample:")
        st.dataframe(df.head(3))

        # Split the layout into two columns
        col1, col2 = st.columns(2)

        # Inputs column
        with col1:
            st.header("Inputs")

            # Create a dropdown button with options
            values_column = st.selectbox("Select the values column", df.columns)
            # grouping_column = st.selectbox("Select the grouping column", df.columns)
            # partition_column = st.selectbox("Select the partition column", df.columns)

            # Define the operations
            operations = ['Total', 'Average', 'Median', 'Minimum', 'Maximum']
            #operation = st.selectbox("Select the operation", operations)
            operation = st.multiselect("Select the operation", operations)

            # Create a button
            button_clicked = st.button("Calculate")

        # Outputs column (aligned to the right)
        with col2:
            st.header("Outputs")
            if button_clicked:
                result_dict = analyse_data(data, values_column, operation)

                # Convert the results into dataframe
                result_df = pd.DataFrame(result_dict.items(), columns=['Operation', 'Results'])

                st.write("Data Analysis")
                st.dataframe(result_df)


if __name__ == "__main__":
    main()
