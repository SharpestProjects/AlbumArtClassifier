import argparse
from album_art_classifier.train_model import train_model
from album_art_classifier.model import model


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--data_dir', default='data/train')
	parser.add_argument('--save_path', default='trained_models/model.h5')
	parser.add_argument('--epochs', type=int, default=10)
	parser.add_argument('--batch_size', type=int, default=32)

	args = parser.parse_args()
	kwargs = vars(args)

	train_model(model, **kwargs)
