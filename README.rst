****************
Wagtail + Gatsby
****************

Web app build with `Wagtail <https://github.com/wagtail/wagtail>`_ + `Gatsby <https://github.com/gatsbyjs/gatsby>`_ = 🚀

.. image:: https://d271q0ph7te9f8.cloudfront.net/www/images/wagtail-gatsby.original.png


**List of commands available :**

- ``python manage.py build <site_id>`` : Deploy wagtail site with gatsby on S3/Cloudfront AWS
- ``python manage.py develop`` : Run tasks to keep up to date gatsby in development mode


Development environment
***********************

First steps
-----------

**Install dependencies**

::

    git clone git@github.com:Aleksi44/wagtail-gatsby.git
    pip install -r requirements.txt
    npm install


**If first run**

::

    # Django migrations
    python manage.py migrate

    # Initialize default database
    python manage.py init


**Add your preferences in .env file**

::

    AWS_ACCESS_KEY_ID=*****************
    AWS_SECRET_ACCESS_KEY=***************************
    AWS_S3_REGION_NAME='eu-west-3' # Paris

    # This bucket is used for Wagtail medias
    AWS_STORAGE_BUCKET_NAME='my-media-bucket'

    # This custom domain is used for Wagtail medias
    AWS_S3_CUSTOM_DOMAIN='my-custom-cloud-front-domain.com'

    # If you use AWS CloudFront
    AWS_DISTRIBUTION_ID=*********

    # Configure and add your Broker URL used by Celery
    # https://docs.celeryproject.org/en/stable/getting-started/brokers/
    # Example with redis
    CMS_BROKER_URL='redis://localhost:6379/0'

Play
----

**1 - Run Django server with Makefile or manually**
::

    # With Makefile
    make start

    # Manually
    python manage.py runserver 0.0.0.0:4243


With this command, you have these services available :

- **Wagtail** = manage your content : ``http://localhost:4243/wagtail/``
- **Graphql** = graphql endpoint : ``http://localhost:4243/graphql/``
- **Graphiql** = test your graphql request : ``http://localhost:4243/graphiql/``
- **Django Admin** = manage task results : ``http://localhost:4243/admin/``


**2 - Run develop worker with Makefile or manually**
::

    # With Makefile
    make worker_dev

    # Manually
    yes | celery -A cms purge && celery -A cms worker -l info


With this command, you have these services available :

- **Gatsby develop** = develop mode with Gatsby : ``http://localhost:8000/``
- **Graphiql** = test your graphql request : ``http://localhost:8000/___graphql``


Related link
************

- Gatsby plugin for Wagtail : `gatsby-source-wagtail <https://github.com/GrappleGQL/gatsby-source-wagtail>`_
- GraphQL endpoints for Wagtail : `wagtail-grapple <https://github.com/GrappleGQL/wagtail-grapple>`_
- Amazon Web Service for static website hosting : boto3 with `S3 <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html>`_ and `CloudFront <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html>`_
- Celery for task queues : `celery <https://docs.celeryproject.org/en/stable/getting-started/introduction.html>`_
