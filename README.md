# Album Art classifier

## Development

#### Setup up virtual environment (recommended)  
`$ python -m venv venv`  
`$ source venv/bin/activate`

#### Install dependencies:  
`$ pip install -r requirements.txt`

#### Download dataset  
`$ python scripts/download_dataset.py`  
Downloads and extracts into root direcory with following structure:
```
 data
  ├── sample
  |   ├── metal/
  |   └── not-metal/
  ├── test
  |   ├── metal/
  |   └── not-metal/
  ├── train
  |   ├── metal/
  |   └── not-metal/
  └── validate
      ├── metal/
      └── not-metal/
```

#### Train model
Set `MLFLOW_TRACKING_URI` env variable  
- If not set, will log experiments to `mlflow` folder in root directory

`$ export MLFLOW_TRACKING_URI=http://localhost:3000`

Run training script:
```
$ python scripts/train.py  \
  --data_dir data/train
  --val_dir data/validate
  --epochs 10
  --batch_size 32
  --exp_name test
```

#### Running MLflow server
`$ mlflow server --default-artifact-root s3://my_bucket/path/to/model`

#### Run Flask app locally
To ensure app runs in debug mode set `FLASK_ENV` environment variable before running:  
`$ export FLASK_ENV=development`

Set `MODEL_URI` env variable, e.g.  
**Note:** should be path to MLFlow model https://mlflow.org/docs/latest/models.html  
`$ export MODEL_URI=s3://my_bucket/path/to/model`  
(if using S3 will also need to set `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` )

Start Flask app  
`$ flask run`


## Deploying Flask app

1. Create heroku account and install heroku CLI: https://devcenter.heroku.com/articles/heroku-cli#download-and-install
2. `$ heroku create <app_name>`
3. Set env variables:  
`$ heroku config:set MODEL_URI=s3://my_bucket/path/to/model`  
(if using S3 will also need to set `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` )
4. `$ git push heroku master`
