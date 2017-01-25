Installation
------------

* `Install NodeConductor <http://nodeconductor.readthedocs.org/en/latest/guide/intro.html#installation-from-source>`_

* Clone NodeConductor OpenID repository

  .. code-block:: bash

    git clone https://github.com/opennode/nodeconductor-auth-openid.git

* Install NodeConductor OpenID into NodeConductor virtual environment

  .. code-block:: bash

    cd /path/to/nodeconductor-auth-openid/
    python setup.py install

* Define configuration settings: LOGIN_URL_TEMPLATE and LOGIN_FAILED_URL_TEMPLATE

The former is used if login has succeeded, the latter is used if login has failed.
