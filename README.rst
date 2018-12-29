=====================
pyArchOps/dnsmasq
=====================

.. image:: https://badge.fury.io/py/pyarchops-dnsmasq.svg
        :target: https://pypi.python.org/pypi/pyarchops-dnsmasq

.. image:: https://img.shields.io/gitlab/pipeline/pyarchops/dnsmasq/next-release.svg
        :target: https://gitlab.com/pyarchops/dnsmasq/pipelines

.. image:: https://readthedocs.org/projects/dnsmasq/badge/?version=latest
        :target: https://dnsmasq.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/pyarchops/dnsmasq/shield.svg
     :target: https://pyup.io/repos/github/pyarchops/dnsmasq/
          :alt: Updates


dnsmasq


* Free software: MIT license
* Documentation: https://pyarchops-dnsmasq.readthedocs.io.


Features
--------

* dnsmasq

Instalation
--------------

.. code-block:: console

    $ pip install pyarchops-dnsmasq


Usage
--------

.. code-block:: python

    impor os
    import textwrap
    from suitable import Api
    from pyarchops import helpers
    from pyarchops_dnsmasq import dnsmasq

    api = Api(
        '127.0.0.1:22',
        connection='smart',
        remote_user='root',
        private_key_file=os.getenv('HOME') + '/.ssh/id_rsa',
        become=True,
        become_user='root',
        sudo=True,
        ssh_extra_args='-o StrictHostKeyChecking=no'
    )

    dnsmasq_conf = textwrap.dedent('''
        no-poll
        no-resolv
        cache-size=1500
        no-negcache
        server=/core-vpn/10.16.254.1
        server=/core-vpn/10.16.254.2
        server=/core-vpn/10.16.254.3
        server=8.8.4.4
        server=8.8.8.8
    ''')

    resolve_conf = 'nameserver 127.0.0.1'

    config = {
        'dnmasq_conf': dnsmasq_conf,
        'resolv_conf': resolve_conf
    }

    result = dnsmasq.apply(api, config=config)
    print(result)

Development
-----------

Install requirements:

.. code-block:: console

    $ sudo pacman -S tmux python-virtualenv python-pip libjpeg-turbo gcc make vim git tk tcl

Git clone this repository

.. code-block:: console

    $ git clone https://github.com/pyarchops/dnsmasq.git pyarchops.dnsmasq
    $ cd pyarchops.dnsmasq


2. See the `Makefile`, to get started simply execute:

.. code-block:: console

    $ make up


Credits
-------

* TODO

