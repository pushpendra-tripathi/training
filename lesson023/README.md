# Subject: Python
## Topic: Modules: datetime, json, os, random
## Module: 
<https://docs.python.org/3/library/datetime.html>

<https://docs.python.org/3/library/json.html>

<https://docs.python.org/3/library/os.html>

<https://docs.python.org/3/library/random.html>

### Goal
You will learn key modules in Python such as datetime, json, os, and random to manipulate data, manage files, and generate random values effectively. 
### Reading 

### Assignment

[Http & Requests Module](#Http-&-Requests-Module)

[Randomizing Data](#Randomizing-Data)

# Http & Requests Module
## Description 

### Goals Here are the goals of today's lesson:


1. Understanding the Http request response cycle

2. Learn about types of Http Requests

3. Understand Http Status Codes

4. Understand the python requests library

    https://requests.readthedocs.io/en/latest/


## Worksheet

1. Read the python requests library quick start guide:
    >   https://requests.readthedocs.io/en/latest/user/quickstart/

2. Install the requests module using the following command:
    > python -m pip install requests

3. Visit https://httpbin.org/#/
    > Write python code using requests to try out the following modules from https://httpbin.org
    > Submit your code in example_requests.py file

    - Http Methods
        - GET
        - POST
        - PUT
        - PATCH
        - DELETE
    - Auth
        - basic-auth
        - bearer
    - Status Codes (all)
    - Request Inspection
        - headers
    - Response Inspection
        - response-headers
    - Response Formats
        - json
        - gzip
        - html
        - xml
    
## Randomizing Data

## Goal
Gain proficiency in generating randomized data structures in Python to simulate asset and rental records. Develop functions to create assets and rentals with specified constraints, including varying purchase and rental dates, avoidance of overlapping rental periods, and adherence to date limitations. Apply understanding of datetime manipulation and randomization techniques to generate realistic and non-overlapping data sets for asset management system

## Asset

```python
assets = [
    {"id": <int>, "purchase_date": "YYYY-MM-DD"},
    {"id": <int>, "purchase_date": "YYYY-MM-DD"},
    ...
]
```

**Write a function that creates `assets` with p random items of varying purchase dates that are between x days ago and today**

```
def create_assets(p):
    return None
```

## Rental

```
rentals = [
    {"id": 1, "asset_id": 1, "start_date": "YYYY-MM-DD", "end_date": "YYYY-MM-DD"},
    {"id": 2, "asset_id": 2, "start_date": "YYYY-MM-DD", "end_date": "YYYY-MM-DD"},
    {"id": 3, "asset_id": 3, "start_date": "YYYY-MM-DD", "end_date": "YYYY-MM-DD"},
    {"id": 4, "asset_id": 2, "start_date": "YYYY-MM-DD", "end_date": "YYYY-MM-DD"},
    {"id": 5, "asset_id": 3, "start_date": "YYYY-MM-DD", "end_date": "YYYY-MM-DD"},
    ...
]
```

**Write a function that uses `assets` created previously and creates `rentals` with q random items of varying start and end dates**

```
def create_rentals(assets, q):
    return None
```

Constraints:
1. For a given asset, start and end dates may be adjacent but may not overlap at all.
2. Start dates cannot be greater than `datetime.date.today()`

Example:

✅ Items with the same asset_id and a start/end of 2023-12-05/2023-12-09 and 2023-12-10/2023-12-23<br>
❎ Items with the same asset_id and a start/end of 2023-12-05/2023-12-09 and 2023-12-08/2023-12-23


