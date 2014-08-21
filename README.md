macbookpro:~ nsatterl$ cat Projects/django-bak/README.md

    install Postgres.app

    $ mkvirtualenv django-tutorial
    $ pip install django
    $ PATH=$PATH:/Applications/Postgres.app/Contents/Versions/9.3/bin pip install psycopg2
    $ django-admin.py startproject djangotutorial
    $ mv djangotutorial django-tutorial
    $ cd django-tutorial
    $ python manage.py runserver 8081

    $ psql
    =# CREATE DATABASE tutorial;
    =# CREATE USER django WITH PASSWORD 'django';
    =# GRANT ALL PRIVILEGES ON DATABASE tutorial to django;

    add dbrouter.py
    update settings.py

    $ python manage.py syncdb --database=dev

    $ psql
    =# \l
    =# \c tutorial
    =# \dt

    $ python manage.py startapp polls

    edit polls/models.py
    add polls to INSTALLED_APPS


    $ python manage.py sql polls

    BEGIN;
    CREATE TABLE "polls_poll" (
        "id" integer NOT NULL PRIMARY KEY,
        "question" varchar(200) NOT NULL,
        "pub_date" datetime NOT NULL
    )
    ;
    CREATE TABLE "polls_choice" (
        "id" integer NOT NULL PRIMARY KEY,
        "poll_id" integer NOT NULL REFERENCES "polls_poll" ("id"),
        "choice_text" varchar(200) NOT NULL,
        "votes" integer NOT NULL
    )
    ;

    COMMIT;

    $ python manage.py syncdb --database=dev