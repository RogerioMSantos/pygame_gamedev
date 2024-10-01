from item import Item

class Moeda(Item):
    def __init__(self,screen,**kwargs):
        super().__init__(screen,name="moeda",color=(255,255,0),**kwargs)


    def collect(self,player):
        player.coin_collected += 1
