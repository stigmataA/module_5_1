# создание класса House
class House:
    def __init__(self, name, number_of_floors):
        #инициализация атрибутов объекта
        self.name = name
        self.numder_of_floors = number_of_floors

    def go_to(self, new_floor):
        # проверка на вхождение new_floor в диапозон number_of_floors
        if 0 < new_floor <= self.numder_of_floors:
            # выводим на экран последовательно номера этажов от 1 до new_floor
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            # выводим сообщение об ошибке
            print(f'Такого этажа не существует')


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
