### Setup Project 

1. install python

```

    pip install python

```

2. setup environment

```
    python -m venv VARIABLE_NAME
    VARIABLE_NAME\scripts\activate

```

3. install Django

```

    pip install django

```

4. create django project

```

    django-admin startproject PROJECT_NAME

```

5. create django App

```

    python manage.py startapp APP_NAME

```

6. Add APP_NAME in setttings.py file

```

    INSTALLED_APPS = [
    'APP_NAME',
]

```

7. Run server

```

    python manage.py runserver

```