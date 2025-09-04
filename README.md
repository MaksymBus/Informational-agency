# Informational Agency Tracking System

## The Digital Horizon

This is a web-based newspaper application built with Django. 
"The Digital Horizon" is a platform for publishing and managing articles focused on the technical world, including news on technology, artificial intelligence, and programming. 
The application allows for a clear separation of content by topics and provides an administration interface for redactors to create and manage articles.

## 🚀 Try it out

https://informational-agency-digital-horizon.onrender.com

Use the following user to log in and check the functionality of the website:

- **Note:** to test site you can take default-user
  - login: `user`
  - password: `70User123`
  
## 🧐 Features

*   Homepage with Live Stats: A dynamic landing page displaying real-time counts of newspapers, redactors, and topics.

*   Article Management: A system for redactors to create, update, and delete articles (Newspapers).

*   User Authentication: Secure login and logout functionality for redactors.

*   Topic-Based Categorization: Organize and filter articles by specific topics.

*   Search Functionality: Users can search for newspapers, redactors, and topics.

*   Responsive Design: A modern, mobile-friendly user interface built on a Bootstrap-based theme.


## Getting started

Python 3 must be already installed

1. Clone repository

```shell

git clone https://github.com/MaksymBus/Informational-agency.git

```

2. Create and activate .venv environment

```shell

python -m venv venv

```
on Windows
```shell

venv\Scripts\activate

```
on macOS
```shell

source venv/bin/activate

```

3. Install requirements.txt 

```shell

pip install -r requirements.txt

```

4. Make migrations

```shell

python manage.py makemigrations

python manage.py migrate

```

5. Load fixtures (Optional, but recommended)

```shell

python manage.py loaddata informational_agency_db_data.json

```

6. Create superuser

```shell

python manage.py createsuperuser

```

7. Run server

```shell

python manage.py runserver # http://127.0.0.1:8000/

```

## Built with

Technologies used in the project:

*   Backend: Django (Python)
*   Database: PostgreSQL (or SQLite for development)
*   Frontend: Django templates
*   Authentication: Django Authentication System
*   Styles: Bootstrap 4

## Demo

![Website Interface](/static/assets/img/demo/LogIn.png)
![Website Interface](/static/assets/img/demo/Home_1.png)
![Website Interface](/static/assets/img/demo/Home_2.png)
![Website Interface](/static/assets/img/demo/RedactorList.png)
![Website Interface](/static/assets/img/demo/RedactorCreate.png)
![Website Interface](/static/assets/img/demo/RedactorDetail.png)
![Website Interface](/static/assets/img/demo/RedactorDelete.png)
![Website Interface](/static/assets/img/demo/NewspaperList.png)
![Website Interface](/static/assets/img/demo/NewspaperCreate.png)
![Website Interface](/static/assets/img/demo/NewspaperDetailAssignMe.png)
![Website Interface](/static/assets/img/demo/NewspaperDetailDelMe.png)
![Website Interface](/static/assets/img/demo/NewspaperDelete.png)
![Website Interface](/static/assets/img/demo/NewspaperUpdate.png)
![Website Interface](/static/assets/img/demo/TopicList.png)
![Website Interface](/static/assets/img/demo/TopicCreate.png)
![Website Interface](/static/assets/img/demo/TopicDelete.png)
![Website Interface](/static/assets/img/demo/TopicUpdate.png)
![Website Interface](/static/assets/img/demo/LoggedOut.png)
