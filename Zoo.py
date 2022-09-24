import Animal

class Zoo:
    pets: list[Animal]
    max_size: int
    def __init__(self, max_size: int):
        self.max_size = max_size
    def add_pet_too_zoo(self, pet):
        if not isinstance(pet, [Animal.Boar, Animal.Tiger, Animal.Deer, Animal.Wolf]):
            raise Exception("Не то животное")
        if self.n < self.max_size:
            self.pets.append(pet)
            self.n += 1
        else:
            raise Exception("Переполнен зоопарк")
#sadrfsfdasdasd


