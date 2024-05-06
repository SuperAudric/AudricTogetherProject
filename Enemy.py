import MapEntity

class Enemy(MapEntity.MapEntity):
    HP = 100

    def __init__(self, enemyID):
        super().__init__("Greater Bean")
        self.HP = 100*enemyID
    

