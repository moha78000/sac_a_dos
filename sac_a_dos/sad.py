import re


class Sac_a_dos :
    def __init__(self, N, W) :
        self.N = N
        self.W = W
        self.poids = [0]*N
        self.valeurs = [0]*N

    def valeur_solution(self, s :set[int]) -> int : # La fonction avce le type de retour décl
        """
        Renvoie la valeur d'une solution
        :param s:
        :return:
        """
        total = 0
        for i in s:
            total += self.valeurs[i]
        return total

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
            nbrs = re.findall(r'\d+', f.read()) # Séquence d'échappement non prise
            N = int(nbrs[0])
            w = int(nbrs[1])
            sad = Sac_a_dos(N, w)
            index = 2
        
            for i in range(N):
        
                sad.valeurs[i] = int(nbrs[index])
                sad.poids[i] = int(nbrs[index+1])
                index += 2 

            return sad




def glouton(sad: Sac_a_dos) -> int:
    efficacite = [sad.valeurs[i] / sad.poids[i] for i in range(sad.N)] # Calcule l'efficacité pour chaque élément
    objets = list(range(sad.N)) # Définit la taille depuis le N
    print(objets)
    objets.sort(key = lambda i : efficacite[i] , reverse=True) # mets l'efficacité de chaque élément dans le tab objets mais en décroissant
    W = sad.W
    val = 0 
    for i in objets :  # Boucle pour mettre des élémens dans le sac à dos 
        if sad.poids[i]<= W:
            val +=sad.valeurs[i]
            W -= sad.poids[i]

    return val        

def solution_dynamique(s : Sac_a_dos) -> list[list[int]]:
    """Returns : 
        list[list[int]]: tableau 2D f[n][w]
    """
    
    f = [[0]*(s.W+1) for i in range(s.N+1)]

    for n in range(1, s.N+1) :
        for w in range(1, s.W+1):
            prendre = f[n-1][w-s.poids[n-1]] + s.valeurs[n-1] \
                if s.poids[n-1] <= w else 0
            pas_prendre = f[n-1][w]
            f[n][w] = max(prendre, pas_prendre)

    return f        
                             


sac = lire_sad("sad_4.txt")
result = glouton(sac)

solution_dynamique(sac)