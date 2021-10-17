FROM python:3.8.2-slim-buster
WORKDIR /backend 
COPY requirements.txt requirements.txt 
RUN python -m pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python3","manage.py","runserver","0.0.0.0:8000"]