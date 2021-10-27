from pet import Pet
#LETS PRACTICE RETRIEVING THE LAST PUSH


class Ninja:
    def __init__(self,first_name,last_name,pet,breed,treats="treat", pet_food="kibble"):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = Pet(pet,breed)
        self.pet_food = pet_food
        self.treat = treats

    def walk(self):
        self.pet.play()

    def feed(self,treat):
        self.pet.eat(treat)

    def bathe(self):
        self.pet.noise()

    def checkup(self):
        self.pet.display_stats()

    def bed_time(self):
        self.pet.sleep()


jeff = Ninja('Jeff', 'Clapper', 'Kenya','Dog')
jeff.walk()
jeff.feed(jeff.treat)
jeff.checkup()
jeff.bed_time()
jeff.bathe()
jeff.walk()
jeff.bed_time()
jeff.checkup()
