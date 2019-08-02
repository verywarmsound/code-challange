code-challange API wrapper for Simulator program
================================================

Wrapper is written with Django for REST API endpoint, only Get endpoint with location parameter is implemented.
Conda interpreter is used.
corsheaders is used for allowing cross-origin because of frontend.

### how to run it?
API wrapper and frontend solution are not in the container, so you need to clone this repository and run on your machine
 - python manage.py runserver on the port 8000.


 ### api
 Accepts request with location parameter, after parsing and converting to float generate response using Simulator program, implemented in api.py file.