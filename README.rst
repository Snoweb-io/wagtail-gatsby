****************
Wagtail + Gatsby
****************

Test project with `Wagtail <https://github.com/wagtail/wagtail>`_ + `Gatsby <https://github.com/gatsbyjs/gatsby>`_ = 🚀

Build with :

- Gatsby plugin for Wagtail : `gatsby-source-wagtail <https://github.com/GrappleGQL/gatsby-source-wagtail>`_
- GraphQL endpoints for Wagtail : `wagtail-grapple <https://github.com/GrappleGQL/wagtail-grapple>`_


Install
#######

::

    git clone git@github.com:Aleksi44/wagtail-gatsby.git
    pip install -r requirements.txt
    npm install


First Run - Django Server
*************************

::

    python manage.py migrate
    python manage.py init
    python manage.py runserver 0.0.0.0:4243
    # Wagtail at : http://localhost:4243/wagtail/
    # Graphiql at : http://localhost:4243/graphiql/


Run Gatsby Server
******************

::

    npm run build-plugin && gatsby clean && gatsby develop
    # Homepage at : http://localhost:8000/
    # Graphiql at : http://localhost:8000/___graphql
