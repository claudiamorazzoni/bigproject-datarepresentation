<h1 align="center"> Final Project - Flask app </h1><br>


<h2 align="center">Data Representation Module</h2></p>

<h3 align="center"><i>Claudia Morazzoni | G00382878<i> </h3><br><br>

***

## Overview

It's a Web application in Flask that has a RESTful API and it's linking to one database table - CRUD operations are available. The project contains the following files:

|    File                       |      Description                                                                                       | 
|:------------------------------|:-------------------------------------------------------------------------------------------------------|
| [crud.sql](https://github.com/claudiamorazzoni/bigproject-datarepresentation/blob/main/crud.sql)                    |   SQL code to create the database, create the tables and populate the tables                             |
| [dbconfig.py](https://github.com/claudiamorazzoni/bigproject-datarepresentation/blob/main/dbconfig.py)                   |   Configuration file for data access object                                                                           |
| [_init_.py](https://github.com/claudiamorazzoni/bigproject-datarepresentation/blob/main/__init__.py)                        |   Flask server that implements a REST API that performs CRUD operations and authorization(logging in)  |
| templates/[index2.html](https://github.com/claudiamorazzoni/bigproject-datarepresentation/blob/main/templates/index2.html)           |   HTML for home page                                                                                   |
| templates/[login.html](https://github.com/claudiamorazzoni/bigproject-datarepresentation/blob/main/templates/login.html)  |   HTML that contains the login form  |
| requirements.txt              |   List of necessary packages                                                                           |


## Login details

| |User1|User2|
|:----:|:----:|:----:|
|username| ClaudiaMorazzoni | 2021  |
|password| GMIT   | DataRepresentation  |


## Quick steps

To run the code check if you have already installed:
- [mysql-connector-python](https://pypi.org/project/mysql-connector-python/)
- [Flask](https://flask.palletsprojects.com/en/master/installation/)
- [Flask-MySQLdb](https://flask-mysqldb.readthedocs.io/en/latest/)
- [Python 3.9.0](https://www.python.org/downloads/release/python-390/)

Also check the [requirements.txt](https://github.com/claudiamorazzoni/bigproject-datarepresentation/blob/main/requirements.txt) to see the libraries used and their version.

*Note*: Most of the languages/packages were included in the Anaconda programme. However, some of them were called through 'pip' on the command line or downloaded from the internet.

*Note 2*: The computer system worked from is windows 10.


## Instructions on how to run the project

**Step 1.** 

Clone the repository to your machine using the following SSH:
:link:git@github.com:claudiamorazzoni/bigproject-datarepresentation.git

**Step 2.**

Open a virtual environment within the project folder of the repository

**Step 3.**

Check the requirements.txt file and install all the packages needed using the command:

    $ pip install -r path/to/requirements.txt

**Step 4.** 

Start mysql server.

**Step 5.** 

To create the database (crud), the tables (students and users) and to insert data into the tables use the command code of the following file:
- crud.sql

**Step 6.** 

Run the Flask server named _init_.py

**Step 7.** 

Type :link: <http://127.0.0.1:5000/> into your browser.

**Step 8.** 

Perform CRUD (Create, Read, Update and Delete) students data into the web application

## License
[![License](https://img.shields.io/badge/license-MIT-orange.svg?style=flat-square)](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt)





