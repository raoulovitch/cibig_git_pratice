#Calcul de la moyenne
#Recuperer les valeurs des 3 note
grade1 = input("Enter first grade: ")
grade2 = input("Enter second grade: ")
grade3 = input("Enter third grade: ")
# Faire la somme des note et lui assigner somme.

somme = float (grade1) + float(grade2) + float(grade3)

print ("la somme est : ", somme)

# Diviser la somme des note par 3
moy = (somme / 3)

# Affiche le resultats
print(f"la moyenne est : {moy: .2f}")





#si la moyenne est inférieure à 10 affiche échoué
if moy < 10 :
    message = "échoué"


#si la moyenne est supérieure ou égale à 10 et inferieur a 12 affiche passable

elif  (moy >= 10 and moy < 12) :
    message = "passable"

#si la moyenne est supérieure ou égale à 12 et inferieur 14 affiche assez bon
elif moy >= 12 and moy < 14:
      message = "assez bon"

#si la moyenne est supérieure ou égale à 14 et inferieur 16 affiche  bon
elif moy >= 14 and moy < 16:
      message = "bon"

#Si la moyenne est supérieure ou égale à 16 affiche très bon
elif moy >= 16 and moy <= 20 :
      message = "très bon"
## pour toute note pas prise en compte dans les autres condition
else :
    message = "retry"

print(message)
