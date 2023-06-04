# -*- coding: utf-8 -*-
import math as m

#ce programme calcul le ferraillage (armatures longitudinales et armatures 
# transversales d\'une poutre soumise a  un effort de traction
L=float(input("entrez la largeur de la section"))
b=float(input("entrez la hauteur de la section"))
Ng=float(input("entrez la valeur de l'effort normal Ng "))
Nq=float(input("entrez la valeur de l'effort normal Nq "))
Cmin=float(input("entrez l'enrobage min "))
Fck=int(input("entrez Fck"))

if Fck < 50:
    Fyk = int(input("entrez Fyk"))
    #On peut prendre un enrobage de 2.5 cm, qui est une valeur standard
    Nu = 1.35 * Ng + 1.5 * Nq
    Asmin = L * b * 0.3 * Fck ** (2 / 3) / Fyk
    Aslong = Nu / Fyk * 1.15
    s = max(Asmin, Aslong)
    if Aslong < Asmin :
        print("la section d armatures logitudinales a prendre en compte est", Asmin)
    else:
        print("la section d armatures longitudinales a prendre en compte est", Aslong) 

#%%  code Ismail
        
# on cherche une combinaison qui permet de s approcher le mieux de s

d = {}

for i in [6, 8, 10, 12, 14, 16, 20, 25, 32, 40]:
    for j in range(1, 10):
        d[(i, j)] = (m.pi*(i/2)**2)*j/100

list_keys = list(d.keys())

# Les combinaisons a 2

for i in range(len(list_keys)):
    for j in range(i):
        key1 = list_keys[i]
        key2 = list_keys[j]
        if 0 < key1[0]-key2[0] <= 4:
            d[key1+key2] = d[key1]+d[key2]

# Les combinaisons a 3
            
for i in range(len(list_keys)):
    for j in range(i):
        for k in range(j):
            key1 = list_keys[i]
            key2 = list_keys[j]
            key3 = list_keys[k]
            if 0 < key1[0]-key2[0] <= 2 and 0 < key2[0]-key3[0] <= 2:
                d[key1+key2+key3] = d[key1]+d[key2]+d[key3]

# Keep elements that are larger than s

#s = 14

new_d = {key: value for key,value in d.items() if value > s}


def keywithminval(d):
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(min(v))]
 

T = keywithminval(new_d)

def decoding(T, b):
    nb_max_lit = b * 10
    n = len(T)
    M = map(str,T)
    if n == 2:
        return '(HA {0}, {1})'.format(*M)
    elif n == 4:
        return '(HA {0}, {1}) puis (HA {2}, {3})'.format(*M)
    elif n == 6:
        return '(HA {0}, {1}) puis (HA {2}, {3}) puis (HA {4}, {5})'.format(*M)
        
        
print(decoding(T, b)) 






