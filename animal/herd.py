import numpy as np
import sys
from typing import Type

from animal.basic_animal import Animal

np.set_printoptions(threshold=sys.maxsize)


class Herd:
    def __init__(self, herd_size:int, animal_type:Type[Animal]) -> None:
        self.herd_size = herd_size


    def get_herd(self):
        return self.animals

    def get_herd_locations(self):
        return [animal.location for animal in self.animals]


if (__name__ == "__main__"):
    herd = Herd(30, Animal)

    print(herd.herd_size)

    herd_locations = herd.get_herd_locations()

    starting_area = np.full((100, 100,3),0)

    for count, animal_loc in enumerate(herd_locations):

        print(count)


    print(starting_area)
