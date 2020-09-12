# Intro to Django

## Django Permissions & Postgresql

Lab: 32 - Django Permissions & Postgresql

*Author: Natalie Sinner and Harry Potter*

----

## Description
Features - General
You have been supplied with two demos, each presenting a key new feature.
blogapi-permissions demonstrates how to restrict access to portions of your APIs data.
blogapi-postgres demonstrates switching over to using postgres vs sqlite
Your job is to merge the functionality of both demos.
Customize your project to use different application features/models than Blog and Post
Features - Django REST Framework
Make your site a DRF powered API as you did in previous lab.
Adjust project’s permissions so that only authenticated user’s have access to API.
Add a custom permission so that only author of blog post can update or delete it.
Add ability to switch user’s directly from browsable API.
Features - Docker
NOTE Refer to demo for built out Dockerfile and docker-compose.yml examples.
create Dockerfile based off python:3.8-slim
create docker-compose.yml to run Django app as a web service.
enter docker-compose up --build to start your site.
add postgres 11 as a service
Note: It is not required to include a volume so that data can persist when container is shut down.
Go to browsable api and confirm site properly restricts users based on their permissions.

## Reference 
[StackOverFlow](https://stackoverflow.com/questions/40667519/why-is-django-throwing-error-disallowedhost-at)

---

### Getting Started
Clone this repository to your local machine.

```
$ git clone [https://github.com/nsinner1/drf-api-permissions-postgres]
```

### To run the program from VS Code:
Select ```File``` -> ```Open``` -> ```django-api-permissions-postgres```

Next navigate to the location you cloned the Repository.

Double click on the ```django-api-permissions-postgres``` directory.

Then select and open ```django-api-permissions-postgres```

### To run in browser:
Locate directory in terminal

Activate virtual environment:

```
poetry init 
poetry shell
```
Once in virtual environment, run command:

```
python manage.py runserver
```

Once server is running, copy and paste URL: http://127.0.0.1:8000/api/v1/books/ or http://0.0.0.0:8001/api/v1/books/

---

### Change Log
***[The change log will list any changes made to the code base. This includes any changes from TA/Instructor feedback]*** 
1.4: *Set up Permissions & Postgresql* - 12 Sept 2020
1.3: *Set up Docker and new port* - 12 Sept 2020
1.2: *Set up server and verified links are correct between each page* - 12 Sept 2020  
1.1: *Set up scaffolding* - 12 Sept 2020  


------------------------------
For more information on Markdown: https://www.markdownguide.org/cheat-sheet