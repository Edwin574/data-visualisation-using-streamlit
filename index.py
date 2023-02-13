import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.write('My first streamlit app')

df = pd.read_csv('gapminder_with_codes.csv')

data_2007 = df[df['year'] == 2007]

st.dataframe(data_2007)
fig,ax=plt.subplots()

sns.set_theme()
violin_data=[]
violin_data.append(data_2007['gdpPercap'])
violin_data.append(data_2007['pop'])
violin_data.append(data_2007['lifeExp'])
sns.violinplot(data=violin_data,palette='light:r',inner='box',orient='h',scale='count',gridsize=150,ax=ax)

st.pyplot(fig)
