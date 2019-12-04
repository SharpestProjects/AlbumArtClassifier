from tensorflow.keras.models import load_model


def load_keras_model(model_path):
    print('Loading model from', model_path)
    model = load_model(model_path)
    return model
