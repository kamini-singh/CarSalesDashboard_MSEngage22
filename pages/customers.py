from operator import index
from pyexpat import model
import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt


def load_view():
 
 manufacturer ='Alfa-Romeo' # Pick some initial values.
 df = pd.read_csv('dataset/Cars_cleaned_data.csv')
 
 #sidebar to take input
 st.sidebar.title("Show Analysis based on Manufacturer")
 st.sidebar.text(" ")

 #saving the input
 manufacturer = st.sidebar.selectbox('Select a Manufacturer Name',df['Manufacturer'].unique().tolist())
 st.header(" 📈 Analysis of the Car brand '%s'" % (manufacturer))

 def get_all_models():
    filter = df['Manufacturer']==manufacturer
    new_dataframe = pd.DataFrame({
    'Model Name': df['Model'].where(filter),
    'Total Sales': df['Total']})
    return new_dataframe

 new_df = get_all_models()
 new_df=new_df.dropna()


 #plotting graph of model against total sales
 #1 Model VS Total Sales
 model_stats_graph = px.bar(
        new_df, 
        x='Model Name',
        y='Total Sales',
        labels={'Total Sales in 2022':'Total Sales for %s' % (manufacturer)},
        color='Model Name')
 st.plotly_chart(model_stats_graph)

 st.write("According to the dataset, most Popular model of the manufacturer  %s is: " % (manufacturer))
 df2=new_df[new_df['Total Sales']==new_df['Total Sales'].max()]
 st.write(df2)
 
 #2 Pie chart of customer distribution

 filter = df['Manufacturer']==manufacturer
 df3 = pd.DataFrame({
    'Male Customers': df['Male'].where(filter),
    'Female Customers': df['Female'].where(filter),
    'Unknown': df['Unknown'].where(filter)})

 df3.dropna()
 dataframe_sum = df3.sum()
 male=df3['Male Customers'].sum()
 female=df3['Female Customers'].sum()
 unknown=df3['Unknown'].sum()

 customer_category=['Male Customers', 'Female Customers', 'Unknown']
 values = [male, female, unknown]
 
 fig = go.Figure(
    go.Pie(
    labels = customer_category,
    values = values,
    hoverinfo = "label+percent",
    textinfo = "value"
  ))
 st.write(" ")
 st.header(" 📈 Customer Segment demonstration of '%s' : " % (manufacturer))
 st.plotly_chart(fig)
 st.write("According to current stats the customer distribution is as follows:")
 st.write(dataframe_sum)


