import tensorflow as tf
from src.utils.common import read_config
import time
import os

def create_model(OPTIMIZER, LOSS_FUNCTION, METRICS, NUM_CLASSES):
    LAYERS = [
            tf.keras.layers.Flatten(input_shape=[28,28], name = 'InputLayer'),
            tf.keras.layers.Dense(300, activation='relu', name = 'HiddenLayer1'),
            tf.keras.layers.Dense(100, activation='relu', name = 'HiddenLayer2'),
            tf.keras.layers.Dense(NUM_CLASSES, activation='softmax', name = 'OutputLayer')
            ]

    model_classifier = tf.keras.models.Sequential(LAYERS)

    model_classifier.compile(optimizer=OPTIMIZER, 
                                loss=LOSS_FUNCTION,
                                metrics=METRICS
                                )
    
    return(model_classifier)

def get_unique_filename(filename):
        unique_filename = time.strftime(f"%Y%m%d_%H%M%S_{filename}")
        return unique_filename

def save_model(model, model_name, model_dir):
        unique_filename = get_unique_filename(model_name)
        path_to_model = os.path.join(model_dir, unique_filename)
        model.save(path_to_model)