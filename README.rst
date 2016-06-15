NodeConductor OpenID
====================

NodeConductor plugin bringing OpenID-based authentication support.

Usage
-----

1. Install the plugin

2. Run migrations to create new tables.

.. code-block::

    nodeconductor migrate --noinput

3. Add your OpenID to your user account:

.. code-block::

    NodeConductor admin > Core > Django_Openid_Auth > User open ids > Add user open id
    User: <your-django-user-id>
    Claimed id: <openid.claimed_id> (example: https://launchpad.net/~johndoe)
    Display name: <your-display-name>

4. Navigate to `<nodeconductor-url>/api-auth/openid/login` and try to log in using your OpenID provider URL

Known issues
------------

**Database migrations do not work correctly with MySQL**

Running migrations (step 3 of 'Usage' section) may fail with following error:

.. code-block::

    django.db.utils.OperationalError: (1170, "BLOB/TEXT column 'claimed_id' used in key specification without a key length")

This is a `known issue<https://bugs.launchpad.net/django-openid-auth/+bug/524796>`_ of `django-openid-auth<https://pypi.python.org/pypi/django-openid-auth/>`_ :
Django `does not allow<https://code.djangoproject.com/ticket/2495>`_ `TextField` to be unique.

Fix exists but it is not yet merged as of 2016-05-03.

To work around the problem you will have to manually patch the `django-openid-auth` code as follows:

.. code-block:: python

    # File: django_openid_auth/migrations/0001_initial.py
    -    claimed_id = models.TextField(max_length=2047, unique=True)
    +    claimed_id = models.CharField(max_length=255, unique=True)

    # File: django_openid_auth/migrations/0001_initial.py
    -                ('claimed_id', models.TextField(unique=True, max_length=2047)),
    +                ('claimed_id', models.CharField(unique=True, max_length=255)),

-- and launch the migrations again.
