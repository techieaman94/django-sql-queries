# Django SQL Queries

This project provides a middleware which can be used in django projects to print all SQL queries, their count and execution time
for processed view before returning response for a request.

## How to use:

1. Install python 3.7 or greater on your system using [pyenv](https://github.com/pyenv/pyenv)
2. Activate your project's virtual environment for installing this library
```shell
$ source <virtualenv-path>/bin/activate
```
3. Install the package by running following command
```shell
$ pip install django-sql-queries
```
4. Add in the list of middlewares of django project
```shell
MIDDLEWARE.append("django_sql_queries.middleware.SQLPrinterMiddleware")
```