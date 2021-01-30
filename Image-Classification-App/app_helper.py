from tensorflow.keras.applications.resnet50 import ResNet50 as myModel
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions

from tensorflow.keras.preprocessing import image
import numpy as np

def get_classes(file_path):
    model = myModel(weights="imagenet")

    img = image.load_img(file_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x= np.array([x])
    x = preprocess_input(x)

    preds = model.predict(x)
    predictions = decode_predictions(preds, top=3)[0]
    return predictions
