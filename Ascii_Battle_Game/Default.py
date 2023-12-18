from Printing import Printing
import random


class DefaultPlay(Printing):

    def play(self,hero,enemylist):

        print(self.getWarning(), self.getHeader(),"Enemy incoming!", self.getEnd())

        while True:

            # print("============================================================================")
            
            i=1
            if len(enemylist)>1:
                print("Enemy alive ")
                for j in enemylist:
                    print(i,j.getName())
                    i=i+1
                i=int(input("Choose which enemy to attack: "))
            
            if i<0 or i>len(enemylist):
                continue
            damage=hero.chooseAction()

            if damage!=None:
                enemylist[i-1].damageTaken(damage)

            
            if enemylist[i-1].getHealth() <= 0:
                self.displayStatsHero(hero)
                self.displayStatsEnemy(enemylist)
                print(self.getOkGreen()+
                    "\n"+enemylist[i-1].getName(), "has died siree", self.getEnd())
                enemylist.pop(i-1)
                if len(enemylist)==0:
                    # self.displayStats(hero, enemylist)
                    print(self.getOkGreen()+ self.getBold()+
                    "\nAll Enemy has died siree.\nYou have won this level\nMoving to next Level:)", self.getEnd())
                    break
            


            i=random.randrange(0,len(enemylist))
            damage = enemylist[i].generateDamage()
            hero.damageTaken(damage)
            print(self.getFail()+enemylist[i].getName(),"dealt", damage, "damage.",
                hero.getName(), "health is", hero.getHealth(),self.getEnd())

            if hero.getHealth() <= 0:
                self.displayStatsHero(hero)
                self.displayStatsEnemy(enemylist)
                print(self.getFail()+ self.getUnderline()+
                    "\n", hero.getName(), "has died siree!\nGame sopped"+ self.getEnd())
                break

            self.displayStatsHero(hero)
            self.displayStatsEnemy(enemylist)

    def pvpPlay(self,player1,player2):

        print(self.getWarning(), self.getHeader(),"Fight!", self.getEnd())

        while True:

            # print("============================================================================")
            
            print(self.getOkBlue()+player1.getName()+"  turn:",self.getEnd())
            damage=player1.chooseAction()

            if damage!=None:
                player2.damageTaken(damage)

            if player2.getHealth() <= 0:
                self.displayStatsHero(player1)
                self.displayStatsHero(player2)
                print(self.getFail()+ self.getUnderline()+
                    "\n", player2.getName(), "has died siree!\nGame sopped"+ self.getEnd())
                print(self.getOkGreen()+ self.getBold()+
                    "\n"+player1.getName()+"has won :)", self.getEnd())
                break

            print(self.getOkBlue()+player2.getName()+"  turn:",self.getEnd())
            damage=player2.chooseAction()

            if damage!=None:
                player1.damageTaken(damage)
            
            # print(self.getOkGreen()+player1.getName(),"dealt", damage, "damage.",
            #     player2.getName(), "health is", player2.getHealth(),self.getEnd())
            # print(self.getOkBlue()+player1.getName(),"dealt", damage, "damage.",
            #     player2.getName(), "health is", player2.getHealth(),self.getEnd())

            if player1.getHealth() <= 0:
                self.displayStatsHero(player1)
                self.displayStatsHero(player2)
                print(self.getFail()+ self.getUnderline()+
                    "\n", player1.getName(), "has died siree!\nGame sopped"+ self.getEnd())
                print(self.getOkGreen()+ self.getBold()+
                    "\n"+player2.getName()+"has won :)", self.getEnd())
                break

            self.displayStatsHero(player1)
            self.displayStatsHero(player2)
