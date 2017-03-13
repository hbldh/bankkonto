=========
Bankkonto
=========

.. image:: https://travis-ci.org/hbldh/bankkonto.svg?branch=master
    :target: https://travis-ci.org/hbldh/bankkonto
.. image:: https://coveralls.io/repos/github/hbldh/bankkonto/badge.svg?branch=master
    :target: https://coveralls.io/github/hbldh/bankkonto?branch=master

A tool for cleaning, parsing and ultimately validating Swedish bank account
numbers, primarily written to be used for web applications with form data.


Installation
------------

.. code-block:: bash

    $ pip install git+https://github.com/hbldh/bankkonto.git@master

Documentation
-------------

Will be available on ReadTheDocs eventually.

Usage
-----

Direct usage for validating a bank account number:

.. code-block:: python

    >>> import bankkonto
    >>> bankkonto.validate('9029', '5735211')
    True
    >>> bankkonto.validate('9029', '5735214')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/home/hbldh/Repos/bankkonto/account.py", line 117, in validate
        bank_account_number, bank_name, bank_account_number[-1]))
    bankkonto.exceptions.BankkontoValidationError: Bank account number 5735214 for Länsförsäkringar Bank has invalid control digit: 4

Clean a entered string containing both clearing number and bank account number:

 .. code-block:: python

    >>> import bankkonto
    >>> cn, bn = bankkonto.clean_and_split('8156-6 111.222.333-2')
    >>> print(cn)
    '81566'
    >>> print(bn)
    '1112223332'
    >>> bankkonto.validate(cn, bn)
    True

There is also a `WTForms <https://wtforms.readthedocs.io/en/latest/>`_ validator
at ``bankkonto.flask.BankkontoValidator`` that can be used with e.g.
`Flask-WTF <https://flask-wtf.readthedocs.io/en/stable/>`_.

.. note::

    A Django counterpart is under development.

Tests
-----

Run with ``pytest``:

.. code-block:: shell

     $ py.test tests/ --cov bankkonto --cov-report term-missing


