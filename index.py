import random

class Ninja:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack = 10
        self.energy = 50
        self.heal = 10

    def attack(self, snake):
        self.energy -= 5
        if snake.health <= 30:
            snake.health -= random.randint(0, self.attack)
        else:
            snake.health -= 10
        print(f"{self.name} has attacked {snake.name} for {self.attack}!")
        print(f"{snake.name} has {snake.health} health left!")
        return self

    def heal(self):
        self.health += 10
        print(f"{self.name} has healed for {self.heal} health!")
        return self

class Snake:
    def __init__(self, name, attack):
        self.name = name
        self.health = 75
        self.attack = attack
        self.energy = 50
        self.heal = 10

    def attack(self, ninja):
        if (ninja.health > 70):
            ninja.health -= 25
        else:
            ninja.health -= 15
        print(f"{self.name} has attacked {ninja.name} for {self.attack}!")
        print(f"{ninja.name} has {ninja.health} health left!")
        return self

    def heal(self):
        self.health += 10
        print(f"{self.name} has healed for {self.heal} health!")
        return self

Penguin = Ninja("Jack")
Turtle = Snake("Hat", 0)

