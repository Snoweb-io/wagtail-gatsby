****************
Wagtail + Gatsby
****************

WIP test project with `Wagtail <https://github.com/wagtail/wagtail>`_ + `Gatsby <https://github.com/gatsbyjs/gatsby>`_ = 🚀

Build with :

- Gatsby plugin for Wagtail : `gatsby-source-wagtail <https://github.com/GrappleGQL/gatsby-source-wagtail>`_
- GraphQL endpoints for Wagtail : `wagtail-grapple <https://github.com/GrappleGQL/wagtail-grapple>`_

Install
#######

::

    git clone git@github.com:Aleksi44/wagtail-gatsby.git
    pip install -r requirements.txt
    npm install


First Run
*************************

::

    python manage.py migrate
    python manage.py init


Develop Run
***********

Django server :
::

    make start
    # OR
    python manage.py runserver 0.0.0.0:4243

    # Wagtail at : http://localhost:4243/wagtail/
    # Graphiql at : http://localhost:4243/graphiql/



Develop worker :
::

    make worker_dev
    # OR
    celery -A cms purge && celery -A cms worker -l info

    # Gatsby Homepage at : http://localhost:8000/
    # Graphiql at : http://localhost:8000/___graphql
