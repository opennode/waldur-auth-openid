NodeConductor OpenID
====================

NodeConductor plugin bringing OpenID-based authentication support.

Usage
-----

1. Install the plugin
2. Enable the plugin -- add these to NodeConductor `settings.py`:

.. code-block:: python

    INSTALLED_APPS += ('django_openid_auth',)
    AUTHENTICATION_BACKENDS += ('django_openid_auth.auth.OpenIDBackend',)

3. Run migrations to create new tables.

.. code-block::

    nodeconductor migrate --noinput

4. Add your OpenID to your user account:

.. code-block::

    NodeConductor admin > Core > Django_Openid_Auth > User open ids > Add user open id
    User: <your-django-user-id>
    Claimed id: <openid.claimed_id> (example: https://launchpad.net/~johndoe)
    Display name: <your-display-name>

5. Navigate to `<nodeconductor-url>/api-auth/openid/login` and try to log in using your OpenID provider URL
