django-timetable
========================

Required packages
------------------
* django-taggit
    https://github.com/alex/django-taggit
* django-colorful
    https://github.com/charettes/django-colorful

Installation
------------

1. Install django-timetable

        $ pip install django-timetable

2. Install Taggit:

        $ pip install django-taggit

3. Install django-colorful:

        $ pip install django-colorful

4. In settings.py file add the following to DJANGO_APPS:

        DJANGO_APPS = (
            ...
            'taggit',
            'timetable',
        )
