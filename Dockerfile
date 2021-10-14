FROM baseImage
RUN python3 -m venv env
RUN source env/bin/activate
RUN python -m pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py runserver