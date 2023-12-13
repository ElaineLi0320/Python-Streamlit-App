# Python-Streamlit-App
Overall Design
Summary:
Looking for a museum experience without leaving home? This application provides an easy-approached website for users to explore the exhibits of the Metropolitan Museum of Art. By using the museum’s open API, the app will provide a rich, educational, and user-friendly experience, making arts more accessible and interesting. The app has three features: random display, data visualization and a quick quiz.
Purpose:
The purpose of this app is to bridge the gap between the public and the museum’s resources, creating an online platform where art, history and culture could be appreciated by everyone, anywhere, anytime.
End Users:
This application is made for art lovers, students, educators, and anyone who want to explore the Metropolitan Museum of Art's collections from anywhere.

Description of the REST API
Name:
The metropolitan museum of art collection API
URL:
https://github.com/metmuseum/openaccess
Documentation:
https://metmuseum.github.io
Description:
I will fetch data about artworks from the metropolitan museum of art collection API. I will use the data to do a random display of highlighted artworks, perform data visualization and creating quiz questions.
Endpoints:
‘/objects’ – get a list of all valid object ids.
‘/objects/[objectID]’ – get a record for an object, including all open access data and its image (if available).
‘/search’ – get a list of all object ids for objects that contain the search query within the object’s data.
‘/search?q=female’ – get a list of all objects ids which the artists are female
‘/search?q=male’ – get a list of all objects ids which the artists are male
‘/search?isHighlight=true&q=isHighlight’ – get a list of objects that are highlighted

List of features
Feature: Random Display
Description: Randomly display the highlighted artworks to the users.
Model (data class): Gallery
REST API endpoint: ‘/search?isHighlight=true&q=isHighlight’
Pages: ‘Random_Display’

Feature: Data Visualization
Description: A sample will be selected from the dataset and feature will display charts for various topics using this sample, including a pie chart that show the gender ration of the artists and a bar chart that groups artworks by the art period they belonged to. 
Model (data class): Period
REST API endpoint: ‘/objects’ & ‘/objects/[objectID]’ & ‘/search?q=female’ & ‘/search?q=male’
Pages: ‘Data’

Feature: Quiz
Description: This feature will contain a quiz of five questions, the question will be related to art and history. 
Model (data class): None
REST API endpoint: None
Pages: ‘Quiz’
