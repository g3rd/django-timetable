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

2. In settings.py file add the following to DJANGO_APPS:

        DJANGO_APPS = (
            ...
            'taggit',
            'timetable',
        )


Change Log
----------

0.1.2:
- Made the Event name searchable on the admin page.
- Updated the instructions.

0.1.1 - Fixed packaging issue for PyPi

0.1.0 - Base working version
