# DJANGO SOCIAL MINIMAL APP

Experimental app to allow to log in to a django app using Google, Faceboot and Instagram using social_django.


## Requirements:

- Django > 4.0
- django-crispy-forms==2.1
- social-auth-app-django==5.4.0

### To have validation from Facebook you need to run:
```bash
    $ python manage.py runserver_plus --cert-file cert.pem --key-file key.pem
```