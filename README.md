# Fun_with_Flora

Developed a Web Application leveraging camera technology to recognize plants, providing insights into their health and rarity with a remarkable 90% success rate. 
Created two projects using Django and Flask frameworks, orchestrating end-to-end development processes. 
Crafted intuitive frontends utilizing HTML / CSS / Javascript and parsed data through JSON.

Fun With Flora!

Advanced Python Project Documentation - Advanced Java Topics

Abdurrahman Raza, Sambhav Agarwal, Samarth Hiremath, Yash Natu
Period 8

- What is Fun With Flora?

Going on a stroll and come across this beautiful flower you have never seen before and want to know more about? No problem! Just point your camera at the plant, and Fun With Flora will provide relevant information about the plant within seconds, including the name, scientific name, health status, potential diseases and much more about the plant. It is an interactive, easily accessible tool that anyone can use. These past few decades have shifted our focus away from nature, and the general public is typically unaware of the vast, exclusive flora they live and breathe. Fun With Flora aims to bring this awareness back, helping the general public slowly be more aware of their surroundings and encourage a form of positive action to save it, as not just flora, but fauna also define a part of this beautiful planet’s future. 
____________________________________________________________________________________

- How does our program work?

A combination of HTML, Flask, and APIs helped bring Fun With Flora to life. Our first step was to design a web application that implemented a camera on the website. We incorporated a webcam using javascript that helped us collect the data and save the data as base64. It was implemented in the HTML/CSS Template for “Project_Camerapage.html”. While the camera API helped us collect the data, we wanted to use the Plant.AI API that identified the plant. To accomplish that, we hosted Flask, a web application framework written in Python. Flask helped us route all our websites together and send the camera data to the Plant.AI API in Python.  

Once the base64 data reached the API, it sent a “GET” request, which the API returned JSON data. Finally, we were able to parse through the data and identified all the data that we required. We used Flask to send the data to “Project_Results.html” and were able to display the plant details on the third page. It all started from taking a picture on the website, and we were able to analyze the data and use respective APIs to display the plant information.
____________________________________________________________________________________

- What did we learn?

Each individual member of the team was to learn at least one unique team from this project. 
Sambhav was able to learn how to implement an API, relearn how to use a flask framework, route all the websites and send data between each website, and parse through JSON data. 
Samarth was able to touch up his skills in JavaScript and learn how to implement a camera using JS. He was also able to learn how to convert data into base64.
Abdurrahman was able to learn how to develop a website. He was responsible for designing the User interface and implementing all the data that was being sent to the HTML pages.
Yash was able to learn CSS and how to style a website regardless of the size of the display. 
____________________________________________________________________________________

- How did each member contribute to the project?

Front-end development: Abdurrahman and Yash
Writing HTML code
Finding relevant background images
Searching and using templates as inspiration
Setting up and formatting website for descriptions, camera section, and results section 
Coding templates to make the User Interface engaging

Back-end development: Sambhav and Samarth
Implementing relevant camera and plant APIs
Adding Flask (Python Framework) into the website for routing functionality
Linking the pages to create a fluid user interface and experience
Implementing the Plant.AI API and sending the camera data to the API
Converting the data into Base64
Receiving JSON data from the Plant.AI API and parsing through it for relevant information
Store the data and route the data to another page
