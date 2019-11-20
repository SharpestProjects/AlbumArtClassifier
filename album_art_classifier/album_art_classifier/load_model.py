from tensorflow.keras.models import load_model

# TODO: Load model from remote storage
print('Loading model...')
model = load_model('trained_models/model.h5')
