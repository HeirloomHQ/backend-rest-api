# backend-rest-api

Rest API for backend services

## Getting started

### Make sure you have the following installed:

1. [python3.9](https://www.python.org/downloads/release/python-390/) - The installers are at the bottom
2. pipenv - to install, run `pip3 install pipenv`
3. [docker-desktop](https://www.docker.com/products/docker-desktop) - This will be for our development db service

### To run the development server:

First run `pipenv install --dev` to install the dependencies.

#### Loading/Updating the Database from remote

```bash
docker-compose down
rm -rf mongodata
docker-compose up -d
python scripts/load_mongo.py
```

#### Database

To start the database:

- `docker-compose up -d`

To stop the database

- `docker-compose stop`

#### To run the flask app

- Mac:
  - `./run.sh`
- Windows:
  - Run `Set-ExecutionPolicy RemoteSigned` to run scripts
  - `.\run.ps1`

#### Postman

- You can import heirloom.postman_collection.json for the latest api routes

#### Missing Dependcies

If missing any dependencies or getting warnings about `env`, run `pipenv sync`
