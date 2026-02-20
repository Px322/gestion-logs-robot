class Robot : 
    def __init__(self):
        self.batterie = 100
        self.position = [0,0]

    def droite(self):
        self.position[0]+=1
        self.diminuer_batterie()
    
    def gauche(self):
        self.position[0] -=1
        self.diminuer_batterie()

    def bas(self):
        self.position[1] -=1
        self.diminuer_batterie()

    def haut(self):
        self.position[1]+=1
        self.diminuer_batterie()

    def get_batterie(self):
        return self.batterie
    
    def diminuer_batterie(self):
        self.batterie -=5

    def get_position(self):
        return self.position


robot1 = Robot()
for i in range(6):
    robot1.droite()
print(robot1.get_batterie())
print(robot1.get_position())