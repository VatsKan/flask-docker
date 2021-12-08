# Python flask tech test 

## Task

Display on '/hello' page the total sales of items for the times between
11:10 - 11:15
11:15 - 11:20
11:20 - 11:25
11:25 - 11:30
11:30 - 11:35

## Changes I would make with more time
- looping through all data for each time range. Not ideal. Should only need to do loop once.
- perhaps not hard code time stamps or at least generate it in some way
- see if better way of reading and filtering timestamp data directly with pandas instead of looping through data in python
- not use moment and datetime libraries in python. just use one of the libraries. 
- refactor and wrap around with python class
- display data in a nicer format on the page rather than as json

## Run locally

To run, create a virtual env (e.g. using conda) then
```
pip install -r requirements.txt
export FLASK_APP=app.py
flask run
```