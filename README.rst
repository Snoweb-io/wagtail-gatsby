****************
Wagtail + Gatsby
****************

Development env
###############

::

    git clone git@github.com:Aleksi44/wagtail-gatsby.git
    pip install -r requirements.txt
    npm install


Run Django Server
*****************

::

    python manage.py migrate
    python manage.py init
    python manage.py runserver 0.0.0.0:4243


Run Gatsby Server
******************

::

    npm run build-plugin && gatsby clean && gatsby develop
