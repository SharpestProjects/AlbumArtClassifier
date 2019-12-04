from tensorflow.keras.models import load_model

<<<<<<< HEAD

def load_keras_model(model_path):
    print('Loading model from', model_path)
    model = load_model(model_path)
    return model
=======
# TODO: Load model from remote storage
print('Loading model...')
model = load_model('trained_models/model.h5')
>>>>>>> master
