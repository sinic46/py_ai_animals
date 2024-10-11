import keras
from uuid import uuid4
from animal import enums


class Dna():
    def __init__(self, action_enum:enums.Enum_Animal_Actions, model_shape: tuple[int, int, int, int] = (10, 15, 15, 5)):

        self.model = keras.Sequential()

        self.guid = uuid4()

        self.model.add(keras.Input(shape=(model_shape[0],)))
        self.model.add(keras.layers.Dense(model_shape[1]))
        self.model.add(keras.layers.Dense(model_shape[2]))
        self.model.add(keras.layers.Dense(model_shape[3]))
        self.model.add(keras.layers.Dense(len(action_enum)))

    def load_weights(self, guid=None):

        if (guid == None):
            guid = self.guid

        self.model.load_weights(
            f".\\genes\\weights\\{guid}.weights.h5", by_name=True, skip_mismatch=True)

    def save_weights(self):
        self.model.save_weights(
            f".\\genes\\weights\\{dna.guid}.weights.h5", True)

    def get_weights(self):
        return self.model.get_weights()

    def set_weights(self, weights):
        self.model.set_weights(weights)

    def get_model_results(self, *args):
        return self.model.predict(args)


if (__name__ == '__main__'):
    dna = Dna()

    print(f"model weights:{len(dna.get_weights())}")
