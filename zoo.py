import animal


class NotAnimalException(Exception):
    pass


class ZooLimitException(Exception):
    pass


class Zoo:
    pets: list[animal]
    max_size: int
    n = 0

    def __init__(self, max_size: int):
        self.max_size = max_size

    def add_pet_too_zoo(self, pet):
        if not isinstance(pet, animal.Animal):
            raise NotAnimalException()
        if self.n < self.max_size:
            self.pets.append(pet)
            self.n += 1
        else:
            raise ZooLimitException()
