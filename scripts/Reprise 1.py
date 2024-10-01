# 1. initialiser la liste
odds_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
print(list (enumerate(odds_list )))
# 2. récuperer la longueur de la liste odds
length_odds = len(odds_list)
print (f"la taille de la liste est {length_odds}")
#3. declare la nouvelle liste vide events
list1 = odds_list[0] + 1
list2 = odds_list[1] + 1
list3 = odds_list[2] + 1
list4 = odds_list[3] + 1
list5 = odds_list[4] + 1
list6 = odds_list[5] + 1
list7 = odds_list[6] + 1
list8 = odds_list[7] + 1
list9 = odds_list[8] + 1
list10 = odds_list[9] + 1
list11 = odds_list[5] + 1
new_odds_list = [list1,list2,list3,list4,list5, list6, list7, list8, list9,list10,list11]
print (f"new_odds_list :{new_odds_list}")
for indice, list in enumerate(odds_list) :
    odds_list.append(1)

#4. parcourir la liste odds avec arret à la fin de la liste



### recuperer la valeur de l'element de la list odds et le mettre dans une variable impair_value

### ajouter +1 à la valeur de la variable impair_value

### ajouter la valeur impair_value dans la nouvelle liste events

#5. afficher la liste events