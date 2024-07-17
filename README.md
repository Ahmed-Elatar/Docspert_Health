# Docspert-Health Assessment  
 

It's a small web app using Django that handles fund transfers between two accounts 
And Retrieve the recent Transfers, and List all accounts with their funds  
also you can search for a certain account from search bar at home page


<br><br>

Docspert-Health - Project Setup Guide <br/>
Pre-requisites<br/>

Before you begin, ensure you have met the following requirements:
- python_version = "3.10" or latest
- virtualenv =  20.26.3
  
1-Install Dependencies :<br/>
- $ pip install virtualenv
- $ pip install -r requirements.txt 



2-Configure Database Settings <br/>
Open settings.py in your Django project directory and update the DATABASES setting to configure your PostgreSQL database. <br/>
Here’s an example configuration:
<br/><br/>
DATABASES = {<br/>
    'default': {<br/>
        'ENGINE': 'django.db.backends.postgresql_psycopg2',<br/>
        'NAME': 'your_database_name',<br/>
        'USER': 'your_database_user',<br/>
        'PASSWORD': 'your_database_password',<br/>
        'HOST': 'your_database_host',<br/>
        'PORT': 'your_database_port',<br/>
    }<br/>
}<br/>

<br/>

3-Run commands:<br/>
- $ python3 manage.py makemigrations
- $ python3 manage.py migrate
- $ pytohn3 manage.py runserver
- Your project should now be running at http://127.0.0.1:8000/

4-Also you can run this command for testing:<br/>
- $ python3 manage.py test

- now the project ready ..


URL Map:
 - path('', index ,For Home Page),
 - path('login/',For Login),
 - path('logout/',For Logout),
 - path('signup/',For signup),
 - path('add-file/', To upload Csv files), # you should to login first
 - path('make-transfer/', To make transfers between accounts), # you should to login first
 - path('list-accounts/',To get all accounts with their funds),
 - path('list-transfers/',To get all recent Transfers),
 

![alt text](https://github.com/Ahmed-Elatar/Docspert_Health/blob/main/Docspert_Health/sceen_shots/Screenshot%20from%202024-07-17%2020-18-49.png)
![alt text](https://github.com/Ahmed-Elatar/Docspert_Health/blob/main/Docspert_Health/sceen_shots/Screenshot%20from%202024-07-17%2020-16-02.png)
![alt text](https://github.com/Ahmed-Elatar/Docspert_Health/blob/main/Docspert_Health/sceen_shots/Screenshot%20from%202024-07-17%2020-16-58.png)
![alt text](https://github.com/Ahmed-Elatar/Docspert_Health/blob/main/Docspert_Health/sceen_shots/Screenshot%20from%202024-07-17%2020-17-09.png)
![alt text](https://github.com/Ahmed-Elatar/Docspert_Health/blob/main/Docspert_Health/sceen_shots/Screenshot%20from%202024-07-17%2020-17-22.png)
![alt text](https://github.com/Ahmed-Elatar/Docspert_Health/blob/main/Docspert_Health/sceen_shots/Screenshot%20from%202024-07-17%2020-17-35.png)
![alt text](https://github.com/Ahmed-Elatar/Docspert_Health/blob/main/Docspert_Health/sceen_shots/Screenshot%20from%202024-07-17%2020-18-24.png)
![alt text](https://github.com/Ahmed-Elatar/Docspert_Health/blob/main/Docspert_Health/sceen_shots/Screenshot%20from%202024-07-17%2020-18-31.png)




