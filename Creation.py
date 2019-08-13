#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 09:55:29 2019

@author: gautierhanna
"""

#Importations Modules

import random as rd
import numpy as np
import itertools

#Programme

"""
Construction et distribution d'un jeu de tarot
"""

Couleurs = {'Carreau','Pique','Coeur','Trèfle'}


#Cartes spécifiques

Bouts = {(1,'Atout'),(21,'Atout'),('Excuse','Atout')}
Têtes = {'Valet': 1.5 ,'Cavalier' : 2.5 ,'Dame' : 3.5 ,'Roi' : 4.5}
TêtesJeu = set(itertools.product(Têtes.keys(),Couleurs))
Cartes_normales = set(itertools.product(range(1,11),Couleurs))
Atouts_normaux = set(itertools.product(range(2,21),{'Atout'}))
Jeu_normal = Cartes_normales.union(Atouts_normaux)

#Points

Dicovaleurs = {}
for carte in Bouts : 
    Dicovaleurs[carte] = 4.5
for carte in TêtesJeu : 
    Dicovaleurs[carte] = Têtes[carte[0]]
for carte in Jeu_normal :
    Dicovaleurs[carte] = 0.5
    
def nb_points(Jeu):
    score = 0
    for carte in Jeu :
        score += Dicovaleurs[carte]
    return score


def Couleur(Carte):
    return Carte[1]

def Valeur(Carte):
    v = Carte[0]
    if v == 'Excuse':
        return 0
    if v == 'Valet':
        return 11
    if v == 'Cavalier':
        return 12
    if v == 'Dame':
        return 13
    if v == 'Roi':
        return 14
    else : 
        return v

def Ens_bouts(Jeu):
    return Bouts.intersection(Jeu)
    
#Distribution
    
def distribution_aleatoire(nb_joueurs = 4):
    Jeu = list(Dicovaleurs.keys())
    if nb_joueurs == 4 :
        Chien = set()
        for i in range(6) :
            Chien.add(Jeu.pop(rd.randint(0,len(Jeu)-1)))
            
        Joueurs = [set(),set(),set(),set()]
        ind = len(Jeu)
        while ind > 0 :
            for joueur in Joueurs :
                joueur.add(Jeu.pop(rd.randint(0,len(Jeu)-1)))
            ind -= 4
        return Joueurs, Chien

def nb_points_liste(Joueurs):
    score = []
    for joueur in Joueurs :
        score.append(nb_points(joueur))
    return score

#Algorithmes de tri
    
def ens_carte_couleur(Jeu,Couleur): # A Modifier en Set
    Paquet = []
    for Carte in Jeu :
        
        if Carte[1]==Couleur:
            Paquet.append(Carte)
    return Paquet

def ens_couleur(Jeu):
    Ensemble = set()
    for carte in Jeu :
        Ensemble.add(carte[1])
    return Ensemble
#Contrats 
    
def nb_bouts(Jeu):
    return len(Ens_bouts(Jeu))

def Contrat(Jeu):
    Bts = nb_bouts(Jeu)
    if Bts == 0 :
        return 56
    elif Bts == 1 :
        return 52
    elif Bts == 2 :
        return 42
    else : 
        return 36
    
def Bool_Partie(Jeu):
    return Contrat(Jeu) <= nb_points(Jeu)
            
    
  
  