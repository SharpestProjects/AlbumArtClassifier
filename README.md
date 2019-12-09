# Album Art classifier

## Development

### Install dependencies:  
`$ python -m venv venv`  
`$ source venv/bin/activate`  
`$ pip install -r requirements.txt`

### Download dataset  
`$ python scripts/download_data.py`

Downloads and unzips into root direcory with following structure:
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

### Running MLflow server

`$ mlflow server`  

With no arguments, will store data and artifacts (e.g. saved weights) on file system

[MlFlow tracking servers](https://www.mlflow.org/docs/latest/tracking.html#mlflow-tracking-servers)

##### Storage
Can set remote locations for storage `backend` for experiment data (e.g. metrics, training parameters), and `artifacts` for large files (saved weights, notebooks)  

```
$ mlflow server \  
--default-artifact-root s3://my_bucket/path/to/model \  
--backend-store-uri /postgresql://<db_uri>
```

If using remote storage, set env variables for authentication
e.g

```
$ export AWS_ACCESS_KEY_ID=<access_key>
$ export AWS_SECRET_ACCESS_KEY=<secret_key>
```

[Setting up authentication for S3](https://www.mlflow.org/docs/latest/tracking.html#amazon-s3)

### Training
To track to an mlflow server set `MLFLOW_TRACKING_URI` env variable:  
`$ export MLFLOW_TRACKING_URI=http://localhost:5000`

If not set, will log experiments (data and artifacts) to `mlflow` folder in root directory

Run training script (with no arguments, will run with defaults shown below):  
```
$ python scripts/train.py \
  --train_dir data/train \
  --val_dir data/validate \
  --epochs 10 \
  --batch_size 32 \
  --exp_name test
```

Running on `data/train` will take a long time on CPU (~15 hours for 10 epochs on my machine), to test that everything runs use `--train_dir data/sample`

  - [ ] TODO: Add instructions for training on GPU


#### Run Flask app locally
To ensure app runs in debug mode set `FLASK_ENV` environment variable before running:  
`$ export FLASK_ENV=development`

Set `MODEL_URI` env variable  
`$ export MODEL_URI=s3://my_bucket/path/to/model`  

Points to an [MLFlow model](https://mlflow.org/docs/latest/models.html  ) with a valid [URI](https://www.mlflow.org/docs/latest/tracking.html#artifact-locations)

(if using S3, will also need to set `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` environment variables)

Start Flask app  
`$ flask run`


## Deploying To Heroku

1. Create heroku account and install heroku CLI: https://devcenter.heroku.com/articles/heroku-cli#download-and-install
2. `$ heroku create <app_name>`
3. Set env variables:  
`$ heroku config:set MODEL_URI=s3://my_bucket/path/to/model`  
(if using S3 will also need to set `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` )
4. `$ git push heroku master`
