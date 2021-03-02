# Есть класс "Воин". От него создаются два экземпляра-юнита.
# Каждому устанавливается здоровье в 100 очков.
# В случайном порядке они бьют друг друга. Тот, кто бьет, здоровья не теряет.
# У того, кого бьют, оно уменьшается на 20 очков от одного удара.
# После каждого удара надо выводить сообщение, какой юнит атаковал, и сколько у противника осталось здоровья.
# Как только у кого-то заканчивается ресурс здоровья, программа завершается сообщением о том, кто одержал победу.

class Warrior:

    def setName(self, n):
        self.name = n
        self.health = 100

    def battle(self, other):
        if self.health > 0:
            self.health = self.health - 20
            print(f"{self.name}'s health is {self.health}. Napadal {other.name}")
        if self.health == 0:
            print(f'{other.name} is the winner')
        if other.health == 0:
            print(f'{self.name} is the winner')


Warrior_1 = Warrior()
Warrior_2 = Warrior()
Warrior_1.setName('Judy')
Warrior_2.setName('Mila')

while Warrior_1.health != 0 and Warrior_2.health != 0:
    rand = random.randint(1, 3)
    if rand == 1:
        Warrior.battle(Warrior_1, Warrior_2)
    if rand == 2:
        Warrior.battle(Warrior_2, Warrior_1)

