## Extending Third Party Django App's urlpatterns

This is just meant to be a quick and dirty example app on how one could extend views
of a third party Django app. No magic, bit hacky.

For more information please see the [blog post](https://medium.com/@_RStein_/extending-third-party-django-app-without-touching-its-code-d35fb136c08f).

This is a fork of mdamien's [Django tutorial repo](https://github.com/mdamien/django-tutorial).

**Setup**

1. `git clone https://github.com/SteinRobert/django-third-party-extension-tutorial`
2. `virtualenv django-tutorial-extension`
3. `pip install Django==1.10` 

## Original Readme

## Django 1.10 Tutorial - Poll app

Resulting app from the [Django 1.10 tutorial](https://docs.djangoproject.com/en/1.10/intro/tutorial01/).

Each step is available via the tags:

   - [step 1](https://github.com/mdamien/django-tutorial/tree/tutorial01) ([commit](https://github.com/mdamien/django-tutorial/commit/tutorial01))
   - [step 2](https://github.com/mdamien/django-tutorial/tree/tutorial02) ([commit](https://github.com/mdamien/django-tutorial/commit/tutorial02))
   - [step 3](https://github.com/mdamien/django-tutorial/tree/tutorial03) ([commit](https://github.com/mdamien/django-tutorial/commit/tutorial03))
   - [step 4](https://github.com/mdamien/django-tutorial/tree/tutorial04) ([commit](https://github.com/mdamien/django-tutorial/commit/tutorial04))
   - [step 5](https://github.com/mdamien/django-tutorial/tree/tutorial05) ([commit](https://github.com/mdamien/django-tutorial/commit/tutorial05))
   - [step 6](https://github.com/mdamien/django-tutorial/tree/tutorial06) ([commit](https://github.com/mdamien/django-tutorial/commit/tutorial06))
   - [step 7](https://github.com/mdamien/django-tutorial/tree/tutorial07) ([commit](https://github.com/mdamien/django-tutorial/commit/tutorial07))

#### Notes

- There exist [another repo doing that](https://github.com/Chive/django-poll-app) but it's not up-to-date
- I decided not to add python 2 support in step 2
- I added the `Choice` model to the admin directly in step 2
- I used `repeat` instead of `no-repeat` for the background in step 6, looks better
