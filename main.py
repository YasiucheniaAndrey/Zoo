from zoo import Zoo
import animal
import datetime

if __name__ == '__main__':
    z = Zoo(5)
    z.add_pet_too_zoo(animal.Boar(datetime.now(), "Серенький", "Малыш"))

