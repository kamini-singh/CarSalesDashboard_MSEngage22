import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from PIL import Image
from utilities.add_images import sidebar_bg


def load_view():

 with open('assets/styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

 st.sidebar.header("Select among the following:")
 box1= st.sidebar.checkbox("Show most popular Car specifications", False)
 box2= st.sidebar.checkbox("Show top Manufacturers according to Sales", False) 
 box3= st.sidebar.checkbox("Show Avgerage Price of Car according to Fuel type",False)
 box4= st.sidebar.checkbox("Show Sales according to Car Price range", False)
 box5= st.sidebar.checkbox("Show Male customer VS their preferred Car manufacturer", False)
 box6= st.sidebar.checkbox("Show Female customer VS their preferred Car manufacturer", False)

 df = pd.read_csv('dataset/Cars_cleaned_data.csv')

 if not box1 and not box2 and not box3 and not box4 and not box5 and not box6:
     st.title('Car Features Page')
     st.write("Get to know your customer's preferable car features, Price v/s Category stats and many more insights with one click.")
     st.write("Select any option in the sidebar to display stats.")
     st.image('assets/images/img2.png')

 #1. displaying most popular car specifications: Transmission, Power, Engine CC, Fuel Type
 if box1:
     st.subheader("Most Popular Car Specifications 2021")  
     col1, col2, col3, col4 = st.columns(4)                                                                   
     #Transmission
     df1 = df.groupby(["Transmission"]).Total.sum().reset_index()
     dff1=df1[df1['Total']==df['Total'].max()]
     val=round(dff1.iloc[0,0], 3)
     col1.metric(label="Transmission", value=val)
      
     
     #Power
     df1 = df.groupby(["Power"]).Total.sum().reset_index()
     dff1=df1[df1['Total']==df['Total'].max()]
     val=round(dff1.iloc[0,0], 3)
     col2.metric(label="Power in BHP", value=val)
    
    
    #Engine CC
     df1 = df.groupby(["Engine CC"]).Total.sum().reset_index()
     dff1=df1[df1['Total']==df['Total'].max()]
     val=round(dff1.iloc[0,0], 3)
     col3.metric(label="Engine size in CC", value=val)

    #Fuel Type
     df1 = df.groupby(["Fuel"]).Total.sum().reset_index()
     dff1=df1[df1['Total']==df['Total'].max()]
     #  val=dff1.iloc[0,0]
     col4.metric(label="Fuel", value="Petrol")

#2. For top n brands Chart
 if box2:
     st.header(" ")
     st.subheader("Top Manufacturers according to Sales 2021")  
     number1 = st.slider('How many top manufacturers you want to display', 0, 30, 5)
     df2 = df.groupby(["Manufacturer"]).Total.sum().reset_index()
     df2.sort_values(by='Total', ascending=False, inplace=True)
     df2=df2.head(number1).reset_index()
     top_manufacturers= px.bar(
        df2, 
        x='Manufacturer',
        y='Total',
        labels={'x': 'Manufacturer', 'y':'Total Sales'},
        color='Manufacturer')
     st.plotly_chart(top_manufacturers)

    
#3. Average price of car according to fuel
 if box3:
     st.header(" ")
     st.subheader("Average Price of Car according to Fuel")
     df3= df.groupby('Fuel',as_index=False)['Price'].mean()  
     col1, col2, col3 = st.columns(3) 
     val=round(df3.iloc[0,1], 3)
     col1.metric(label=df3.iloc[0,0], value=('$ %s K' % (val)))

     val=round(df3.iloc[1,1], 3)
     col2.metric(label=df3.iloc[1,0], value=('$ %s K' % (val)))

     val=round(df3.iloc[2,1], 3)
     col3.metric(label=df3.iloc[2,0], value=('$ %s K' % (val)))   
 
#4. Customers V/S Price Range
 if box4:
     st.header(" ")
     st.subheader("No. of Customers V/S Price Range")
     m = df['Price'].max().astype(int)
     new_df1 = pd.DataFrame(columns = ['Range', 'Total Customers'])
     jumps = []
     # creating the jumps (ranges of 5 lakh)
     for item in range(0, m, 5):
       jumps.append([item, item + 5])
     # creating filter for each range
     for item in jumps:
       df4= df[(item[0] <= df['Price']) & (df['Price'] <= item[1])]
       df2 = {'Range': item[1], 'Total Customers':df4.Total.sum() }
       new_df1 = new_df1.append(df2, ignore_index=True)
     #plotting the graph
     fig = px.line(new_df1, x="Range", y="Total Customers")
     st.plotly_chart(fig)
     st.caption("Here 'Range' means car price value in thousand dollars between the 'Range' and 'Range-5'")
     st.caption("Example: Range=30 means Car price lying between 25K to 30K dollars")
       


 #5. Manufacturer V/S Male Customers
 if box5:
     st.header(" ")
     st.subheader("Car Manufacturer V/S No. of Male Customers")
     number2 = st.slider('How many top manufacturers you want to display', 0, 30, 6)
     df_male = df.groupby(["Manufacturer"]).Male.sum().reset_index()
     df_male.sort_values(by='Male', ascending=False, inplace=True)
     df_male=df_male.head(number2).reset_index()
     top_manufacturers_male= px.bar(
        df_male, 
        x='Manufacturer',
        y='Male',
        labels={'x': 'Manufacturer', 'y':'Total Male Customers'},
        color='Manufacturer')
     st.plotly_chart(top_manufacturers_male)

 #6. Manufacturer V/S Female Customers
 if box6:
     st.header(" ")
     st.subheader("Car Manufacturer V/S No. of Female Customers")
     number3 = st.slider('How many top manufacturers you want to display', 0, 30, 10)
     df_female = df.groupby(["Manufacturer"]).Female.sum().reset_index()
     df_female.sort_values(by='Female', ascending=False, inplace=True)
     df_female=df_female.head(number3).reset_index()
     top_manufacturers_female= px.bar(
        df_female, 
        x='Manufacturer',
        y='Female',
        labels={'x': 'Manufacturer', 'y':'Total Female Customers'},
        color='Manufacturer')
     st.plotly_chart(top_manufacturers_female)


 