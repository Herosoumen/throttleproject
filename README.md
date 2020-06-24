# Throttle Project

To serve all user details through one endpoint(API)

## Installation

No need to install any db or thirtd party apps,here I'm using inbuilt dbsqlite3 database

* Install requirements

pip3 install -r requirements.txt

* To run migrations:

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py migrate --run-syncdb


python3 manage.py runserver
open localhost:8000 in browser

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [DRF](https://www.django-rest-framework.org/) - The web framework used



## Overview

The project divided into two folders:
```
* throttllab for global label settings

* assignment for core app level configuration
```





