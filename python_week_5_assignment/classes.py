# Assignment 1
class Superhero:
    def __init__(self, suit, realname):
        self.suit = suit
        self.realname = realname

    def fly(self):
        print(f'{self.realname} is flying.')

    def good(self):
        return "Superheroes fight for justice."

class Antihero(Superhero):
   def good(self):
        return "Antiheroes aren't necessarily good."
        

superman = Superhero('blue and red', 'Clerk')
omniman = Antihero('white and red', 'Nolan')

for hero in [superman, omniman]:
    print(hero.good())

# Assignment 2
class Animal:
    def move(self):
        return "walking"
    
class Fish:
    def move(self):
        return "swimming"
    
class Insect:
    def move(self):
        return "crawling"
    
for organism in [Animal(), Fish(), Insect()]:
    print(organism.move()) 