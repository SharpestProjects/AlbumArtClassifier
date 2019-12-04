# Album Art classifier

## Development

#### Setup up virtual environment (Recommended)  
`$ python -m venv venv`  
`$ source venv/bin/activate`

#### Install dependencies:  
`$ pip install -r requirements.txt`

#### Download dataset  
`$ python scripts/download_dataset.py`  

#### Train model  
`$ python scripts/train.py --data_dir data/train --save_path trained_models/model.h5 --epochs 10 --batch_size 32`


#### Run Flask app locally
To ensure app runs in debug mode set `FLASK_ENV` envioronment variable before running:  
`$ export FLASK_ENV=development`

Start Flask app  
`$ python app.py`


## Deployment

1. Create heroku account and install heroku CLI: https://devcenter.heroku.com/articles/heroku-cli#download-and-install
2. `$ heroku create <app_name>`
3. `$ git push heroku master`
