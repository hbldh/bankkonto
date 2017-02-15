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

    $ pip install git+https://github.com/hbldh/bankkonto.git@master

Documentation
-------------

Will be available oin ReadTheDocs eventually.

Usage
-----

.. code-block:: python

    >>> import bankkonto
    >>> bankkonto.validate('9029', '5735211')
    True
    >>> bankkonto.validate('9029', '5735214')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/home/hbldh/Repos/swedwise/bankkonto/bankkonto/account.py", line 117, in validate
        bank_account_number, bank_name, bank_account_number[-1]))
    bankkonto.exceptions.BankkontoValidationError: Bank account number 5735214 for Länsförsäkringar Bank has invalid control digit: 4





