# README

## Film library

### Launching an app locally
Clone project from GitHub:\
`git clone https://github.com/frozjeee/MTS.git`

Install virtual environment:\
`python -m venv venv`

Activate virtual environment (Linux/Unix):\
`source venv/bin/activate`

Activate virtual environment (Windows):\
`venv\Scripts\activate`

Install all dependencies:\
`pip install -r requirements.txt`

Apply migrations:\
`python manage.py migrate`

Load test data to your database (Linux/Unix):\
`python manage.py loaddata fixtures/*.json`

Load test data to your database (Windows):\
`python manage.py loaddata fixtures/accounts_dump.json fixtures/films_dump.json`

To run server:\
`python manage.py runserver 0.0.0.0:8000`

### Launching an app in docker container
Clone project from GitHub:\
`git clone https://github.com/frozjeee/MTS.git`

Build docker container:\
`docker build -t film_library .`

To run container:\
`docker run -p 8000:8000 film_library`


API Documentation is available at:\
[Swagger UI](http://localhost:8000/swagger/)
or
[Redoc UI](http://localhost:8000/redoc/)


Test data can be added via Django Admin.

### Test users
Admin user (superuser)\
email: admin@mail.com\
password: admin123

Second user\
email: mail@mail.com
password: poiupoiu