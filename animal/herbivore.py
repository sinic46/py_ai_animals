from .basic_animal import Animal
from .enums import enum_animal_type
from random import randint


class Herbivore(Animal):
    def __init__(self, id: int, image_file_path: str, velocity: int,  max_x: int, min_x: int, max_y: int, min_y: int, size: tuple[int, int]):
        super().__init__(id, enum_animal_type.HERBIVORE, image_file_path,
                         velocity,  max_x, min_x, max_y, min_y, size)

    def update(self, DEBUG: bool = False):
        """ this is used to decide which action is taken for the animal.

        :param DEBUG: boolean to check if debug mode is on.

        """
        choice = randint(1, 5)

        if (DEBUG):
            print(f'{self.id} is doing action {choice}')

        if (self.energy > 0):
            if (choice == 1):
                self.move_forward(self.move_energy_cost)
            elif (choice == 2):
                self.turn(self.agility)
            elif (choice == 3):
                self.turn(-self.agility)
            elif (choice == 4):
                self.eat_grass()

    def eat_grass(self):
        """ Simulates eating grass, adds energy to the animal.
        """
        if (self.energy <= 80):
            self.energy += 20
        else:
            self.energy = 100

    def move_forward(self, energy_cost: int):
        """ moves the animal forward and takes off the energy cost.

        :param: the energy cost to move forward.

        """

        self.energy -= energy_cost

        return super().move_forward()
