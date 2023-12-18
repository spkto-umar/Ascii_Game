from Default import DefaultPlay
from Enemy import Enemy
from Hero import Hero
from ConfigurePlayers import PlayerData


class Caller(DefaultPlay):

    def normalGame(self):
        player_stats = PlayerData()

        name, a_power, armour, mp, magic_owned, heal_potion = player_stats.inputPlayerDetails(False)
        heroPlayer = Hero(name, a_power, armour, mp, magic_owned, heal_potion)
        # print(heroPlayer)
        enemylist=[]

        level=1
        while heroPlayer.getHealth()>0:
            heroPlayer.reset(mp)

            for i in range(level):
                enemy = Enemy("Soldier "+str(i+1), 10+i+1, 4+i+1)
                enemylist.append(enemy)
                # print(enemy)
            
            self.play(heroPlayer,enemylist)
            level+=1
    
    def customGame(self):
        player_stats = PlayerData()

        name, a_power, armour, mp, magic_owned, heal_potion = player_stats.inputPlayerDetails(False)
        heroPlayer = Hero(name, a_power, armour, mp, magic_owned, heal_potion)
        # print(heroPlayer)

        name, a_power, armour, *useless = player_stats.inputPlayerDetails(True)
        enemyPlayer1 = Enemy(name, a_power, armour)
        # print(enemyPlayer1)

        name, a_power, armour, *useless = player_stats.inputPlayerDetails(True)
        enemyPlayer2 = Enemy(name, a_power, armour)
        # print(enemyPlayer2)
        
        self.play(heroPlayer,[enemyPlayer1,enemyPlayer2])

    
    def pvpGame(self):
        player_stats = PlayerData()

        name, a_power, armour, mp, magic_owned, heal_potion = player_stats.inputPlayerDetails(False)
        Player1 = Hero(name, a_power, armour, mp, magic_owned, heal_potion)
        # print(Player1)

        name, a_power, armour, mp, magic_owned, heal_potion = player_stats.inputPlayerDetails(False)
        Player2 = Hero(name, a_power, armour, mp, magic_owned, heal_potion)
        # print(Player2)
        
        
        self.pvpPlay(Player1,Player2)

    def main(self):
        self.startImage()
        while True:
            print("Welcome to Ascii Battle. ")
            print("Choose style of play:")
            print("1 - Normal Game")
            print("2 - Custom Game")
            print("3 - Two Player Game")
            choice=int(input("Choose style of play:"))

            if choice==1:
                self.normalGame()
                break
            elif choice==2:
                self.customGame()
                break
            elif choice==3:
                self.pvpGame()
                break
            else:
                print(self.getFail()+"You didn't desighned the game bushy hair, So shut your .... and choice from the option"+self.getEnd())
    print("Game Ended Sire")


start=Caller()
start.main()