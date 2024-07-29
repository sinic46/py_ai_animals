from .herbivore import Herbivore


class Cow(Herbivore):
    def __init__(self, id, max_x: int, min_x: int, max_y: int, min_y: int):
        super().__init__(id=id, image_file_path=r'.\animal\images\cow.png', velocity=10,
                         max_x=max_x, min_x=min_x, max_y=max_y, min_y=min_y, size=(10, 20))
