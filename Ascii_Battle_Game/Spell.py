from Colours import Colour
import random


class Spell(Colour):

    def __init__(self, name, cost, damage, type):
        self.__name = name.capitalize()
        self.__cost = cost
        self.__damage = damage
        self.__type = type.capitalize()

    def getName(self):
        return self.__name

    def getCost(self):
        return self.__cost

    def getDamage(self):
        return self.__damage

    def getType(self):
        return self.__type

    def generateMagicDamage(self, magic_power=0):

        if magic_power < self.__cost:
            print(self.getFail()+
                  "Not Enough Magic Power\n", self.getEnd())
            return 0, 0

        mgl = self.__damage-7
        mgh = self.__damage+10
        return random.randrange(mgl, mgh), self.__cost

    def generateHealth(self, magic_power=0):

        if magic_power < self.__cost:
            print(self.getFail()+
                  "Not Enough Magic Power to heal\n", self.getEnd())
            return 0, 0

        elif self.__type != 'Healing':
            print(self.getFail()+
                  "Wrong choice to heal\n", self.getEnd())
            return 0, 0

        mpl = self.__damage-7
        mph = self.__damage+7
        return random.randrange(mpl, mph), self.__cost

    def __str__(self):
        return "Spell Name: {0}, Cost: {1}, Damage: {2}, Type: {3} ".format(self.__name, self.__cost, self.__damage, self.__type)
