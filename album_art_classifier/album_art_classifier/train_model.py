import math
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from album_art_classifier.utils import count_files_in_dir


def train_model(
	model,
	data_dir='data/train',
	save_path=None,
	epochs=10,
	batch_size=32
):
	model.compile(
		loss='binary_crossentropy',
		optimizer='rmsprop',
		metrics=['accuracy']
	)

	data_gen = ImageDataGenerator(rescale=1. / 255)

	train_generator = data_gen.flow_from_directory(
		data_dir,
		target_size=(300, 300),
		class_mode='binary',
		batch_size=batch_size
	)

	train_steps = math.floor(count_files_in_dir(data_dir) / batch_size)

	print('Training model...')
	model.fit_generator(
		train_generator,
		steps_per_epoch=train_steps,
		epochs=epochs,
		verbose=1
	)

	if save_path is not None:
		print('Saving model as', save_path)
		model.save(save_path)

	return model
