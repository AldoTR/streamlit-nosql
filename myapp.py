import streamlit as st
import numpy as np

st.title("My first streamlit app")

x = st.slider('Select a value for x', 0.0, 10.0, 5.0)

x_values = np.linspac(0, 10, 100)
y_values = np.sin(x_values * x)
plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = sin(x * {})'.format(x))
st.pyplot()

st.write("Welcome to my streamlit app")

