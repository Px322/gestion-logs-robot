from logger import Logger
import time

class Robot:
    def __init__(self):
        self.batterie = 100
        self.position = [0, 0]
        self.largeur = 20
        self.hauteur = 15
        self.obstacles = [[3, 0], [6, 4], [10, 5]]
        self.logger = Logger("logs/robots_logs.txt")

    def est_en_vie(self):
        return self.batterie > 0

    def droite(self):
        if not self.est_en_vie():
            self.logger.log("ERROR", "Batterie vide, robot arrêté !")
            return False
        prochaine_position = [self.position[0]+1, self.position[1]]
        if prochaine_position in self.obstacles:
            self.logger.log("WARNING", "Obstacle détecté, impossible d'avancer à droite")
            return False
        if self.position[0]+1 < self.largeur:
            self.position[0] += 1
            self.diminuer_batterie()
            self.logger.log("INFO", f"Robot avance à droite → {self.position}")
            self.get_batterie()
        else:
            self.logger.log("WARNING", "Bordure droite atteinte")
        time.sleep(2)

    def gauche(self):
        if not self.est_en_vie():
            self.logger.log("ERROR", "Batterie vide, robot arrêté !")
            return False
        prochaine_position = [self.position[0]-1, self.position[1]]
        if prochaine_position in self.obstacles:
            self.logger.log("WARNING", "Obstacle détecté, impossible d'avancer à gauche")
            return False
        if self.position[0]-1 >= 0:
            self.position[0] -= 1
            self.diminuer_batterie()
            self.logger.log("INFO", f"Robot avance à gauche → {self.position}")
            self.get_batterie()
        else:
            self.logger.log("WARNING", "Bordure gauche atteinte")
        time.sleep(2)

    def bas(self):
        if not self.est_en_vie():
            self.logger.log("ERROR", "Batterie vide, robot arrêté !")
            return False
        prochaine_position = [self.position[0], self.position[1]+1]
        if prochaine_position in self.obstacles:
            self.logger.log("WARNING", "Obstacle détecté, impossible de descendre")
            return False
        if self.position[1]+1 < self.hauteur:
            self.position[1] += 1
            self.diminuer_batterie()
            self.logger.log("INFO", f"Robot avance en bas → {self.position}")
            self.get_batterie()
        else:
            self.logger.log("WARNING", "Bordure basse atteinte")
        time.sleep(2)

    def haut(self):
        if not self.est_en_vie():
            self.logger.log("ERROR", "Batterie vide, robot arrêté !")
            return False
        prochaine_position = [self.position[0], self.position[1]-1]
        if prochaine_position in self.obstacles:
            self.logger.log("WARNING", "Obstacle détecté, impossible de monter")
            return False
        if self.position[1]-1 >= 0:
            self.position[1] -= 1
            self.diminuer_batterie()
            self.logger.log("INFO", f"Robot avance en haut → {self.position}")
            self.get_batterie()
        else:
            self.logger.log("WARNING", "Bordure haute atteinte")
        time.sleep(2)

    def get_batterie(self):
        if self.batterie == 0:
            self.logger.log("ERROR", "Plus de batterie !")
        elif self.batterie == 10:
            self.logger.log("WARNING", "Batterie à 10%")
        elif self.batterie == 20:
            self.logger.log("WARNING", "Batterie à 20%")
        elif self.batterie == 25:
            self.logger.log("WARNING", "Batterie à 25%")
        elif self.batterie == 50:
            self.logger.log("WARNING", "Batterie à 50%")

    def diminuer_batterie(self):
        self.batterie -= 5

    def get_position(self):
        self.logger.log("INFO", f"La position du robot est : {self.position}")