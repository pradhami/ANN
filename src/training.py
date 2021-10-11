from yaml import parse
from src.utils.common import read_config
from src.utils.data_mgmt import get_data
from src.utils.model import create_model
import argparse

def training(config_path):
    config = read_config(config_path)
    validation_datasize = config["params"]["validation_datasize"]
    (x_train,y_train),(x_valid,y_valid),(x_test,y_test) = get_data(validation_datasize)

    LOSS_FUNCTION = config["params"]["loss_function"]
    OPTIMIZER = config["params"]["optimizer"]
    METRICS = config["params"]["metrics"]
    NUM_CLASSES = config["params"]["no_classes"]
    model = create_model(OPTIMIZER, LOSS_FUNCTION, METRICS, NUM_CLASSES)

    EPOCHS = config["params"]["epochs"]
    history = model.fit(x_train, y_train, epochs=EPOCHS, validation_data=(x_valid,y_valid), verbose=config.VERBOSE)


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('"--config',"-c",default="config.yaml")
    parsed_arg = args.parse_args()
    training(config_path = parsed_arg.config)