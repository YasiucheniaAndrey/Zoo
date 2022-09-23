import datetime

class Animal:
    def __int__(self, birthday: datetime, color: str, name: str):
        self.birthday = birthday
        self.color = color
        self.name = name
    def get_birthday(self):
        return self.birthday
    def get_color (self):
        return self.color
    def get_name (self):
        return self.name
    def set_name (self):
        name = input()
        self.name = name


class Predator(Animal):
    kill_list = []
    def kill(self, pet: Animal):
        if isinstance(pet, Herbivore):
            if not pet.kick():
                self.kill_list.append((datetime.now(), pet.get_name()))
class Wolf(Predator):
    pass
class Tiger(Predator):
    pass


class Herbivore(Animal):
    is_herbivore = True
    is_alive = True
    def kick(self):
        if not self.is_alive:
            return False
        self.is_alive = False


class Deer(Herbivore):
    pass


class Boar(Herbivore):
    pass
