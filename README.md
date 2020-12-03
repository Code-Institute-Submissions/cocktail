# Cocktail Book
 Cocktail book was created for educational purposes, it's my 3rd **Milestone** **Project** 
 which complete my Data Centric Development module.
 
 A live **desktop demo** you can find [here](https://cocktail-book-project.herokuapp.com/).
 
 The **source code** you can find [here](https://github.com/ka-pa-ra/cocktail).

 # Table of Contents
* UX
* User Stories
* Features
* Technologies Used
* Testing
* Deployment
* Deployment to Heroku
* Credits

# UX
The idea of Cocktail Book is to create a community member for bartenders and not only. 

The website offers to users to find or sharing new recipes by searching for them in _Cocktails page_ ,
where users can find the ingredients , method and etc. . 

# User Stories

## User Story One:
As a user, I want to create a Profile account.

## User Story Two:
As a user I want to be able search and share Cocktails.

## User Story Three:
As user it's important that I can add, edit or delete  my own recipes.

## User Story Four:
As user it's important that I can see image of the cocktail.

## User Story Five:
As a user I want to be with information  about the cocktail, such as what ingredients I might need, method, glass or which ice I need to pour in the glass.

# Features

* When the user is on the homepage can see a navigation bar with name of the website on the left corner and on the right corner can see 
  Log in, Profile , Cocktails and Register.

* The Homepage contains a card panel with a little description of the website and button _Get Started_ which if the user will click and be redirect to Log In page.

* At the time the user is logged in , the user will find another page to the Navigation bar which is My Cocktails and also New Cocktail.

* In My Cocktails page the user will be able to see, edit and delete is own cocktails.

* The Profile page provides a welcoming message with the user's name and a button "My Cocktails".

* The Cocktails page has a search bar where the user can use to find cocktails.

* The My Cocktails page has also a search bar.

# Features Left to Implement

* In future versions I would love to give to users a better Profile page with more details and also their own picture.

* A chat page where users will be able to message each other and exchange ideas.

* A opportunity for users to upload images from their phone or computer instead of inserting a URL.

* A opportunity for the user to share it on social media or with contacts.

* It would be a positive experience for the user if each recipe had a comment section so other users could comment about the recipe.

# Technologies Used

## HTML5
The project uses HTML5 to construct the pages within the application.
## CSS3
The project uses CSS3 in order to style the HTML5 and Bootstrap elements and components.
## Materialize (ver 1.0.0)
The project uses the Materialize components for the design framework.
## Jquery (ver 3.4.1)
The project uses the Jquery in order to make it much easier to use JavaScript.
## Gitpod
The project uses Gitpod as the primary IDE for coding.
## Github
The project uses Github for remote storing of code online.
## Flask (ver 1.1.2)
The project uses Flask as a microframework.
## Jinja
The project uses Jinja for templating with Flask.
## Werkzeug (ver 1.0.1)
The project uses Werkzeug for password hashing, authentication and authorisation.
## Heroku
The project uses Heroku for app hosting.
## Python
The project uses Python as a programming language.
## MongoDB Atlas
The project uses MongoDB Atlas as a cloud database service.

# Testing 

The codes used for this website are been tested on :

* [HTML Validator](https://validator.w3.org/)
* [CSS Validator](https://jigsaw.w3.org/css-validator/)
* [JAVASCRIPT Validator](https://jshint.com/)
* [PYTHON Validator](http://pep8online.com/)

The website has been checked for responsiveness on a multitude of screen sizes from PC to portable devices, such as tablets and mobile phones.

All HTML code was run through the W3C HTML Validator and returned some errors about the pages not starting with a document type declaration.

# Deployment in GitHub

1. On GitHub, navigate to your site's repository.
2. Under your repository name, click Settings.
3. Under "GitHub Pages", use the None or Branch drop-down menu and select a publishing source.
4. Optionally, use the drop-down menu to select a folder for your publishing source.
5. Click Save.

[A live project page.](https://ka-pa-ra.github.io/cocktail/)

# Deployment to Heroku

1. Create a requirements.txt file by typing pip3 freeze --local > requirements.txt into the terminal line.

2. Create a Procfile by typing echo web: python app.py > Procfile.

3. Add, commit and push these changes to Github.

4. Navigate to the Heroku.

5. Create new app and give it a unique name.

6. Choose the region that is closest to you.

7. Go to the Deploy tab and choose Github.

8. Search for the correct repository and connect.

9. Go to Heroku Settings and navigate to Config Vars.

### Set the following:

* IP = 0.0.0.0
* MONGO_DBNAME = [Name of MongoDB]
* MONGO_URI = mongodb+srv://:@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority
* PORT = 5000
* SECRET_KEY = [Secret key]

### Go to the Deploy tab and Deploy Branch, ensuring that the master branch is selected.

# Credits

* The code for the navigation bar, forms and views was duplicated from Code Institute's Task Manager Project.

* Bootstrap - for providing documentation on the framework.

* W3schools - for various code segments, examples and explanations used throughout the project.

* Font Awesome - CDN for icons used in the project.

* Google Fonts - CDN for fonts used in the project.

* Images take using Google.





