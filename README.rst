=========
Bankkonto
=========

.. image:: https://travis-ci.org/hbldh/bankkonto.svg?branch=master
    :target: https://travis-ci.org/hbldh/bankkonto
.. image:: https://coveralls.io/repos/github/hbldh/bankkonto/badge.svg?branch=master
    :target: https://coveralls.io/github/hbldh/bankkonto?branch=master


Installation
------------

.. code-block:: bash

    $ pip install bankkonto

Documentation
-------------

Available at the `Github pages <https://hbldh.github.io/pymetawear/>`_
of this repository.

Usage
-----



.. code-block:: python

    >>> import bankkonto
    >>> bankkonto.validate('9029', '5735214')
    True
    >>> bankkonto.validate('9029', '5725645')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValidationError: integer division or modulo by zero



