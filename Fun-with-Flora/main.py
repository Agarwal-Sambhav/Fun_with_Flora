#importing all relevant libraries
from flask import Flask, render_template, request
import base64
import requests
from time import sleep
#from . import forms, urls
import base64
from io import BytesIO
import requests

#setting up the flask framework
app = Flask(__name__)


#setting the initial routing to when the website is opened. This will cause it to render the "index.html" template.
@app.route('/')
def index():
  return render_template ('index.html')

 #When "/camera" is routed in the URL, it would render the template Project_CameraPage. 
@app.route('/camera', methods =["GET", "POST"])
def camera():

  #if the submit button is pressed
  if (request.method == "POST"):
    base_64 = request.form['projectFilepath']

    #It will access the APIs
    response = requests.post(
        "https://api.plant.id/v2/identify",
        json={
            "images": [base_64],
            "modifiers": ["similar_images"],
            "plant_details": ["common_names", "url"],
        },
        headers={
            "Content-Type": "application/json",
            "Api-Key": "rlgTNY8TSLivgT1UZ4uxqcK4yk6jTbNUOazlOd6t7D2TGuwjcJ"
            ,
        }).json()

#Alternate API Key:
#g5F5Bk4BjjTkwJhGL0igPk47BGrZhIDzJtUN76H7zMqsV1DIky
#qkso8wh3wXTBTtEWp17UB86fezs2wicLEEyGpBbAbacFTw6V7d"
#rlgTNY8TSLivgT1UZ4uxqcK4yk6jTbNUOazlOd6t7D2TGuwjcJ

    #second API
    response_health = requests.post(
    "https://api.plant.id/v2/health_assessment",
    json={
        "images": [base_64],
        "modifiers": ["similar_images"],
        "disease_details": ["description", "treatment"],
    },
    headers={
        "Content-Type": "application/json",
        "Api-Key": "rlgTNY8TSLivgT1UZ4uxqcK4yk6jTbNUOazlOd6t7D2TGuwjcJ",
    }).json()

    #parses through JSON to identify multiple things about the plant. The data about the plant is stored in Base 64 data.
    is_healthy = response_health["health_assessment"]["is_healthy"]
    is_healthy_probability = (str(float(response_health["health_assessment"]["is_healthy_probability"])*100) + "%")
    
    #uses try logic becauses not all plants have diseases
    try:
      diseases = response_health["health_assessment"]["diseases"][0]["disease_details"]["description"]
    
      prevention = response_health["health_assessment"]["diseases"][0]["disease_details"]["treatment"]["prevention"][0]
    except: 
      diseases = "none detected"
      prevention = "none required"


      
    #I am using try logic to check if it throws an error, that means that the object could not be recognized as no data was returned
    try:
    #finds all the common names of the plant by parsing through the JSON
      common_names = ""
      common_names_string = response["suggestions"][0]["plant_details"]["common_names"]
      for x in range(len(common_names_string)):
        if (x == len(common_names_string) - 2):
          common_names += response["suggestions"][0]["plant_details"]["common_names"][x] + ", "
        else:
          common_names += response["suggestions"][0]["plant_details"]["common_names"][x]
  
      #uses the base 64 data to identify scientific name
      scientific_name = response["suggestions"][0]["plant_details"]["scientific_name"]
      wiki_link = response["suggestions"][0]["plant_details"]["url"]
      probability = (str(float(response["suggestions"][0]["probability"])*100) + "%")

    except:
        common_names = "could not identify"
        scientific_name = "could not identify"
        wiki_link = "could not identify"
        probability = "could not identify"

    #Once the submit button is pressed, it identifies all the data and assigns them to variables and renders Project_Results.html
    return render_template("Project_Results.html", common_names = common_names, scientific_name = scientific_name, wiki_link = wiki_link, probability = probability, is_healthy = is_healthy, is_healthy_probability = is_healthy_probability, diseases = diseases, prevention = prevention)


  #If the submit button hasn't been pressed yet, it will render Project_camerapage  
  else:
      return render_template ('Project_Camerapage.html')

#This routes the page to the results page
@app.route('/results')
def results():
  return render_template('Project_Results.html')

app.run(host='0.0.0.0', port=81)

