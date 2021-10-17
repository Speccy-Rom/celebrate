# Celebrate - REST API service

#### A Python/ AioHttp REST API service will analyse the data provided and identify the demand for gifts among residents of different age groups in different cities by month.


#### _In this application I have developed and tested a REST API service in Python, packaged in a lightweight Docker container and deployed using Ansible._

###The following handlers are implemented in the service:
___
* **POST /imports** (Adds a new upload with data);

* **GET /imports/$import_id/citizens**
  (Returns the inhabitants of the specified upload);

* **PATCH /imports/$import_id/citizens/$citizen_id**
  ( Modifies information about the inhabitant (and their relatives) in the specified upload);

* **GET /imports/$import_id/citizens/birthdays**
  (Calculates how many gifts each person in the upload will buy for their relatives (first order), grouped by month);

* **GET /imports/$import_id/towns/stat/percentile/age**
  (Calculates the 50th, 75th and 99th percentiles of age (full years) of residents by town in the specified sample)


The project involves technologies such as:

* Python 3
* AioHttp
* Asyncio
* PostgreSQL
* sqlalchemy core
* Database
* alembic
* ansible
* Docker
* Docker-compose
* flake8
* Pytest
* Swagger


#### the application is under development