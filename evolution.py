from random import randint
class Monkey:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(self.name.title() + " eat's banana" )
#mon1 = Monkey('Aram')
#print(mon1.name)
#mon1.eat()

class Australopithecus(Monkey):
    def __init__(self,name,weapon = 'stick'):
        Monkey.__init__(self,name)
        #self.name = name
        self.__weapon = weapon

    def take_a_weapon(self):
        print(f"{self.name.title()} take's a  {self.weapon}")

    @property
    def weapon (self):
        #print('pro')
        return(self.__weapon)

    @weapon.setter
    def weapon(self,value):
        print('setter')
        if value.lower() != 'stic':
            raise ValueError(f"{self.name} take's only stic ")
        else:
            self.__weapon = value


#jab = Australopithecus('Leonya')
#print(jab.name,jab.weapon)
#jab.eat()
#jab.weapon = 'wood'
#jab.take_a_weapon()



class Homo_habilis(Australopithecus):
    def __init__(self,name,things_1,things_2):
        Australopithecus.__init__(self, name, weapon='stick')
        #self.name = name
        self.things_1 = things_1
        self.things_2 = things_2
    def make_a_gun(self):
        if self.things_1 == 'stic' and self.things_2 == 'wood':
            digit = randint(1,3)
            if digit == 1:
                txt = 'You made the ax'
                print(txt)
                return txt
            elif digit == 2:
                txt = 'You made the spear'
                print(txt)
                return txt
            elif digit == 3:
                txt = 'You spend a lot of time to make the things. Tigers ate you.'
                print(txt)
                return txt
        else:
            raise ValueError ('In my cenry we have only stic and wood')


#Klava = Homo_habilis('Klava','stic','wood')
#Klava.make_a_gun()
#Klava.eat()


class Homo_erectus(Homo_habilis):
    def __init__ (self,name,thing_1,thing_2):
        Homo_habilis.__init__(self,name,thing_1,thing_2)
        self.name = name
    def hunting(self):
        gun = Homo_habilis.make_a_gun(self)
        food = randint (1,2)

        if gun ==  'You made the ax' or 'You made the spear':
            if food == 1:
                print('You kill mamonth')
                return(True)
            else:
                print('Mamonth kill you ')
                return(False)
        else:
            print('You is fool and die, when you did the gun')
            return(False)
#New_Klava = Homo_erectus('Klava2','stic','wood')
#New_Klava.hunting()
#New_Klava.eat()



class Homo_neanderthalensis(Homo_erectus):
    def __init__(self, name,thing_1, thing_2):
        Homo_erectus.__init__(self,name,thing_1,thing_2)
    def make_fire(self):
        successful_hunt = Homo_erectus.hunting(self)
        if successful_hunt == True:
            count_wood = randint(1, 2)
            if count_wood == 2:
                print('You make a bonfire')
                return(True)
            else:
                print('You have only one wood and near not one more wood')
                return(False)
        else:
            print('Hello die')
            return(False)

#Klava3 = Homo_neanderthalensis('Klava2','stic','wood')
#Klava3.make_fire()
#Klava3.eat()

class Homo_sapiens(Homo_neanderthalensis):
    def __init__(self,name,thing_1, thing_2):
        Homo_neanderthalensis.__init__(self, name, thing_1, thing_2)
    def make_dinner(self):
        fire = Homo_neanderthalensis.make_fire(self)
        if fire == True:
            print('You make a dinner')
        else:
            print('hello die')

Klava3 = Homo_sapiens('Klava2','stic','wood')
Klava3.make_dinner()
Klava3.eat()
