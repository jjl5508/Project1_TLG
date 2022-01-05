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
        print(f"{self.name} has attacked {snake.name}!")
        print(f"{snake.name} has {snake.health} health left!")
        return self

    def heal(self):
        self.health += 10
        print(f"{self.name} has healed for {self.heal} health!")
        return self

    def status(self):
        print(f"The Ninja has {self.health} health remaining.")


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
        print(f"{self.name} has attacked {ninja.name}!")
        print(f"{ninja.name} has {ninja.health} health left!")
        return self

    def heal(self):
        self.health += 10
        print(f"{self.name} has healed for {self.heal} health!")
        return self

    def status(self):
        print(f"The Snake has {self.health} health remaining.")


Penguin = Ninja("Jack")
Turtle = Snake("Bob", 0)
while True:
    Question01 = input("Do you want to attack the Ninja? (Y/M/N)")
    answer01 = input()

    if answer01 == "Y":
        Snake.attack(Turtle, Penguin)
        Question01 = input("Do you want to attack the Ninja again? (Y/N)")
        answer01 = input()
        if answer01 == "Y":
            Snake.attack(Turtle, Penguin)
    elif answer01 == "M":
        Question02 = input("Do you want to attack the Snake? (Y/M/N)")
        answer02 = input()
        if answer02 == "Y":
            Ninja.attack(Penguin, Turtle)
        elif answer02 == "M":
            Question03 = input("Would you like to heal? (Y/N)")
            answer03 = input()
            if answer03 == "Y":
                Ninja.heal(Penguin)
            else:
                Ninja.status(Penguin)
        else:
            print("Thank you for playing!")
    else:
        Snake.heal(Turtle)
        Snake.status(Turtle)
    play = input("Play again? (y/n): ")
    if play.lower()!= "y":
        print("Thanks for playing!")
        break
