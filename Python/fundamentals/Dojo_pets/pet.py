class Pet:
    def __init__(self,name,breed,health = 100,energy = 100):
        self.name = name
        self.breed = breed
        self.energy = energy
        self.health = health

    def sleep(self):
        print(f'awww.... {self.name} is sleeping')
        self.energy += 25

    def eat(self, food):
        print(f"{self.name} is eating {food}. It looks yummy!")
        if food == "treat":
            self.energy += 10
            self.health += 1
        else:
            self.energy += 5
            self.health += 10

    def play(self):
        print(f"{self.name} is playing! So adorable!")
        self.health += 5
        self.energy -= 50

    def noise(self):
        print(f"{self.name} whined.... {self.name} doesn't like baths...")
        self.health += 5

    def display_stats(self):
        print(self.health)
        print(self.energy)