import simplejson as json
import os
from Spell import Spell


class PlayerData:

    def inputPlayerDetails(self, enemy):
        if enemy == False:
            name = input("Enter your name : ")
        else:
            name = input("Enter enemy name: ")

        a_power = int(input("Enter attacking power : "))
        if a_power <= 0:
            print(
                "Attacking power cannot be less than or equal to 0.\nSetting it to lowest power.")
            a_power = 1
        elif a_power > 15:
            print(
                "Attacking power cannot be more than 15.\nSetting it to highest power.")
            a_power = 15

        armour = int(input("Enter armour strength : "))
        if armour > 8:
            print("Armour cannot be more than 8.\nSetting it to maximium armour.")
            armour = 8
        elif armour < 0:
            print("Armour cannot be negative.\nSetting it to lowest armour.")
            armour = 0

        if enemy != True:
            mp = int(input("Enter magical strength: "))
            if mp < 0:
                print(
                    "Magical power cannot be negative.\nSetting it to lowest magical strength.")
                mp = 0
            elif mp > 100:
                print(
                    "Magical power cannot be more than 100.\nSetting it to highest magical strength.")
                mp = 100
        else:
            mp = 0

        if mp == 0:
            return name, a_power, armour, 0, [], []

        magic_owned, heal_potion = self.magicalCapabilities()

        return name, a_power, armour, mp, magic_owned, heal_potion

    def magicalCapabilities(self):

        if os.path.isfile("saved_data.json") and os.stat("saved_data.json").st_size != 0:
            old_file = open("saved_data.json", "r+")
            data = json.loads(old_file.read())

            # del data["Magical Attacks"]
            # del data["Heal Potions"]
            # print(data)
            # print(data["Magical Attacks"])
            # print(data["Heal Potions"])

        else:
            old_file = open("saved_data.json", "w+")
            data = {
                "Magical Attacks": [
                    {
                        "name": "Fire Ball",
                        "cost": 15,
                        "damage": 20,
                        "type": "Fire"
                    },
                    {
                        "name": "Fire Blast",
                        "cost": 10,
                        "damage": 15,
                        "type": "fire"
                    },
                    {
                        "name": "Thunder Strike",
                        "cost": 9,
                        "damage": 13,
                        "type": "Lightning"
                    },
                    {
                        "name": "Water Blade",
                        "cost": 12,
                        "damage": 16,
                        "type": "Water"
                    },
                    {
                        "name": "Wind Arrow",
                        "cost": 6,
                        "damage": 10,
                        "type": "Air"
                    },
                    {
                        "name": "Earthquake",
                        "cost": 15,
                        "damage": 22,
                        "type": "Earth"
                    },
                    {
                        "name": "Tsunami Wave",
                        "cost": 20,
                        "damage": 26,
                        "type": "Water"
                    },
                    {
                        "name": "Explosions Boom",
                        "cost": 30,
                        "damage": 35,
                        "type": "Fire"
                    },
                    {
                        "name": "Tornado Hit",
                        "cost": 10,
                        "damage": 14,
                        "type": "Air"
                    }
                ],
                "Heal Potions": [
                    {
                        "name": "Bandage",
                        "cost": 15,
                        "damage": 15,
                        "type": "Healing"
                    },
                    {
                        "name": "Cure",
                        "cost": 20,
                        "damage": 20,
                        "type": "Healing"
                    },
                    {
                        "name": "Divine Heal",
                        "cost": 30,
                        "damage": 35,
                        "type": "Healing"
                    }
                ]
            }
            print("No saved file found.\nReverting to default spells.")
            # old_file.seek(0)
            # old_file.write(json.dumps(data))

        # print(type(data))
        choice = "yes"
        while choice == "yes":
            choice = input(
                "If you want to add your own magical attack technique, enter 'yes': ").lower()
            if choice == "yes":
                m_name = input("Enter magic name: ").capitalize()
                m_atp = int(input("Enter attack power: "))
                if m_atp <= 0:
                    m_atp = 1
                    print(
                        "Attacking power is too low.\nSetting it to lowest attacking power.")
                if m_atp >= 50:
                    print(
                        "Attacking power is too high.\nSetting it to highest attacking power.")
                    m_atp = 50
                m_cost = (int)(m_atp/1.4)
                m_type = input("Enter magic type: ").capitalize()
                data["Magical Attacks"].append(
                    {"name": m_name, "cost": m_cost, "damage": m_atp, "type": m_type})

            else:
                break

        old_file.close()
        old_file = open("saved_data.json", "w+")
        old_file.write(json.dumps(data))
        old_file.close()

        print("Choose any 5 magical power: ")
        playerMagic = []
        playerPotion=[]
        new_file = open("saved_data.json", "r+")
        data = json.loads(new_file.read())
        count = 0
        while count < 5:
            x = 0
            st=["" for y in range(len(data["Magical Attacks"]))]
            for i in data["Magical Attacks"]:
                st[x]=st[x]+"  Name: "+i["name"]
                while(len(st[x])<30):
                    st[x]+=" "
                st[x]+="Cost: "+str(i["cost"])
                while(len(st[x])<42):
                    st[x]+=" "
                st[x]+="Damage: "+str(i["damage"])
                while(len(st[x])<55):
                    st[x]+=" "
                st[x]+="Type: "+i["type"]
                x += 1


            x=0
            for i in data["Magical Attacks"]:
                x += 1
                st[x-1]=" "+str(x)+st[x-1] if x<=9 else str(x)+st[x-1]
                print(st[x-1])
                

            
            choice = int(input())
            if choice<1 or choice>x:
                continue
            magic=data["Magical Attacks"].pop(choice-1)
            st.remove(st[choice-1])
            spell=Spell(magic["name"],magic["cost"],magic["damage"],magic["type"])
            playerMagic.append(spell)
            count += 1

        while len(data["Heal Potions"])>0:
            magic=data["Heal Potions"].pop(0)
            spell=Spell(magic["name"],magic["cost"],magic["damage"],magic["type"])
            playerPotion.append(spell)

        return playerMagic, playerPotion
