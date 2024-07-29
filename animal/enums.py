
from enum import Enum

class enum_animal_type(Enum):
    HERBIVORE = 10
    CARNIVORE = 20
    OMNIVORE = 30



if(__name__ == '__main__'):
    print(enum_animal_type(10))