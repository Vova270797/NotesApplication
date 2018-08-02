# Test Project
Application for creating notes

## Configurations

Create venv:
```sh
$ python3 -m venv .env
$ source .env/bin/activate
$ pip install -r requirements.txt
$ cp .src/app/local_settings.py.example .src/app/local_settings.py
```

Django:
```sh
$ ./src/manage.py runserver
$ ./src/manage.py migrate