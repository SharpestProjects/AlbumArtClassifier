# Basic Flask app for Heroku


## Deploying:
1. Create heroku account and install heroku CLI: https://devcenter.heroku.com/articles/heroku-cli#download-and-install
2. `$ heroku create <app_name>`
3. `$ git push heroku master`


## Development

(Recommended) Setup up virtual environment https://virtualenv.pypa.io/en/latest/  
`$ virtualenv venv`  
`$ source venv/bin/activate`

Install dependencies:  
`$ pip install -r requirements.txt`

To ensure app runs in debug mode set `FLASK_ENV` envioronment variable before running:  
`$ export FLASK_ENV=development`


To run app locally (starts server on localhost:5000)
`$ flask run`
