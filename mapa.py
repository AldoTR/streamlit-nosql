import streamlit as st
import numpy as np
import pandas as pd

map_data = pd.DataFrame(
     np.random.randn(10, 2) /  [50, 50] + [18.91506, -97.02790],
     columns=['lat', 'lon'])

st.map(map_data)

st.dataframe(map_data)
