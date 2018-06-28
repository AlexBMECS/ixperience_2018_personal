# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 23:38:13 2018

@author: alexrazer
"""

import sys
number_of_players = sys.argv[0]


class Player: 
    def __init__(self,name, hand):
        self.name = name
        self.hand = hand
        
class Hand: 
    def __init__(self,num = 5, cards):
        self.num = num
        self.cards = cards
        
class Card:
    def _init_(self, num, suit):
        self.num  = num;
        self.suit = suit;
        
        
counter = 0

while counter < 5:
 deck = []
    
 for n in range(1,5)
    deck.append(Card(1,"Spade")
    deck.append(Card(1,"Spade")
    deck.append(Card(1,"Spade")
    Card(1,"Heart"),Card(1,"Diamond"),Card(1,"Club"),
        Card(2,"Spade",Card(2,"Heart"),Card(2,"Diamond"),Card(2,"Club"),
        Card(3,"Spade",Card(1,"Heart"),Card(1,"Diamond"),Card(1,"Club"),
        Card(1,"Spade",Card(1,"Heart"),Card(1,"Diamond"),Card(1,"Club"),
             ]
       