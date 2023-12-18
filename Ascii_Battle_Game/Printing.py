from Colours import Colour


class Printing(Colour):
    def printBar(self,value):
        for i in range(1,100,4):
            if i<=value:
                print("█",end='')
            else:
                print(" ",end="")

    def displayStatsHero(self,hero):
        print("----------------------------------------------------------------------------")
        print(self.getOkGreen()+ hero.getName())
        print("HP: ",end='')
        self.printBar(hero.getHealth())
        print("  ",hero.getHealth(),self.getEnd())
        
        if hero.getMagicPower()>0:
            print(self.getOkBlue()+"MP: ",end='')
            self.printBar(hero.getMagicPower())
            print("  ",hero.getMagicPower())
            print("\n",self.getEnd())
        
        print("----------------------------------------------------------------------------")

    
    def displayStatsEnemy(self,enemy):
        print("----------------------------------------------------------------------------")
        # print(type(enemy))
        for i in enemy:
            # print(i)
            print(self.getFail()+i.getName())
            print("Hp: ",end='')
            self.printBar(i.getHealth())
            print("  ",i.getHealth(),self.ENDC)
        print("----------------------------------------------------------------------------")


    def startImage(self):
        print(self.getBold()+self.getHeader())
        print("                                      . ")
        print("                                   .+=. ")
        print("       :--===-:                  :+*.   ")
        print("     ==:  ..:=*+               -++:     ")
        print("    :+...  .:-+++            -+*-       ")
        print("    =+:....:-==+*       :*==+++         ")
        print("    .*=:--=++=++=      ==#***:          ")
        print("      =*==+++**+   .:-=:+*#*+:          ")
        print("      . =+:-=*+=----.:=#*=-             ")
        print("      .=:   .:-==+++==:                 ")
        print("     --:=-..-=+-                        ")
        print("   .-.-*-=. -+=                         ")
        print("   - :*-:: :-+:                         ")
        print("   - -# =.  -+-                         ")
        print("  :: -*.=  .:=+                         ")
        print("  -==*+-- +*.=*                         ")
        print("       -. +%.-*.                        ")
        print("       = .=%::+=                        ")
        print("       = :+%:.-+                        ")
        print("      -..-**::=+:                       ")
        print("      + .-*+:.-++                       ")
        print("     -=..=*+-.:++:                      ")
        print("     +..:=+*-.:==*                      ")
        print("     *===+*++==+++                      ")
        print("       . ... .                          ")
        print(self.getEnd())