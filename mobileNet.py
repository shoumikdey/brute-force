import tensorflow as tf
import numpy as np


def getImage(filename):
    img = tf.keras.preprocessing.image.load_img(filename, target_size=(224, 224))
    img = tf.keras.preprocessing.image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    return tf.keras.applications.mobilenet_v2.preprocess_input(img)


model = tf.keras.applications.mobilenet_v2.MobileNetV2()
test_image = getImage('German_Shepherd.jpg')
predict = model.predict(test_image)
results = tf.keras.applications.imagenet_utils.decode_predictions(predict)
print(results)
