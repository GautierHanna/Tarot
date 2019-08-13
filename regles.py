#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 17:29:36 2019

@author: gautierhanna
"""

from Creation import *

def priorite(Carte1,Carte2):
    Dict_couleur_carte = {Couleur(Carte1):Carte1, Couleur(Carte2): Carte2}
    
    if len(Dict_couleur_carte)==1:
        Dict_valeur_carte = {Valeur(Carte1):Carte1, Valeur(Carte2):Carte2}
        return Dict_valeur_carte[max(list(Dict_valeur_carte.keys()))]
    else : 
        
        if 'Atout' in list(Dict_couleur_carte.keys()) :
            return Dict_couleur_carte['Atout']
        else :
            return Carte1
        
    
def couleur_a_jouer(Jeu,Cartes_jouees = []):
    if len(Cartes_jouees) == 0 : 
        return 0
    Coul = Couleur(Cartes_jouees[0])
    
    Coul_jeu = ens_couleur(Jeu)
    
    if Coul in Coul_jeu:
        return Coul
    else : 
        if 'Atout' in Coul_jeu :
            return 'Atout'
        else :
            return 0

def Vainqueur(Cartes_jouees):
    Couleur = Cartes_jouees[0][1]
    Maitre = 0
    for i in range(len(Cartes_jouees)):
        if Couleur != 'Atout' :
            if Cartes_jouees[i][1] == 'Atout' and Cartes_jouees[i][0] != 'Excuse' :
                Maitre = i
                Couleur = 'Atout'
            elif Cartes_jouees[i][1] == Couleur :
                if Valeur(Cartes_jouees[i]) > Valeur(Cartes_jouees[Maitre]):
                    Maitre = i
        else :
            if Cartes_jouees[i][1] == 'Atout':
                if Valeur(Cartes_jouees[i])>Valeur(Cartes_jouees[Maitre]):
                    Maitre = i
    return Maitre

def liste_cartes_a_jouer(Jeu, Cartes_jouees = []) :
    Coul = couleur_a_jouer(Jeu, Cartes_jouees)
    if Coul == 0 :
        return Jeu
    else : return ens_carte_couleur(Jeu,Coul)
    
                
        
        


    
    