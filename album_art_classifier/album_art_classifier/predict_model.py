import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array


def predict_model(model, file):
	try:
		x = img_to_array(load_img(file)) / 256
	except: # noqa E722
		return 'Invalid input', 400

	# TODO: validate input
	pred = model.predict(np.expand_dims(x, axis=0))

	print('Input', x)
	print('Output', pred)

	genre = 'metal!' if pred[0][0] < 0.5 else 'not metal'

	return genre
