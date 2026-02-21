from robot import Robot


# Objet robot1
robot1 = Robot()

# Actions aléatoires robots 
for i in range(10):
    robot1.droite
    robot1.bas
    
robot1.haut

robot1.get_position() # permet d'obtenir la position finale du robot

# Gestion des logs

robot1.logger.supprimer(None,"INFO") # supprime les logs comportant le mot INFO
robot1.logger.supprimer("15",None) # supprime les 15 premières logs
robot1.logger.vider() # supprime l'entièreté des logs

