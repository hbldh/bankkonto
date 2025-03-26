# Bankkonto

![Build and Test](https://github.com/hbldh/bankkonto/workflows/Build%20and%20Test/badge.svg)
[![Upload Python Package](https://github.com/hbldh/bankkonto/actions/workflows/python-publish.yml/badge.svg)](https://github.com/hbldh/bankkonto/actions/workflows/python-publish.yml)

A tool for cleaning, parsing and ultimately validating Swedish bank account numbers, primarily written to be used for web applications with form data.

## Installation

```bash
pip install bankkonto
```

## Documentation

Will be available on ReadTheDocs eventually.  

## Usage

Direct usage for validating a bank account number:

```python
>>> import bankkonto

>>> bankkonto.validate('9029', '5735211')
True

>>> bankkonto.validate('9029', '5735214')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/hbldh/Repos/bankkonto/account.py", line 117, in validate
    bank_account_number, bank_name, bank_account_number[-1]))
bankkonto.exceptions.BankkontoValidationError: Bank account number 5735214 for Länsförsäkringar Bank has invalid control digit: 4`
```

Clean an entered string containing both clearing number and bank account number:

```python
>>> import bankkonto
>>> cn, bn = bankkonto.clean_and_split('8156-6 111.222.333-2')
>>> print(cn)
'81566'
>>> print(bn)
'1112223332'
>>> bankkonto.validate(cn, bn)
True
```

There is also a WTForms validator at `bankkonto.flask.BankkontoValidator` that can be used with e.g. Flask-WTF. 

## Tests

Run with pytest:

```bash
pytest tests
```

Install `pytest-cov` first, and get coverage report:

```bash
pytest tests --cov bankkonto --cov-report term-missing
```