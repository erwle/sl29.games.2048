"""Module providing the logic of the 2048 game"""

import random
from typing import List, Tuple
import copy 

TAILLE:int = 4


# ==========================================================
# 🎯 FONCTION PUBLIQUE (API POUR L’INTERFACE)
# ==========================================================

def nouvelle_partie() -> Tuple[List[List[int]], int]:
    """
    Crée une nouvelle partie du jeu 2048.

    :return: Une grille TAILLExTAILLE initialisée avec deux tuiles, ainsi que le score à 0.
    :rtype: Tuple[List[List[int]], int]
    """

    grille = _creer_plateau_vide()
    _ajouter_tuile(grille)
    grille2 = _ajouter_tuile(grille) 
    grille3 = _ajouter_tuile(grille2)
    return(grille3,0)

def jouer_coup(plateau: List[List[int]], direction: str) -> tuple[List[List[int]], int, bool]:
    """
    Effectuer un mouvement sur le plateau.

    :param plateau: Une grille TAILLExTAILLE du jeu.
    :type plateau: List[List[int]]
    :param direction: La direction du déplacement : 'g' (gauche), 'd' (droite), 'h' (haut), 'b' (bas).
    :type direction: str
    :return: Retourne un tuple (nouveau_plateau, points, est_fini).
    :rtype: tuple[List[List[int]], int, bool]
    """

    raise NotImplementedError("Fonction jouer_coup non implémentée.")

# ==========================================================
# 🔒 FONCTIONS PRIVÉES (LOGIQUE INTERNE)
# ==========================================================

def _creer_plateau_vide() -> List[List[int]]:
    """
    Crée une grille TAILLExTAILLE remplie de zéros.
    :return: Une grille vide.
    :rtype: List[List[int]]
    """
    grille = []
    for _ in range(TAILLE):
        ligne = []
        for _ in range(TAILLE):
            ligne.append(0)
        grille.append(ligne)
    return grille

def _get_cases_vides(plateau: List[List[int]]) -> List[Tuple[int, int]]:
    """
    Retourne les coordonnées des cases vides sous forme d'une liste de coordonnées

    :param plateau: La grille actuelle.
    :type plateau: List[List[int]]
    :return: Une liste de coordonnées
    :rtype: List[Tuple[int, int]]
    """
    result = []
    for j in range(len(plateau)):
        for i in range(len(plateau[j])):
            valeur = plateau[j][i]
            if valeur == 0:
                result.append((j,i))
    return result


def _ajouter_tuile(plateau: List[List[int]]) -> List[List[int]]:
    """
    Ajoute une tuile de valeur 2 sur une case vide.

    :param plateau: La grille actuelle.
    :type plateau: List[List[int]]
    :return: Une nouvelle grille avec une tuile ajoutée.
    :rtype: List[List[int]]
    """
    plateau = copy.deepcopy(plateau)
    cv = _get_cases_vides(plateau)

    pos = random.randint(0,len(cv)-1)
    coord = cv[pos]
    ligne = coord[0]
    colonne = coord[1]
    plateau[ligne][colonne] = 2
    return plateau

def _supprimer_zeros(ligne: List[int]) -> List[int]:
    """
    Supprime les zéros d'une ligne.

    :param ligne: Une ligne de la grille.
    :type ligne: List[int]
    :return: La ligne sans zéros.
    :rtype: List[int]
    """
    result = []

    for element in ligne:
        if element !=0:
            result.append(element)
    return result

    raise NotImplementedError("Fonction _supprimer_zeros non implémentée.")

def _fusionner(ligne: List[int]) -> Tuple[List[int], int]:
    """
    Fusionne les valeurs identiques consécutives d'une ligne.

    :param ligne: Une ligne sans zéros.
    :type ligne: List[int]
    :return: La ligne après fusion, les points gagnés
    :rtype: Tuple[List[int], int]
    """
    
    fusion = []
    i = 0 
    points = 0
    while i < len(ligne):
        if (i+1 < len(ligne) and ligne[i] == ligne[i+1]) :
            points_gagnes = ligne[i] + ligne[i+1]
            points = points + points_gagnes 
            fusion.append(points_gagnes)
            i = i + 2 
        else:
            fusion.append(ligne[i])
            i = i +1

    return fusion, points

    raise NotImplementedError("Fonction _fusionner non implémentée.")

def _completer_zeros(ligne): # ajouter les annotations de type
    
    l = ligne
    l_c = l + (TAILLE - len(l))*[0]

    raise NotImplementedError("Fonction _completer_zeros non implémentée.")

def _deplacer_gauche(plateau): # ajouter les annotations de type
    nouveau_plateau = []
    nouveaux_points = 0
    pour chaque ligne du plateau:
        ligne_sans_zeros = _supprimer_zeros(plateau)
        ligne_fusionnee, points = _fusionner_ligne(ligne_sans_zeros)
        nouveaux_points = nouveaux_points + points
        ligne_finale = _completer_zeros(ligne_fusionnee)
        append(nouveau_plateau, ligne_finale)

    return  nouveau_plateau, nouveaux_points
    raise NotImplementedError("Fonction _deplacer_gauche non implémentée.")

def _inverser_lignes(plateau): # ajouter les annotations de type
    """
    DOCSTRING À ÉCRIRE
    """
    raise NotImplementedError("Fonction _inverser_lignes non implémentée.")

def _deplacer_droite(plateau: List[List[int]]) -> Tuple[List[List[int]], int]:
    """
    Déplace les tuiles vers la droite en fusionnant les valeurs identiques.

    :param plateau: La grille actuelle du jeu.
    :type plateau: List[List[int]]
    :return: Un tuple contenant la nouvelle grille après déplacement et les points gagnés.
    :rtype: Tuple[List[List[int]], int]
    """
    raise NotImplementedError("Fonction _deplacer_droite non implémentée.")

def _transposer(plateau): # ajouter les annotations de type
    """
    DOCSTRING À ÉCRIRE
    """
    raise NotImplementedError("Fonction _transposer non implémentée.")

def _deplacer_haut(plateau: List[List[int]]) -> Tuple[List[List[int]], int]:
    """
    Déplace les tuiles vers le haut en fusionnant les valeurs identiques.

    :param plateau: La grille actuelle du jeu.
    :return: Un tuple contenant la nouvelle grille après déplacement et les points gagnés.
    """
    raise NotImplementedError("Fonction _deplacer_haut non implémentée.")


def _deplacer_bas(plateau: List[List[int]]) -> Tuple[List[List[int]], int]:
    """
    Déplace les tuiles vers le bas en fusionnant les valeurs identiques.

    :param plateau: La grille actuelle du jeu.
    :return: Un tuple contenant la nouvelle grille après déplacement et les points gagnés.
    """
    raise NotImplementedError("Fonction _deplacer_bas non implémentée.")

def _partie_terminee(plateau: List[List[int]]) -> bool:
    """
    DOCSTRING À ÉCRIRE
    """
    # Partie non terminee si il y a des cases vides
    # Partie non terminee si il y a des fusions possibles (horizontale ou verticale)
    # Sinon c'est vrai

    raise NotImplementedError("Fonction _partie_terminee non implémentée.")