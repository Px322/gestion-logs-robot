from datetime import datetime

class Logger:
    def __init__(self, fichier):
        self.fichier = fichier

    def log(self, niveau, message):
        date = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        ligne = f"{date} {niveau} - {message}\n"
        
        with open (self.fichier, "a",encoding="utf-8") as f:
            f.write(ligne)
        
        print(ligne)

    def supprimer(self, nombre=None, mot=None):
        with open(self.fichier, "r", encoding="utf-8") as f:
            lignes = f.readlines()

        if nombre is not None:
            lignes = lignes[nombre:]  # supprime les X premières lignes par sl
            print(f"{nombre} lignes ont été supprimés !")

        if mot is not None:
            lignes = [l for l in lignes if mot not in l]  # supprime les lignes avec le mot
            print(f"Les lignes contenant le mot {mot} ont été supprimés !")

        with open(self.fichier, "w", encoding="utf-8") as f:
            f.writelines(lignes)

    def vider(self):
        with open(self.fichier, "w", encoding="utf-8") as f:
            f.write("")
        print("Logs supprimés !")

        
            