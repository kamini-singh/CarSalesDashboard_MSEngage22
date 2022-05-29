 <h1 align="center"> Car Sales Dashboard :oncoming_automobile: </h1> 
 
 <p align="center"> 
 <a target="_blank" href="https://carsales-dashboard.herokuapp.com/">Link to the Website </a>
    ||
 <a target="_blank" href="#"> Video Demo</a>
</p>

<!-- TABLE OF CONTENTS -->
## About the Project

- Car Sales Dashboard created during Microsoft Engage 2022.
- A Web App that predicts Car prices and helps visualize various sales stats of the Car Industry.

### Salient Features

- Car Price Prediction using Machine Learning model.
- Visualizing top Car features with the help of line graphs and charts.
- Visualizing brand-wise top car models and Customer segments.

### Compatible Platforms
 - Laptops, Desktops and Tablet PCs

### Built With
* ![Front-end][front-end-shield]
* ![Back-end][back-end-shield]
* ![Tools][tools-shield]
* [Dataset Used](https://www.kaggle.com/datasets/brijlaldhankour/car-buyers)


### Run Locally

To separately run the Web application on your local host, perform the following steps:

Install the following dependencies separately:

```bash
  pip install streamlit
  pip install plotly_express==0.4.0
  pip install -U scikit-learn
  pip install protobuf~=3.19.0
```

Start the server

```bash
  streamlit run app.py
```

## Navigating through the App
- Car Price Prediction Model

![Screenshot (112)](https://user-images.githubusercontent.com/78756272/170863719-316676f6-d3c7-48be-a499-fc1ea5d48834.png)

- Visualizing various Car Features based on Sales
 
![Screenshot (114)](https://user-images.githubusercontent.com/78756272/170863796-c214806d-23a4-4c60-b2d7-34de904d1f7c.png)
![Screenshot (113)](https://user-images.githubusercontent.com/78756272/170863797-b44f5513-d131-4efd-bc2a-dc5571d8c85a.png)

- Visualizing Brand-wise model popularity and Customer segmentation

![Screenshot (113)](https://user-images.githubusercontent.com/78756272/170863723-c77a6f23-1b8f-40ad-b840-3ba40f24038f.png)
![Screenshot (116)](https://user-images.githubusercontent.com/78756272/170863731-f604b6dc-cab2-4f63-8bc8-578dbe73ab60.png)


### Directory Tree 
```![Screenshot (115)](https://user-images.githubusercontent.com/78756272/170863727-cd798353-bcee-461a-8088-1dfdf9537bf3.png)

├── .streamlit 
│   ├── config.toml
├── assets 
│   ├── images
│   ├── styles.css
├── dataset
│   ├── CarBuyers.csv
│   ├── Cars_cleaned_data.csv
├── pages
│   ├── home_page.py
│   ├── car_features.py![Screenshot (114)](https://user-images.githubusercontent.com/78756272/170863725-bb470f40-6d82-477c-96bf-418e8b632e42.png)

│   ├── customers.py
├── Utilities
│   ├── navbar.py
│   ├── add_images.py
│   ├── paths.py
├── Procfile (for deployment)
├── README.md
├── app.py
├── carsales.ipynb
├── carsales.pkl
├── requirements.txt (for deployment)
```


<!--MARKDOWN LINKS-->
[front-end-shield]: https://img.shields.io/badge/Front--end-Streamlit-blue
[back-end-shield]: https://img.shields.io/badge/Back--end-Python-blue
[tools-shield]: https://img.shields.io/badge/Tools-Jupyter%20Notebook-blue



