# This is a sample Python script.
import datetime



class Animal:
    was_born = False #проверяем было ли рождено животное после инициализации нельзя менять день рождения и цвет
    birthday = str #Установка дня рождения
    def get_birthday(self):
        return self.birthday
    def set_birthday (self):
        if self.was_born == True:
            print("Животное было рождено" + self.get_birthday() + "и с этим уже ничего не поделать")
        elif self.was_born == False:
            print("Введите день рождения зверя \n")
            date = input()
            self.birthday = date
    color = str #Установка цвета животного
    def get_color (self):
        return self.color
    def set_color (self):
        if self.was_born == True:
            print("Животное было рождено цвета" + self.get_color() + "и с этим уже ничего не поделать")
        elif self.was_born == False:
            print("Введите цвет зверя \n")
            color = input()
            self.color = color
    name = str #Установка клички животногоj
    def get_name (self):
        return self.name
    def set_name (self):
        print("Введите кличку животного")
        name = input()
        self.name = name

    def __init__(self):
        self.set_birthday()
        self.set_color()
        self.set_name()
        self.was_born = True




class Predator(Animal):
    kill_list = list
    def kill(self):
        pass
class Wolf(Predator):
    pass
class Tiger(Predator):
    pass

class Herbivore(Animal):
    is_herbivore = True
    is_alive = True
    def kick(self):
        pass
class Deer(Herbivore):
    pass
class Boar(Herbivore):
    pass




class Zoo:
    pets = []
    def __init__(self):
        self.x = int(input('на какое количество животных создается зоопарк \n'))
        #add animals to zoo
        i = 0
        while i < self.x:
            print("Кого добавляем\nволк - ввести 1\nтигр - ввести 2\nолень - ввести 3\nкабан - ввести 4\n")
            z = int(input())
            if z == 1:
                self.pets.append(Wolf())
            elif z == 2:
                self.pets.append(Tiger())
            elif z == 3:
                self.pets.append(Deer())
            elif z == 4:
                self.pets.append(Boar())
            i += 1
        print("Зоопарк создан и можно веселиться в зоопарке находится " + str(len(self.pets)) + "зверей")
    def lets_play (self):
        while True:
            day = 1
            print("В зоопарке рассвет дня " + str(day) + " в клетках сидят")
            for pet in self.pets:
                print(Animal(pet).get_name)

            day += 1
            break



Z = Zoo()
Z.lets_play()

