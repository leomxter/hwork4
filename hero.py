class SuperHero:
    people='people'
    fly = True
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
    def nameHero(self):
        print("Name hero is", self.name)
    
    def squarehealth_points(self):
        print("Health_points: ",self.health_points * 2)

    def __str__(self) -> str:
        return f"Status hero:\nNikname hero - {self.nickname}\nSuperpower hero - {self.superpower}\nhealth_points hero - {self.health_points}"
        
    def __len__(self):
        return len(self.catchphrase)
# hero = SuperHero("Toni Stark", "Ironman", "Inventor", 100, "I'm just Ironman")
# hero.nameHero()
# hero.myltyhealth_points()
# print(hero)
# print(len(hero))
# print(SuperHero.people())

class Airhero(SuperHero): 
    people ="Asgardian"
    def myltyhealth_points(self):
        print(self.health_points**2)
    def __init__(self, name, nickname, superpower, health_points, catchphrase , fly = False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.fly= fly
    def __str__(self) -> str:
        return f"Status hero:\nNikname hero - {self.nickname}\nSuperpower hero - {self.superpower}\nhealth_points hero - {self.health_points}\nfly {self.fly}"
        
    def new_metod(self):
        self.fly = True
        print(f"fly in the True_phrase: {self.fly }")


class Landhero(Airhero):
    people = "athland"
    def new_metod(self):
        self.fly= False
        print(f"fly in the True_phrase: {self.fly }")

class Cosmohero(Landhero):
   people = "people"



hero_1 = Airhero("Gon" , "Gon","Force" ,300, "Rock, paper, siasers!")
print(hero_1)
hero_1.squarehealth_points()
hero_1.new_metod()

hero_2 = Landhero("Killua","Killer","zap",200,"Now, your heart is mine")
print(hero_2)
hero_2.squarehealth_points()
hero_2.new_metod()


hero_3 = Cosmohero("Hisoka","Hisokabek","Card",250,"I will kill you anyway")
print(hero_3)
hero_3.squarehealth_points()
hero_3.new_metod()