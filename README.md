<p align="center">
    <img src="https://miro.medium.com/max/1142/0*hviGPCXKKQa0T8OQ.png"/>
</p>

<h1 align="center">
  🎯 DDD & REST-API & DOCKER in Python Django
</h1>

<p align="center">
   <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black"/></a>
    <a href="https://www.python.org/downloads/release/python-370/"><img src="https://img.shields.io/badge/python-v3.7-blue" alt="Python v3.7"/></a>
<a href="http://www.djangoproject.com/"><img src="https://img.shields.io/badge/django%20version-2.2-purple" border="0" alt="A Django site." title="A Django site." /></a>

</p>

<p align="center">
  Boilerplate API project for Django following Domain-Driven Design (DDD) principles keeping the code as simple as possible.
  <br />
  <br />
  Take a look, develop and have fun with this.
  <br />
  <br />
  <a href="#table-of-contents"><strong>Explore the docs »</strong></a>
  <br />
  <br />
  <a href="https://github.com/davidcerezal/docker-django-ddd/issues">Report Bug</a>
  ·
  <a href="https://github.com/davidcerezal/docker-django-ddd/issues">Request Feature</a>
</p>


<!-- TABLE OF CONTENTS -->
## Table of Contents

* [🚀 Environment setup](#-environment-setup)
  * [🐳 Needed tools](#-needed-tools)
  * [🌍 Application execution](#-application-execution)
* [🤔 Project explanation](#-project-explanation)
  * [DDD skeleton](#-ddd-skeleton)
  * [Django Rest Framework](#-django-rest-framework)
  * [Django Rest Registration](#-django-rest-registration)
  * [Celery](#-celery)
  * [Docker](#-docker)
* [👷‍ Console commands](#-console-commands)
* [🤝 Contributing](#-contributing)

## 🚀 Environment setup

### 🐳 Needed tools

1. [Install Docker](https://www.docker.com/get-started)

### 🌍 Application execution

1. First run **`make build`** inside root directory.
2. Then run **`make up`** to start up the project for first time.
3. Use/update environment variables from [**`.envs`**](https://github.com/davidcerezal/docker-django-ddd/blob/master/.envs) folder.

Checkout the [commands](#commands) section for more usage.

## Preview
A default Django project resides in `src` directory. So, when you start the project, you will see the following screen in `8000` port:

![Demo One](https://github.com/ruddra/blog-images/raw/master/Demo%201.png)

Also when you access the django container log via `make log-web`, you will see the following:

![Demo Two](https://github.com/ruddra/blog-images/raw/master/Demo%202.png)

## 🤔 Project explanation

This project tries to be a full rest API platform for Indexacapital.

### 🤔 DDD skeleton
Bootstrap your new projects or be inspired by DDD and hexagonal architecture. 

### 🤔 Django Rest Framework
Django REST framework is a powerful and flexible toolkit for building Web APIs.

Some reasons you might want to use REST framework:
- The Web browsable API is a huge usability win for your developers.
- Authentication policies including packages for OAuth1a and OAuth2.
- Serialization that supports both ORM and non-ORM data sources.
- Customizable all the way down - just use regular function-based views if you don't need the more powerful features.
- Extensive documentation, and great community support.
- Used and trusted by internationally recognised companies including Mozilla, Red Hat, Heroku, and Eventbrite.

Full documentation for the project is available at https://www.django-rest-framework.org/.


### 🤔 Django Rest Registration
User registration REST API, based on Django REST Framework.

Full documentation for the project is available at https://django-rest-registration.readthedocs.io/.

### 🤔 Celery
Celery is an asynchronous task queue/job queue based on distributed message passing. It is focused on real-time operation, but supports scheduling as well.

Full documentation for the project is available at http://www.celeryproject.org/.

### 🤔 Docker
If you already doesn't know what it's docker, that place it's not for you.
Try with that: https://docs.docker.com/get-started/overview/

### Advantages
1. Ready to use with your django project.
2. Combined with NGINX, Redis, Celery to handle relevent things.
3. Alpine based images are used, so that sizes of the images are compartively low.
4. Now comes built it with Numpy, Scipy and Pandas support. So you can integrate your datascience projects with this. [Instructions](#now-featuring-numpy-scipy-and-pandas) for integrating these libraries are also shared in the `Dockerfile`.
5. With Numpy, Pandas and Scipy dependecies installed, the total size is 657MB(may differ if you have more packages). Without these, size reduces to 390MB.
6. Now comes with support to install [Pillow](https://pypi.org/project/Pillow/) using django.

## 👷‍ Console commands
To use this project, run this commands:

1. `make up` to build the project and starting containers.
2. `make build` to build the project.
3. `make start` to start containers if project has been up already.
4. `make stop` to stop containers.
5. `make shell-web` to shell access web container.
6. `make shell-db` to shell access db container.
7. `make shell-nginx` to shell access nginx container.
8. `make logs-web` to log access web container.
9. `make logs-db` to log access db container.
10. `make logs-nginx` to log access nginx container.
11. `make collectstatic` to put static files in static directory.
12. `make log-web` to log access web container.
13. `make log-db` to log access db container.
14. `make log-nginx` to log access nginx container.
15. `make restart` to restart containers.


## 🤔 Contributing
There are some things missing (improve documentation...), feel free to add this if you want! If you want
some guidelines feel free to contact us :)

<a name="notRecommended">1</a>: This method is the slower and only must be used if you don't have connectivity with GitHub






