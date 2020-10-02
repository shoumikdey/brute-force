import tensorflow as tf
import numpy as np


def get_image(filename):
    img = tf.keras.preprocessing.image.load_img(filename, target_size=(224, 224))
    img = tf.keras.preprocessing.image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    return tf.keras.applications.inception_v3.preprocess_input(img)


def get_prediction(img):
    model = tf.keras.applications.inception_v3.InceptionV3()
    test_image = get_image(img)
    predict = model.predict(test_image)
    results = tf.keras.applications.inception_v3.decode_predictions(predict)
    return results[0]
