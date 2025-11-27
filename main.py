#### Fonctions secondaires

"""Module qui retourne les valeurs de la suite de syracuse pour une source n,
le temps de vol, l'altitude maximale et le temps de vol en altitude de cette suite"""

# imports
from plotly.graph_objects import Scatter, Figure

### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """Création du graphique
    
    Args :
        lsyr : le tableau contenant les valeurs de la suite de syracuse

    Returns : 
        None
    """
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = [ i for i in range(len(lsyr)) ]
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
    return None
#######################

def syracuse_l(n):
    """retourne la suite de Syracuse de source n

    Args:
        n (int): la source de la suite

    Returns:
        list: la suite de Syracuse de source n
    """

    # votre code ici
    l = [n]
    while n != 1 :
        if n % 2 == 0 :
            n = n/2
        else :
            n = n*3 + 1
        l.append(n)
    return l

def temps_de_vol(l):
    """Retourne le temps de vol d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol
    """

    # votre code ici

    for n in l :
        if n == 1 :
            return l.index(n)
    return None



def temps_de_vol_en_altitude(l):
    """Retourne le temps de vol en altitude d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: le temps de vol en altitude
    """

    # votre code ici

    for i in range (0,len(l) - 1) :
        if l[i+1] < l[0] :
            return i
    return None


def altitude_maximale(l):
    """retourne l'altitude maximale d'une suite de Syracuse

    Args:
        l (list): la suite de Syracuse

    Returns:
        int: l'altitude maximale
    """

    # votre code ici

    am = l[0]
    for n in l[1:len(l)] :
        am = max(am,n)
        #if n > am :
        #    am = n
    return am


#### Fonction principale


def main():
    """ Exécution des fonctions secondaires"""
    # vos appels à la fonction secondaire ici
    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))


if __name__ == "__main__":
    main()
