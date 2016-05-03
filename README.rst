NodeConductor OpenID
====================

NodeConductor plugin bringing OpenID-based authentication support.

Usage
-----

1. Install the plugin
2. Enable the plugin -- add these to NodeCOnductor `settings.py`:

.. code-block:: python

    INSTALLED_APPS += ('django_openid_auth',)
    AUTHENTICATION_BACKENDS += ('django_openid_auth.auth.OpenIDBackend',)

3. Add your OpenID to your user account:

.. code-block::

    NodeConductor admin > Core > Django_Openid_Auth > User open ids > Add user open id
    User: <your-django-user-id>
    Claimed id: <openid.claimed_id> (example: https://launchpad.net/~johndoe)
    Display name: <your-display-name>

4. Navigate to `<nodeconductor-url>/api-auth/openid/login` and try to log in using your OpenID provider URL
