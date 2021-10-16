# Quotes-Backend

Django application for the Quotes Frontend


<!-- python3 -m venv env
source env/bin/activate
python -m pip install django
python -m pip freeze > requirements.txt
python -m pip install -r requirements.txt
pip install django-cors-headers
python manage.py makemigrations
python manage.py migrate
python manage.py runserver  -->


# Installation

`python3 -m venv env`

`source env/bin/activate`

`python -m pip install -r requirements.txt`

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py runserver`

# Run Docker

`docker build -t backend .`

`docker run --name backend-container -d -p 8000:8000 backend`

