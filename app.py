import streamlit as st
import pandas as pd
from functions import (read_data,
                       analyse_data,
                       save_results,
                       percentage_change,
                       get_profile)


def main():
    st.title("Spreadsheet Analysis")

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:

        # Read data as a dict
        data = read_data(f'data_files/{uploaded_file.name}')

        # Read the data to a dataframe
        df = pd.read_csv(f'data_files/{uploaded_file.name}')

        # Generate profile
        profile_df = get_profile(df)

        # Display the data profile
        st.subheader("Profile:")
        st.dataframe(profile_df)

        # Create button to save summary
        save_analysis = st.button("Save Summary")

        # Save the summary
        if save_analysis:
            tmp = save_results(profile_df,"Profile_Summary.csv")
            st.write(tmp)

        # Split the layout into two columns
        col1, col2 = st.columns(2)

        # Inputs column
        with col1:
            st.subheader("Data Groups Analysis:")

            # Create a dropdown button with options
            options = df.columns
            values_column = st.selectbox("Select the values column (values must be int or float values)", options)
            grouping_column = st.selectbox("Select the grouping column (Columns which gropus the values like a country or a year or a month)", options, index=None)
            # partition_column = st.selectbox("Select the partition column", df.columns)

            # Define the operations
            operations = ['Total', 'Average', 'Median', 'Minimum', 'Maximum', 'Count']
            # operation = st.selectbox("Select the operation you want to perfom on the groups", operations)
            operation = st.multiselect("Select the operation you want to perfom on the groups", operations)

            # Create a button
            button_clicked = st.button("Calculate")


        # Outputs column
        with col2:
            st.subheader("Outputs:")
            if button_clicked:

                result_df = analyse_data(data, values_column, operation, grouping_column)

                # st.write("Data Analysis")
                st.dataframe(result_df)

        # Display percentage change
        st.subheader("Percentage change:")
        # Create a button
        button_clicked2 = st.button("Get % Change")
        if button_clicked2:
            df['change'] = percentage_change(data, values_column)
            st.dataframe(df[[values_column, 'change']])
        #
        # Display the graph
        st.subheader("Plot Graph:")

        # Drop the nan values
        df_clean = df.dropna(axis=0)

        # if graph_options == 'Simple Plot':
        x = st.selectbox("Choose X axis", df_clean.columns)
        y = st.selectbox("Choose Y axis", df_clean.columns)
        z = st.selectbox("Choose colour", df_clean.columns)
        button_clicked3 = st.button("Plot")
        if button_clicked3:
            st.scatter_chart(
                    df_clean,
                    x=x,
                    y=y,
                    color=z
                )


if __name__ == "__main__":
    main()
