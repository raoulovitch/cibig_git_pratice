# list de des animaux

## Afficher le contenu d'une liste en utilisant while
# Creer la liste et on assigne des valeurs
animal_list = ['cow', 'mouse', 'yeast', 'bacteria']
#Parcourir la liste avec while
# Condition arret : le nombre d'element de liste
len(animal_list)

#stocker le nombre d'element liste dans une variable
nb_liste = len(animal_list)

#print(nb_liste)

# La condition d'arret est 4
#Ecrire la boucle while avec le sconditions

# tant que i soit plus petit ou egal à taille de la liste
# si je dois parcourir toutes la liste alors je mettre i=0 le i = + 1 (permet de conditionner l'arret par saux de 1) et : sont tres important
i=0
while i <= nb_liste :
    print(i)
    i = i + 2


#affiche tous les éléments de la liste des animaux en utilisant une boucle for boucle
animal_list = ['cow', 'mouse', 'yeast', 'bacteria']
for animal in animal_list:
    print(animal)