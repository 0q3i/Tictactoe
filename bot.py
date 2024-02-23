import fonction as fonc
from random import randint 

def robot(elemDeJeu,listDeJeu,equipe,dicDeJeu):
    '''renvois l'attaque du bot'''
    elemDeJeu = str(randint(1,len(dicDeJeu)))
    if dicDeJeu[elemDeJeu] in listDeJeu:
      elemDeJeu = str(randint(1,len(dicDeJeu)))
    if dicDeJeu[elemDeJeu] not in listDeJeu:
      fonc.playBot(elemDeJeu,listDeJeu,equipe,dicDeJeu)
    return None 
