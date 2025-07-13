import streamlit as st
import pandas as pd
import numpy as np

# Set the title of the web app
st.title("My First Streamlit Web App")

# Display a simple text message
st.write("Hello, World!")

# Create a simple DataFrame
df = pd.DataFrame({"Column 1": [1, 2, 3, 4, 5], "Column 2": [10, 20, 30, 40, 50]})

# Display the DataFrame in the app
st.write("Here is the DataFrame:")
st.write(df)

# create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3), columns=["Column A", "Column B", "Column C"]
)
st.line_chart(chart_data)