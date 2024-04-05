import streamlit as st
import pandas as pd
from monthly_sales import calculate_sales
from read_file import read_data

def main():
    st.title("CSV File Upload and Display")

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        #data = read_data(uploaded_file)
        st.subheader("CSV File Contents:")
        st.dataframe(df.head(10))

        #st.subheader("Calculations:")
        #len,sales = calculate_sales(df)
        #st.write(f'sales_figures:{sales}')
        user_input = st.text_input("Enter some text:")
        total_sales = df[user_input].sum()
        #total_sales = calculate_sales()
        #st.write(f'The total sales across all {len(total_sales)} months is {sum(total_sales)}.')


if __name__ == "__main__":
    main()
