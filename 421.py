from random import randint
from time import sleep

class Table:
    def __init__(self):
        self.pot=21
        self.joueur = [Joueur(),Joueur()]
        
    def est_vide_pot(self):
        return self.pot == 0
       
class Joueur:
    def __init__(self):
        self.jeton = 0
        self.lancer = []
        self.valeur = None
        
    def lancer_de(self):
        for _ in range(3):
            self.lancer.append(randint(1,6))
            
        v = self.lancer
        if 4 in v and 2 in v and 1 in v:
            self.valeur = 10
        elif v.count(1) == 3:
            self.valeur = 7
        elif (v.count(1) == 2 and v.count(6)==1) or v.count(6)==3:
            self.valeur = 6
        elif (v.count(1) == 2 and v.count(5)==1) or v.count(5)==3:
            self.valeur = 5
        elif (v.count(1) == 2 and v.count(4)==1) or v.count(4)==3:
            self.valeur = 4
        elif (v.count(1) == 2 and v.count(3)==1) or v.count(3)==3:
            self.valeur = 3
        elif (v.count(1) == 2 and v.count(2)==1) or v.count(2)==3:
            self.valeur = 2
        elif (1 in v and 2 in v and 3 in v) or (2 in v and 3 in v and 4 in v) or (3 in v and 4 in v and 5 in v) or (4 in v and 5 in v and 6 in v):
            self.valeur = 2
        elif v.count(2)==2 and v.count(1) == 1:
            self.valeur = -1
        else:
            self.valeur = 1
        
    def reset_lancer(self):
        self.lancer = []
        
def comp(j1,j2):
    res = 0
    if j1.valeur > j2.valeur:
        res = 1
    elif j1.valeur < j2.valeur:
        res = 2
    else:
        if sum(j1.lancer) > sum(j2.lancer):
            res = 1
        else:
            res = 2
    return res

def partie():
    t = Table()
    j1 = t.joueur[0]
    j2 = t.joueur[1]
    print('La partie commence khoya !')
    print('Manche charge')
    while not t.est_vide_pot():
        j1.lancer_de()
        j2.lancer_de()
        print('Le joueur 1 a fait',j1.lancer)
        sleep(0.5)
        print('Le joueur 2 a fait',j2.lancer)
        sleep(0.5)
        if comp(j1,j2) == 1:
            if t.pot >= j1.valeur:
                j2.jeton += j1.valeur
                t.pot -= j1.valeur
            else:
                j2.jeton += t.pot
                t.pot = 0
        if comp(j1,j2) == 2:
            if t.pot >= j2.valeur:
                j1.jeton += j2.valeur
                t.pot -= j2.valeur
            else:
                j1.jeton += t.pot
                t.pot = 0
        print("Le joueur 1 a", j1.jeton,"jetons")
        sleep(0.5)
        print("Le joueur 2 a", j2.jeton,"jetons")
        sleep(0.5)
        j1.reset_lancer()
        j2.reset_lancer()
    print('Manche décharge')
    while j1.jeton > 0 and j2.jeton > 0:
        j1.lancer_de()
        j2.lancer_de()
        print('Le joueur 1 a fait',j1.lancer)
        sleep(0.5)
        print('Le joueur 2 a fait',j2.lancer)
        sleep(0.5)
        if comp(j1,j2) == 1:
            if j1.jeton >= j1.valeur:
                j2.jeton += j1.valeur
                j1.jeton -= j1.valeur
            else:
                j2.jeton += j1.jeton
                j1.jeton = 0
        if comp(j1,j2) == 2:
            if j2.jeton >= j2.valeur:
                j1.jeton += j2.valeur
                j2.jeton -= j2.valeur
            else:
                j1.jeton += j2.jeton
                j2.jeton = 0
        print("Le joueur 1 a", j1.jeton,"jetons")
        sleep(0.5)
        print("Le joueur 2 a", j2.jeton,"jetons")
        sleep(0.5)
        j1.reset_lancer()
        j2.reset_lancer()
    if j1.jeton == 0:
        print('Le joueur 1 a gagné, BRAVO khoya')
    else:
        print('Le joueur 2 a gagné, BRAVO khoya')