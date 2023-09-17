from moves import *
from random import randrange
import pygame as pg
import time
from pathlib import Path
from copy import deepcopy

pg.init()
ecran = pg.display.set_mode((500,450))

poslink_ref = {'G': (50, 220),
               'O': (400, 220),
               'Y': (150, 320)}
               
poslink = [(150, 70), (200, 70), (150, 120), (200, 120),
           (50, 170), (100, 170), (100, 220),
           (150, 220), (150, 170), (200, 170), (200, 220),
           (250, 220), (250, 170), (300, 170), (300, 220),
           (350, 220), (350, 170), (400, 170),
           (150, 270), (200, 270), (200, 320)]


blocklink = {file.name[0]:file for file in Path("Sprites/").iterdir()}

def displayCube(pos) :
    """
    Affiche dans l'interface graphique pygame le cube dont la definitionstring
    est donnée par l'opérateur en argument.
    """
    ecran.fill((143, 134, 109))
    
    for color, coord in poslink_ref.items() :
        ecran.blit(pg.image.load(blocklink[color]), coord)
        
    for i in range(21) :
        ecran.blit(pg.image.load(blocklink[pos[i]]), poslink[i])
            
    pg.display.flip()

def get_nearby(pos) :
    return [F(pos), Fpm(pos), F2(pos),
            R(pos), Rpm(pos), R2(pos),
            U(pos), Upm(pos), U2(pos)]

displayCube(e)

def BFS() :
    """
    Recherche en profondeur exécutée au démarrage pour indexer les cubes en fonction de leur profondeur.
    Elle retourne une liste de sets, dont l'index correspond à la profondeur de chaque cube que contient le
    set correspondant. On utilise la structure des sets pour profiter du hashing de donné, qui offre une performance
    à complexité optimale lors de l'exploration des positions visitées.
    
    G[0] correspond donc à {e} (la definitionstring du cube résolu)
    G[1] au set des 9 cubes adjacents par 1 mouvement au cube résolu.
    """
    init = time.time() ; t = None
    G = [{e}, set(get_nearby(e))] #où get_nearby(c) permet d'obtenir la liste des cubes adjacents à c
    
    while G[-1]: #Tant que G[n] n'est pas vide (condition d'arrêt)
        G.append(set())
        for i in G[-2] : #Pour chaque c dans G[n]
            for adj in get_nearby(i) : #On étudie les cubes adjacents
                if not (adj in G[-1] or adj in G[-2] or adj in G[-3]) : #Si ce cube n'a jamais été visité.
                    G[-1].add(adj) #On l'ajoute dans G[n+1]
        
        t = (time.time(), time.time()-t[0]) if t else (time.time(), time.time()-init)
        print(f"Finished depth {len(G)-1}. {len(G[-1])} cubes found in {round(t[1],2)} seconds.")
    print(f"Finished exploring configurations in {round(time.time()-init,2)} seconds. \n\nProblem is depth {len(G)-2}")
    return G

G = BFS()

str_to_move = {"U" : U, "F" : F, "R" : R,
               "U'" : Upm, "F'" : Fpm, "R'" : Rpm,
               "U2": U2, "F2" : F2, "R2": R2}

move_to_str = {i:j for j,i in str_to_move.items()}


def p(pos, ref=None) :
    """
    Fonction opérationnelle une fois la recherche en profondeur terminée.
    Après cette dernière, les cubes sont indexés dans la liste "depth" en fonction
    de leur profondeur (le nombre de mouvements nécessaires pour les résoudres)
    Cette fonction search retourne la profondeur d'un cube donné, où pos reçoit
    la definitionstring du cube dont on souhaite la profondeur.
    La variable ref permet de fournir la profondeur du cube actuel. On n'explorera ainsi
    que les "profondeurs adjacentes", ce qui réduit le temps d'execution
    """
    if ref : # Exploitation de la profondeur de référence si elle est fournie.
        for i in range(ref-1, ref+2) :
            if i in range(len(G)) and pos in G[i] :
                return i
    for i in range(len(G)) : #On explore chaque profondeur
        if pos in G[i] :
            return i
    return "Illegal position"

def solve(pos, n=None, sq="", init=None) :
    """
    Prend en argument la definitionstring du cube à résoudre, et retourne la séquence de mouvements
    à exécuter pour le résoudre, après avoir affiché la résolution dans l'interface graphique pygame.
    """
    if pos==e :
        sequence(init,sq)
        return sq
    if not n :
        init = pos
        n = p(pos)
    assert p(pos)==n
    options = [(mv, new_pos) for mv, new_pos in [(x, x(pos)) for x in move_to_str] if p(new_pos, ref=n)<n]
    for move, new_pos in options :
        result = solve(new_pos, n-1, sq+move_to_str[move], init)
        if result :
            return result
    return None

def sequence(init, seq, visu=True) :
    """
    Où : - init est la definitionstring du cube initial
         - seq la chaine de caractère contenant la séquence de mouvements à exécuter
    Cette fonction exécute dans l'interface graphique pygale les mouvements contenus dans seq
    et retourne la definitionstring du cube résolu.
    Remarque : il est possible de désactiver la visualisaion des mouvements en ajoutant visu=False
    en argument.
    """
    seq = seq.replace(" ","")
    if visu :
        displayCube(init)
    time.sleep(0.5)
    new = init
    while seq!="" :
        if seq[:2] in str_to_move :
            current, seq = seq[:2], seq[2:]
        elif seq[0] in str_to_move :
            current, seq = seq[0], seq[1:]
        else :
            print("Illegal Move !")
            break
        new = str_to_move[current](new) #Executer le mouvement
        if visu :
            displayCube(new)
        time.sleep(0.2)
    return new
    
def non_repet(move="#") : #move est de type str
    """
    Retourne la liste des mouvements non-redondants avec le précédent.
    (Inutilisée pour l'instant)
    """
    return [mv for mv in str_to_move if move[0] not in mv]


def scramble(depth=14) :
    """
    Génère une séquence aléatoire de mouvements et retourne la definitionstring du cube ainsi mélangé.
    """
    l = [[i for i in str_to_move][randrange(9)]]
    for i in range(depth-1) :
        l.append(non_repet(l[i])[randrange(6)])
    seq = "".join(l)
    print(seq)
    return sequence(e, seq)