import re


class Sac_a_dos :
    def __init__(self, N, W) :
        self.N = N
        self.W = W
        self.poids = [0]*N
        self.valeurs = [0]*N

    def valeur(self, s :set[int]) -> int : # La fonction avce le type de retour décl
        """
        Renvoie la valeur d'une solution
        :param s:
        :return:
        """
        pass

def lire_sad(nomFichier: str) -> Sac_a_dos :
        """
        Lit un fichier .txt du type :
        N W
        p1 v1
        p2 v2
        ...
        Retourne un objet Sac_a_dos rempli.
        """

        with open(nomFichier, 'r') as f:
          nbrs = re.findall(r'\d+', f.read()) #Séquence d'échappement non prise
          print(nbrs)

sac = lire_sad('sad_4.txt')
