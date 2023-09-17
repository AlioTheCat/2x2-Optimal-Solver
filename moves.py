"""
Solved cube's definition string :
'WWWWGGGRRRRBBBBOOOYYY'

Pour le rubik's cube 2x2, on a un grand nombre de simplifications.
Au lieu de considérer les moves UD LR FB, on peut se réduire
à la moitié car à symétrie près ces moves sont identiques.
"""

e = 'WWWWGGGRRRRBBBBOOOYYY'

def F(pos) :
    """Il suffit de réindexer chaque caractère de
       def(c) suivant la permutation correspondante"""
    return (pos[0] + pos[1] + pos[6] + pos[5] +
            pos[4] + pos[18] + pos[19] +
            pos[10] + pos[7] + pos[8] + pos[9] +
            pos[3] + pos[2] + pos[13] + pos[14] +
            pos[15] + pos[16] + pos[17] +
            pos[11] + pos[12] + pos[20])

def Fpm(pos) :
    return (pos[0] + pos[1] + pos[12] + pos[11] +
            pos[4] + pos[3] + pos[2] +
            pos[8] + pos[9] + pos[10] + pos[7] +
            pos[18] + pos[19] + pos[13] + pos[14] +
            pos[15] + pos[16] + pos[17] +
            pos[5] + pos[6] + pos[20])

def F2(pos) :
    return (pos[0] + pos[1] + pos[19] + pos[18] +
            pos[4] + pos[11] + pos[12] +
            pos[9] + pos[10] + pos[7] + pos[8] +
            pos[5] + pos[6] + pos[13] + pos[14] +
            pos[15] + pos[16] + pos[17] +
            pos[3] + pos[2] + pos[20])

def U(pos) :
    return (pos[2] + pos[0] + pos[3] + pos[1] +
            pos[8] + pos[9] + pos[6] +
            pos[7] + pos[12] + pos[13] + pos[10] +
            pos[11] + pos[16] + pos[17] + pos[14] +
            pos[15] + pos[4] + pos[5] +
            pos[18] + pos[19] + pos[20])

def Upm(pos) :
    return (pos[1] + pos[3] + pos[0] + pos[2] +
            pos[16] + pos[17] + pos[6] +
            pos[7] + pos[4] + pos[5] + pos[10] +
            pos[11] + pos[8] + pos[9] + pos[14] +
            pos[15] + pos[12] + pos[13] +
            pos[18] + pos[19] + pos[20])

def U2(pos) :
    return (pos[3] + pos[2] + pos[1] + pos[0] +
            pos[12] + pos[13] + pos[6] +
            pos[7] + pos[16] + pos[17] + pos[10] +
            pos[11] + pos[4] + pos[5] + pos[14] +
            pos[15] + pos[8] + pos[9] +
            pos[18] + pos[19] + pos[20])

def R(pos) :
    return (pos[0] + pos[9] + pos[2] + pos[10] +
            pos[4] + pos[5] + pos[6] +
            pos[7] + pos[8] + pos[19] + pos[20] +
            pos[14] + pos[11] + pos[12] + pos[13] +
            pos[1] + pos[3] + pos[17] +
            pos[18] + pos[15] + pos[16])

def Rpm(pos) :
    return (pos[0] + pos[15] + pos[2] + pos[16] +
            pos[4] + pos[5] + pos[6] +
            pos[7] + pos[8] + pos[1] + pos[3] +
            pos[12] + pos[13] + pos[14] + pos[11] +
            pos[19] + pos[20] + pos[17] +
            pos[18] + pos[9] + pos[10])

def R2(pos) :
    return (pos[0] + pos[19] + pos[2] + pos[20] +
            pos[4] + pos[5] + pos[6] +
            pos[7] + pos[8] + pos[15] + pos[16] +
            pos[13] + pos[14] + pos[11] + pos[12] +
            pos[9] + pos[10] + pos[17] +
            pos[18] + pos[1] + pos[3])