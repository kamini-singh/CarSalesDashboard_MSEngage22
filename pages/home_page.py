import streamlit as st
import streamlit as st
import pandas as pd
import numpy as np
import joblib
from utilities.add_images import set_bg_img

def load_view():
   set_bg_img('assets/images/car1.png')

   st.subheader("Our website is one-stop destination to obtain all the industry insights!")
   
  #loading the dataset.
   car = pd.read_csv('dataset/CarBuyers.csv')

   brand_list = ['Alfa-Romeo',
   'Aston-Martin',
   'Audi', 
   'BMW',
   'Bentley', 
   'Chevrolet', 
   'Chrysler',
   'Citroen',
   'Dacia',
   'Daewoo',
   'Daihatsu',
   'Daimler',
   'Datsun',
   'Dodge', 
   'Ferrari', 
   'Fiat', 
   'Ford',
   'Honda',
   'Hyundai',
   'Jaguar',
   'Kia', 
   'Lada',
   'Lancia',
   'Land-Rover',
   'Lexus',
   'Lotus',
   'MG', 
   'Maserati', 
   'Mazda',
   'Mercedes', 
   'Mini', 
   'Mitsubishi', 
   'Morris', 
   'Nissan',
   'Opel',
   'Peugeot',
   'Porsche', 
   'Renault',
   'Rover', 
   'Saab', 
   'Seat', 
   'Skoda',
   'Smart', 
   'Ssangyong', 
   'Subaru', 
   'Suzuki', 
   'TVR', 
   'Toyota', 
   'Triumph',
   'Volkswagen', 
   'Volvo',
   'Abarth',]

   fuel_type_list= ['Diesel','Petrol','Automatic']

 #loading the model
   @st.cache(allow_output_mutation=True)
   def model_loader(path):
       model = joblib.load(path)
       return model


 #loading both models
   with st.spinner('Hold on, the app is loading !!'):
       model_forest = model_loader("carsales.pickle")


   col1, col2 = st.columns((0.6, 0.5))
   with col2:
    st.write(" ")
#Column 1
   with col1:
      st.title('Car Price Prediction')
  #start taking inputs
     #1. Manufacturer name
      manufacturer= st.selectbox(label='Enter the Brand of the car', options=brand_list, help='From which brand the car belongs?')    #passing the brand list
      manufacturer= brand_list.index(manufacturer)    #converting the brand name to numerical encoding form

     #2. Transmission
      transmission= st.number_input(label='Enter the Transmission', help='Example: 5.7')

     #3. Engine CC
      engine= st.number_input(label='Enter the Engine Size in CC', help='Example: 1560')

     #4. Power
      power = st.number_input(label='Enter the Power of the Car in BHP.', help='Example: 85')
     #5. Fuel Type
      fuel_type = st.selectbox(label='Enter the Fuel Type', options=fuel_type_list, help='Example: Petrol')
      fuel_type = fuel_type_list.index(fuel_type)


    #creatng a input array for prediction
      inp_array = np.array([transmission, power, engine])
      for i in range(0,51):
       if i==manufacturer:
         inp_array=np.append(inp_array, [1])
       else:
         inp_array=np.append(inp_array, [0])

      for i in range(0, 2):
       if i==fuel_type:
         inp_array= np.append(inp_array, [1])
       else:
         inp_array= np.append(inp_array, [0])

      predict = st.button('Predict')  #creating a predict buutton
      print(inp_array)
      if predict: 
           pred = model_forest.predict([inp_array])
           if pred < 0:    #handeling negative outputs.
               st.error('The input values must be irrelevant, try again by giving relevent information.')
           else:
              pred = round(float(pred),3)
              write = 'The predicted price of the car is $ '+ str(pred) +'K'
              st.success(write)
