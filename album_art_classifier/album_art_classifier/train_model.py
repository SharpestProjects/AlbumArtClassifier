import math
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from album_art_classifier.utils import count_files_in_dir


def train_model(
	model,
	train_dir='data/train',
	val_dir='data/validate',
	save_path=None,
	epochs=10,
	batch_size=32,
	callbacks=[]
):
	model.compile(
		loss='binary_crossentropy',
		optimizer='rmsprop',
		metrics=['acc']
	)

	data_gen = ImageDataGenerator(rescale=1. / 255)

	train_generator = data_gen.flow_from_directory(
		train_dir,
		target_size=(300, 300),
		class_mode='binary',
		batch_size=batch_size
	)

	val_generator = data_gen.flow_from_directory(
		val_dir,
		target_size=(300, 300),
		class_mode='binary',
		batch_size=batch_size
	)

	train_steps = math.floor(count_files_in_dir(train_dir) / batch_size)
	val_steps = math.floor(count_files_in_dir(val_dir) / batch_size)

	print('Training model...')
	model.fit_generator(
		train_generator,
		validation_data=val_generator,
		validation_steps=val_steps,
		steps_per_epoch=train_steps,
		epochs=epochs,
		verbose=1,
		callbacks=callbacks
	)

	if save_path is not None:
		print('Saving model as', save_path)
		model.save(save_path)

	return model
