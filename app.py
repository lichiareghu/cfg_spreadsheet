import streamlit as st
import pandas as pd
from functions import (read_data,
                       analyse_data,
                       percentage_change,
                       get_profile)


def main():
    st.title("Spreadsheet Analysis")

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:

        # Read the filename into a dict
        data = read_data(f'data_files/{uploaded_file.name}')

        # Read the data to a dataframe
        df = pd.read_csv(f'data_files/{uploaded_file.name}')

        # Generate profile
        profile = get_profile(df)

        # Convert the dict in to dataframe
        profile_df = pd.DataFrame(profile)

        # Display the data profile
        st.subheader("Profile:")
        st.dataframe(profile_df)

        # Split the layout into two columns
        col1, col2 = st.columns(2)

        # Inputs column
        with col1:
            st.header("Data Analysis")

            # Create a dropdown button with options
            options = df.columns
            values_column = st.selectbox("Select the values column", options)
            grouping_column = st.selectbox("Select the grouping column", options, index=None)
            # partition_column = st.selectbox("Select the partition column", df.columns)

            # Define the operations
            operations = ['Total', 'Average', 'Median', 'Minimum', 'Maximum']
            # operation = st.selectbox("Select the operation", operations)
            operation = st.multiselect("Select the operation", operations)

            # Create a button
            button_clicked = st.button("Calculate")

        # Outputs column
        with col2:
            st.header("Outputs")
            if button_clicked:

                result = analyse_data(data, values_column, operation, grouping_column)

                # Convert the results into dataframe
                result_df = pd.DataFrame(result, columns=['Operation', 'Group',values_column.capitalize()])

                # st.write("Data Analysis")
                st.dataframe(result_df)

        # Display percentage change
        st.subheader("Percentage change")
        # Create a button
        button_clicked2 = st.button("Get % Change")
        if button_clicked2:
            df['change'] = percentage_change(data, values_column)
            st.dataframe(df[[grouping_column, values_column, 'change']])

        # Display the graph
        st.subheader("Plot Graph")

        # Create a dropdown button with options
        # graph_options = st.selectbox("Select the type of graph", ['Percentage change', 'Simple Plot'])

        # if graph_options == 'Simple Plot':
        x = st.selectbox("Choose X axis", df.columns)
        y = st.selectbox("Choose Y axis", df.columns)
        z = st.selectbox("Choose colour", df.columns)
        button_clicked3 = st.button("Plot")
        if button_clicked3:
            st.scatter_chart(
                    df,
                    x=x,
                    y=y,
                    color=z
                )


if __name__ == "__main__":
    main()
