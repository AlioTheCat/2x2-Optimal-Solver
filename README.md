# 2x2-Optimal-Solver
This program uses BFS to build a "best path" heuristic. The BFS search lasts around 2 minutes. Then any 2x2 is solvable optimally and instantly.

################################################################################################################################################

Français :

Le projet est divisé en 2 fichiers python.
"moves.py" répertorie l'ensemble des mouvements applicables à un cube.
"solver.py" rassemble les méthodes utilisées pour parcourir le graphe des positions,
ainsi que résoudre un cube à partir d'une heuristique.

********************************************************************************************

Dans l'ensemble du programme, pour modéliser un cube, on utilise sa 'definitionstring'. Elle correspond aux couleurs des stickers
présentes sur le cube, indexées suivant le schéma consultable dans le fichier 'Patron-Memo.png'.

Les couleurs sont notées : 'W' pour white, 'G' pour green, 'R' pour red, 'B' pour blue, 'O' pour orange, 'Y' pour yellow.

Par exemple, le cube résolu a pour definitionstring 'WWWWGGGRRRRBBBBOOOYYY'

********************************************************************************************

Le coin Jaune-Orange-Vert est immobile; il sert de référence et permet ainsi :
* de fixer l'orientation du cube et appliquer ainsi au problème toutes les réductions par symétrie possibles.
* de diviser par 2 le nombre de mouvements appliquables à un cube donné, bien évidemment SPDG puisque l'ensemble
      des mouvements restants permet toujours de parcourir toutes les configurations existantes.


********************************************************************************************

Les mouvements restants sont notés conformément aux conventions internationales :
F comme front, pour la face frontale | U comme up, pour la face du haut | R comme right, pour la face de droite
Par défaut, une face est tournée dans le sens horaire. Si la notation s'accompagne d'une apostrophe (dite 'prim')
on effectue le mouvement dans le sens trigo. Si accompagnée d'un 2, on tourne la face de 180°. Evidemment, dans
ce cas précis, le sens de rotation de la face n'a aucune importance.

Exemples de notation :
U -> on tourne la face du haut dans le sens horaire
F' -> on tourne la face frontale dans le sens trigo
R2 -> on tourne la face de droite deux fois

********************************************************************************************
