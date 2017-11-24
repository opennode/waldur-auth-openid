Installation
------------

* `Install Waldur <https://github.com/opennode/waldur-core/blob/develop/docs/guide/install-from-src.rst>`_

* Clone Waldur Auth OpenID repository

  .. code-block:: bash

    git clone https://github.com/opennode/waldur-auth-openid.git

* Install Waldur Auth OpenID into Waldur virtual environment

  .. code-block:: bash

    cd /path/to/waldur-auth-openid/
    python setup.py install

* Define configuration settings: LOGIN_URL_TEMPLATE and LOGIN_FAILED_URL_TEMPLATE

The former is used if login has succeeded, the latter is used if login has failed.
