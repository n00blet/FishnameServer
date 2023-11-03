
# The Tech-Stack

The repository presented to you is set up with

**Backend**
- [**Docker**](https://www.docker.com) as the build tool
- [**Python3**](https://www.python.org) as the backend programming language
- [**PostgreSQL**](https://www.postgresql.org) as the relational database.
- [**SQLAlchemy**](https://www.sqlalchemy.org) and the Python SQL toolkit and ORM
- [**fastAPI**](https://fastapi.tiangolo.com) as the web framework for building APIs
- [**pytest**](https://docs.pytest.org/en/6.2.x/) for unit testing

<br/><br/>


# Setup Project

Assuming that you have docker installed and running in your system, this is how you can run the application from the 
project root folder.

```
make all
```

This will install requirements for the project and runs pytests <br>
After the above two steps are done, it will create a docker instance of the application running at ```0.0.0.0:8000```


# Run locally
- To run the code locally, you need to have a postgres instance running in the background with db fishnames.
- You also need to update DB configs in either ```.env``` or edit ```session.py``` pointing to your DB instance.
- To install python requirements: ```pip install -r requirements.txt```
- To run the project from base dir: ```uvicorn "src.api.main:app" --host 0.0.0.0 --port 8000 --log-level "debug"```



## Curl Requests example and sample output

#### Get a random fish name. 

```
curl --location 'http://0.0.0.0:8000/random_fish_name' \
--header 'accept: application/json'
```


**Response**
```
{
    "name": "Dartfish"
}
```