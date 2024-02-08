Data Engineer Assignment
================================

Technologies used and Why ?
---------------------------

To resolve this problem, I have used ``django`` and ``djangorestframework``, ``PostgreSQL`` , and ``pandas``.

* ``django``: among the best python web frameworks.
* ``djangorestframework``: working well for this solution.
* ``PostgreSQL``: Database used to store our data.
* ``pandas``: Used to transform data.


Installation
------------

This application can be accessed through docker. Once you have downloaded the application you can use the following command to build it

.. code:: sh
        docker-compose build
        docker-compose up -d

Download the project from GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To clone the code, run the command below in the CLI

.. code:: sh

    git clone "git@github.com:aguijarro/db_migration.git"


Assumptions & Issues
####################





Analyzing The Solution
----------------------

Build a batch type API that inserts a large number of data without realizing many messages.

Solving the issue
~~~~~~~~~~~
~~~~~~~~~~~

To solve this problem, use Django Rest Framework and apply the strategies.

* Receive a data object (list of data to process) no individual objects.

* Use a hardware function that allows you to process bulk type data.

Tests
~~~~~

* All of the processes are built with a TDD strategy. Reason why all tests are available.

