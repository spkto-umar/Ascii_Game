from Colours import Colour
from Spell import Spell
import random
import pyttsx3
import sys


class Hero(Spell):
    __hp = 100

    def __init__(self, name, attack_power, armour=0, magic_power=0, magic_owned=[], magic_heals=[]):
        self.__name = name.capitalize()
        self.__attack_low = attack_power-6 if attack_power-6 > 2 else 2
        self.__attack_high = attack_power+4
        self.__armour = armour
        self.__magic_power = magic_power
        self.__magic_owned = magic_owned
        self.__magic_heals = magic_heals
        self.__actions = ["Sword Attack", "Magic attack", "Heal"] if magic_power>0 else ["Sword Attack"]

    def getHealth(self):
        return self.__hp
    
    def reset(self,mp):
        self.__hp=100
        self.__magic_power=mp

    def __addHealth(self, hp):
        self.__hp += hp
        if self.__hp > 100:
            self.__hp = 100

    def getName(self):
        return self.__name

    def getAttackPower(self):
        return self.__attack_low, self.__attack_high

    def getMagicPower(self):
        return self.__magic_power

    def getMagicHeals(self):
        return [potion.__str__() for potion in self.__magic_heals]

    def getMagicOwned(self):
        return [magic.__str__() for magic in self.__magic_owned]

    def __reduceMagicPowerBy(self, magic_power):
        self.__magic_power -= magic_power

    def getArmour(self):
        return self.__armour

    def __setArmour(self, armour):
        self.__armour = armour

    def getActions(self):
        return self.__actions

    def damageTaken(self, damage):
        if self.__armour < damage:
            self.__hp = self.__hp+self.__armour-damage
            if self.__hp < 0:
                self.__hp = 0

    def generateDamage(self):
        damage = random.randrange(self.__attack_low, self.__attack_high)
        print(self.getOkGreen()+self.__name, "attacked enemy for",
              damage, "health points"+self.getEnd())
        return damage

    def __chooseMagic(self):
        while True:
            print(self.__name, "Magical capabilities:")
            index = 1
            for i in self.__magic_owned:
                print(index, "Ability:", i.getName(),end="")
                s=""
                for x in range(20-len(i.getName())):
                    s+=" "
                print(s,end="")
                print("\tDamage Type:", i.getType())
                index += 1

            choice = int(input("Choice magic to attack\n"))-1
            if choice >= 0 and choice < len(self.__magic_owned):
                return choice
            if choice == -1:
                print(self.getFail() + self.getBold() +
                      "\n" + self.runningAway()+self.getEnd())
                sys.exit()
            print(self.getHeader() + self.getUnderline()
                  + "No such capabilities learned you little girl.\nChoose again!"+self.getEnd())

    def __generateMagicDamage(self):
        choice = self.__chooseMagic()
        damage, cost = self.__magic_owned[choice].generateMagicDamage(
            self.__magic_power)
        self.__reduceMagicPowerBy(cost)
        print(self.getOkGreen()+self.__name, "used", self.__magic_owned[choice].getName(), "to attack for",
              damage, "health points"+self.getEnd())
        return damage

    def __chooseHeals(self):
        while True:
            print(self.__name, "Healing potions:")
            index = 1
            for i in self.__magic_heals:
                print(index, "Potion:", i.getName())
                index += 1

            choice = int(input("Choice potion\n"))-1
            if choice >= 0 and choice < len(self.__magic_heals):
                return choice
            if choice == -1:
                print(self.getFail() + self.getBold() +
                      "\n" + self.runningAway()+self.getEnd())
                sys.exit()
            print(self.getHeader() + self.getUnderline()
                  + "No such potions owned you moron.\nChoose again!"+self.getEnd())

    def __healHero(self):
        choice = self.__chooseHeals()
        hp, cost = self.__magic_heals[choice].generateHealth(
            self.__magic_power)
        self.__addHealth(hp)
        self.__reduceMagicPowerBy(cost)
        print(self.getOkGreen()+self.__name, "healed himself for",
              hp, "health points"+self.getEnd())

    def chooseAction(self):
        while True:
            print("How do you wanna fight,", self.__name)
            index = 1
            for i in self.__actions:
                print(index, i)
                index += 1

            choice = int(
                input("Enter fighting style or zero to run away anytime.\n"))-1

            if choice == 0:
                return self.generateDamage()
            elif choice == 1 and self.__magic_power!=0:
                return self.__generateMagicDamage()
            elif choice == 2 and self.__magic_power!=0:
                self.__healHero()
                return None

            if choice == -1:
                print(self.getFail() + self.getBold() +
                      "\n"+self.runningAway() + self.getEnd())
                sys.exit()
            print(self.getHeader() + self.getUnderline()
                  + "No such talent in your bones, Mister on Cloud9.\nChoose again!"+self.getEnd())

    def runningAway(self):
        sentence = self.__name + \
            " the old geezer, has run away from battlefield with his arithritis."
        speed = 160
        engine = pyttsx3.init()
        engine.setProperty('rate', speed)
        engine.say(sentence)
        engine.runAndWait()
        return sentence

    def __str__(self):
        return "Hero Name: {0}, Health: {1}, Low_Attack_Power: {2}, High_Attack_Power: {3}, Armour: {4}, Magic_Power: {5}, Magic_mastered: {6}, Potions_learned: {7}, Actions: {8} ".format(
            self.__name, self.__hp, self.__attack_low, self.__attack_high, self.__armour, self.__magic_power,
            self.getMagicOwned(), self.getMagicHeals(), self.__actions)
