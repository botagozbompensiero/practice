# Есть класс Person, конструктор которого принимает три параметра (не учитывая self) – имя,
# фамилию и квалификацию специалиста. Квалификация имеет значение заданное по умолчанию, равное единице.
#
# У класса Person есть метод, который возвращает строку, включающую в себя всю информацию о сотруднике.
#
# Класс Person содержит деструктор, который выводит на экран фразу "До свидания, мистер …"
# (вместо троеточия должны выводиться имя и фамилия объекта).
#
# В основной ветке программы создайте три объекта класса Person. Посмотрите информацию о
# сотрудниках и увольте самое слабое звено.
#
# В конце программы добавьте функцию input(), чтобы скрипт не завершился сам, пока не будет нажат Enter.
# Иначе вы сразу увидите как удаляются все объекты при завершении работы программы.

class Person:

    def __init__(self, n, sn, lvl = 1):
        self.name = n
        self.surname = sn
        self.level = lvl

    def getInfo(self):
        print(f'Name: {self.name}, Surname: {self.surname}, Level: {self.level}')

    def __del__(self):
        print(f'Goodbye, {self.name} {self.surname}, {self.level}')
        input()



first = Person('Lames', 'Baker', 4)
second = Person('dfd', 'rrr')
third = Person('yyy', 'oooo', 2)
first.getInfo()
second.getInfo()
third.getInfo()
second.__del__()
