import random
import pyttsx3
from Colours import Colour


class Enemy(Colour):
    __hp = 100

    def __init__(self, name, attack_power, armour=0):
        self.__name = name.capitalize()
        self.__attack_low = attack_power-4
        self.__attack_high = attack_power+7
        self.__armour = armour

    def getName(self):
        return self.__name

    def getAttackPower(self):
        return self.__attack_low, self.__attack_high

    def setAttackPower(self, attack_power):
        self.__attack_low = attack_power-4
        self.__attack_high = attack_power+7

    def getHealth(self):
        return self.__hp

    def getArmour(self):
        return self.__armour

    def setArmour(self, armour):
        self.__armour = armour

    def damageTaken(self, damage):
        if self.__armour < damage:
            self.__hp += self.__armour-damage
            if self.__hp < 0:
                self.__hp = 0

    def armourAI(self):
        if self.__hp < 40 and self.__armour <= 3:
            if self.__armour == 0:
                self.__armour = 3
            self.setArmour((int)(self.__armour*1.5))
            # to act like a jumpscare
            sentence = self.__name+" has hardened its muscles."
            speed = 170
            engine = pyttsx3.init()
            engine.setProperty('rate', speed)
            engine.say(sentence)
            engine.runAndWait()
            print("\n"+self.getWarning()+sentence+self.getEnd())

    def healthAI(self):
        if self.__hp < 25:
            self.__hp *= 2
            # to act like a jumpscare!!!
            sentence = self.__name+" has pumped up its Adrelanine production."
            speed = 170
            engine = pyttsx3.init()
            engine.setProperty('rate', speed)
            engine.say(sentence)
            engine.runAndWait()
            print("\n"+self.getWarning()+sentence+self.getEnd())

    def generateDamage(self):
        damage = random.randrange(self.__attack_low, self.__attack_high)
        return damage

    def __str__(self):
        return "Enemy Name: {0}, Health: {1}, Low_Attack_Power: {2}, High_Attack_Power: {3}, Armour: {4} ".format(self.__name, self.__hp, self.__attack_low, self.__attack_high, self.__armour)
