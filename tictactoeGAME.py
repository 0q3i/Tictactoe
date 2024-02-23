from turtle import *
from random import randint
import bot as foncB
import fonction as fonc
#PARAMETRE DE JEU
speed(10)
'''vitesse de jeu'''
run = True
'''varible de lancement
cette variable a une importence elle sera rapeler 
multipler fois'''
list_de_deja_utiliser = []
'''list des position deja jouer'''
dicPos = {'1':[-25, 25]
    ,'2':[25, 25]
    ,'3':[75, 25]
    ,'4':[-25, 75]
    ,'5':[25, 75]
    ,'6':[75, 75]
    ,'7':[-25, 125]
    ,'8':[25, 125]
    ,'9':[75, 125]
    }
'''dictionnaire de toute les postions posible'''

#Mis en place de l'environement 
#on affiche une grille
fonc.grille()

equipe = int(input('donner votre equipe 1 ou 2 :'))
while True:
  run = True
  color(0,0,0)
  input_du_joueurKEY = input("taper un chiffre entre 1 et 9 pour mettre une croix sur une casse :")
  while run == True:
    if dicPos[input_du_joueurKEY] not in list_de_deja_utiliser:
      fonc.play(input_du_joueurKEY,list_de_deja_utiliser,equipe,dicPos)
      run = False
    else:
      input_du_joueurKEY = input("Donne une nouvelle position: ")
  print('Au tour du robot:')
  run = True
  while run == True:
    foncB.robot(input_du_joueurKEY,list_de_deja_utiliser,equipe,dicPos)
    run = False
