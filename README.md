# Throttle Project

To serve all user details through one endpoint(API). If you want to populate the database with dummy data then run python populate.py .To check database query and response time use querydebugger,which is available in utils.py file.

* Please follow this below link:
``` https://throttlelab.herokuapp.com/```

## Installation

#### For psycopg2:

* sudo apt install postgresql postgresql-contrib

#### Install requirements

* pip3 install -r requirements.txt

#### To run migrations:

* python3 manage.py makemigrations

* python3 manage.py migrate

* python3 manage.py migrate --run-syncdb


* python3 manage.py runserver
* open localhost:8000 in browser

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [DRF](https://www.django-rest-framework.org/) - The web framework used



## Overview

The project divided into two folders:
```
* throttllab for global label settings

* assignment for core app level configuration
```





