# EagleMountainCommunityHub
Website for TSA Webmaster. Built using the Django framework.
We chose it for its high preformance and easy full-stack development.

It has resources for the community including city documents.
It has a home page, forum, etc.

FILE STRUCTURE:
mywebsite/                # Project Root Directory
├── manage.py             # Command-line utility
├── mywebsite/            # Project's Python package (configuration files)
│   ├── __init__.py
│   ├── settings.py       # Project settings (database, installed apps, etc.)
│   ├── urls.py           # Project URL dispatcher
│   ├── asgi.py           # ASGI server configuration
│   └── wsgi.py           # WSGI server configuration
├── home/                 # Django App directory (modular application logic)
│   ├── migrations/       # Database migration files
│   ├── __init__.py
│   ├── admin.py          # Admin interface configuration
│   ├── apps.py           # Application configuration
│   ├── models.py         # Database models definition
│   ├── tests.py          # Application tests
│   ├── views.py          # Request handlers (views)
│   └── urls.py           # App URL patterns (you create this)
└── templates/            # Optional: Global templates folder (best practice for shared layouts)
    └── base.html

Follow file strcuture while developing
