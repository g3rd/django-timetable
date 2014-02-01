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

0.1.7:
- Get update url from the model (get_absolute_update_url)
- Search in admin via the name and now tags
- Default admin sort order via the start_date_time

0.1.6 - Removed the event all day event replaceing start and end time because it didn't handline timezone correctly.

0.1.5 - Fixed syntax error in the model

0.1.4:
- Changed unicode name
- Removed unused code

0.1.3 - Fixed an issue with all day events

0.1.2:
- Made the Event name searchable on the admin page.
- Updated the instructions.

0.1.1 - Fixed packaging issue for PyPi

0.1.0 - Base working version
