class Hero_name:
    def __init__(self, name):
        self.name = name
        return f'{self.name}'

class Hero_age:
    def __init__(self, age):
        self.age = age
        return f'{self.age}'

class Hero_hp:
    def __init__(self, hp):
        self.hp = hp
        return f'{self.hp}'


class Hero_power:
    def __init__(self, power):
        self.power = power
        return f'{self.power}'

class Hero(Hero_name, Hero_age, Hero_hp, Hero_power):
    def __init__(self,name,age,hp,power):
        Hero_name.__init__(self,name)
        Hero_age.__init__(self,age)
        Hero_hp.__init__(self,hp)
        Hero_power.__init__(self,power)

    def __str__(self):
        return f'{self.name} {self.age} {self.hp} {self.power}'

hero = Hero('Elmo', 14, 'health is full', 'power is thunder')
print(hero)