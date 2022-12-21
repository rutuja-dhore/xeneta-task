
# Flask + Postgres + Docker Application
# Assignment: HTTP-based API

Develop an [HTTP-based API](#task-1-http-based-api) capable of handling the GET request described below. Our stack is based on Flask, but you are free to choose any Python framework you like. All data returned is expected to be in JSON format. Please demonstrate your knowledge of SQL (as opposed to using ORM querying tools).


Implement an API endpoint that takes the following parameters:

* date_from
* date_to
* origin
* destination

and returns a list with the average prices for each day on a route between port codes *origin* and *destination*. Return an empty value (JSON null) for days on which there are less than 3 prices in total.

Both the *origin, destination* params accept either port codes or region slugs, making it possible to query for average prices per day between geographic groups of ports.

    curl "http://127.0.0.1/rates?date_from=2016-01-01&date_to=2016-01-10&origin=CNSGH&destination=north_europe_main"

    [
        {
            "day": "2016-01-01",
            "average_price": 1112
        },
        {
            "day": "2016-01-02",
            "average_price": 1112
        },
        {
            "day": "2016-01-03",
            "average_price": null
        },
        ...
    ]

# How to run application

To run the application and database together
```bash
docker compose up --build pythonapp
```

If you To run the database only
```bash
docker compose up -d db
```

To connect to the database 
```bash
docker exec -it db psql -U postgres
```

To see if tables are uploaded
```bash
\dt
```

To see the API
```bash
curl "http://127.0.0.1/rates?date_from=2016-01-01&date_to=2016-01-07&origin=CNSGH&destination=EETLL"
[{"average_price":"1462.6830332787779596","day":"2016-01-01"},{"average_price":"1462.5979268957992362","day":"2016-01-02"},{"average_price":"Null","day":"2016-01-03"},{"average_price":"Null","day":"2016-01-04"},{"average_price":"1455.2343142698500833","day":"2016-01-05"},{"average_price":"1441.8256524153248195","day":"2016-01-06"},{"average_price":"1432.4662983425414365","day":"2016-01-07"}]

```

To execute tests 
```bash 
============================================================================================ test session starts =============================================================================================
platform darwin -- Python 3.10.8, pytest-7.2.0, pluggy-1.0.0
rootdir: /Users/rutuja.dhore/Desktop/demo-projects/xeneta-task
plugins: mock-3.10.0
collected 2 items                                                                                                                                                                                            

test.py ..                                                                                                                                                                                             [100%]

============================================================================================= 2 passed in 0.22s ==============================================================================================
(.venv) NOMI000336:xeneta-task rutuja.dhore$ 
``` 