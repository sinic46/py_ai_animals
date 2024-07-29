import keras
import os


class Dna():
    def __init__(self, model_shape: tuple[int, int, int, int]):

        self.model = keras.Sequential()

        self.model.add(keras.Input(shape=(model_shape[0],)))
        self.model.add(keras.layers.Dense(model_shape[1]))
        self.model.add(keras.layers.Dense(model_shape[2]))
        self.model.add(keras.layers.Dense(model_shape[3]))


    def load_weights(self,weights_filename):
        pass
        


if (__name__ == '__main__'):
    dna = Dna((10, 64, 64, 5))
    print(dna.model.get_weights())

