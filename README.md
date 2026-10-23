# Flask API Assignment

## Description
This application is a Rest API built by using Python and Flask
It porvides the following:
- GET / -- Displays a message that confirms that the Flask API is running.
- GET /hello-- Returns a greeting. you can optionallu provide a name using the name query parameter.
- POST /sum-- Accepts a JSON list of numbers and returns their sum.
the API validates the inputs and returns them as an HTTP 400 error for any invalid requests.
## Requirements
- Python (up to date)
- Flask
- Pytest
## Setup
1. Create and activate the Conda environment:
    conda create -n flask_assignment python=3.12
    conda activate flask_assignment
2. install the required -m pip install Flask pytest
## Run the Application
From the project folder, run:

    python app.py

Application will run locally at:
http://127.0.0.1:5000
## API Examples
### Hello endpoint
 Request:

GET /hello?name=Nicholas

Example response:
{"message" : "Hello, Nicholas!"}
## Sum endpoint
Request:
POST /sum
JSON body:
{"numbers": [1, 2, 3, 4, 5]}
Example response:
{"sum": 15}
## Run Tests
Run the tests from the project folder by typing in the following with folder showing as running within Anaconda Prompt:
python -m pytest -v