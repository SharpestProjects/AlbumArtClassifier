import argparse

import mlflow
from tensorflow.keras.callbacks import Callback

from album_art_classifier.train_model import train_model
from album_art_classifier.model import model


class MlFlowKerasLogger(Callback):
	def __init__(self):
		pass

	def on_train_begin(self, logs={}):
		print('hi?')
		mlflow.log_params(self.params)

	def on_epoch_end(self, epoch, logs={}):
		mlflow.log_metrics({
			'acc': logs['acc'],
			'loss': logs['loss']
		}, step=epoch)


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--data_dir', default='data/train')
	parser.add_argument('--save_path', default='trained_models/model.h5')
	parser.add_argument('--epochs', type=int, default=10)
	parser.add_argument('--batch_size', type=int, default=32)
	parser.add_argument('--exp_name', default='test')

	args = parser.parse_args()
	kwargs = vars(args)
	exp_name = kwargs.pop('exp_name')

	experiment_id = mlflow.set_experiment(exp_name)
	with mlflow.start_run(experiment_id=experiment_id):
		train_model(model, callbacks=[MlFlowKerasLogger()], **kwargs)
