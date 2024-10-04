# assignment
###### Set Up the Project Directory and Virtual Environment ######
Create a folder and open it in Visual Studio Code: 
Create a virtual environment: python -m venv venv
Activate the virtual environment: source venv/bin/activate

###### Install MySQL and Django ######
Install MySQL using Homebrew:   brew install mysql
Install Django: pip install django

##### Create a Django Project and App #####
Start a new Django project: django-admin startproject projectname
Go to project directory:
Create a Django app: python3 manage.py startapp appname
Add the app to your INSTALLED_APPS in settings.py

##### Set Up MySQL Database ####
Create a MySQL database: CREATE DATABASE users;
Configure the database in settings.py:
Migrate the database: python3 manage.py migrate

USE users;

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    email VARCHAR(50),
    role VARCHAR(50)
);


##### Add Templates and Views #####
Create a templates folder in the app directory:
Create a hello.html file in the templates folder:
Create a view function in views.py:
Add a URL to urls.py:

##### Create Models and Migrate ####
Define a model in models.py:
Make migrations for the app: python3 manage.py makemigrations appname
Migrate the changes to the database: python3 manage.py migrate

##### Display Data from MySQL in HTML #####
Create a view to retrieve data from the database:
Create a users.html file in the templates:

##### Create a Form to Add a New User #####
Create a new view for user creation:
Create new_user.html with a form: Add csrf Token To understand this let us take an example. Suppose you are logged into the website. The attacker sends a link with the help of an email, chat, or with the use of sms. The link contains the request which the attacker wants to be performed. As the user is already authenticated on the website the request is completed when he clicks on the link. This type of request is very dangerous as it may take complete access to the data and other harmful actions may be performed such as transfer of funds, change of email and so on.

### user_detail Route ########
This route fetches a user's details by their id. If the user is not found, it returns a "User not found" error page.
URL: /users/<id> (e.g., /users/1)
Success: Displays user details on user_detail.html.
Error: If the user doesn't exist, shows an error message on error.html.

#### Git Workflow ###
Follow these steps to ensure proper version control:
Initialize Git Repository: git init 
Create a Branch: git checkout -b assignment
Make Commits :
git add .
git commit -m "Commit Message"
Push to Remote Repository:
git remote add origin < Remote Url >
git push -u origin assignment

###### Sql Querys To task 2 ########
INSERT INTO users (name, email, role) VALUES ('example', 'email@example.com', 'Admin');
INSERT INTO users (name, email, role) VALUES ('example', 'email@example.com', 'Admin');














