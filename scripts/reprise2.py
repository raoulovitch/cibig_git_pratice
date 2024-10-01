
sequence = "TCTGTTAACCATCCACTTCG"
# Donner l'inverse avec le code [::-1]et assigne une variable
sequence_inversed = sequence [::-1]
#pour mettre tous sequence en majiscule DNA_upper : DNA.upper()
print(sequence_inversed)


for i in sequence_inversed :
    if (i== "A"):print ("T", end= "")
    elif (i== "T"):print ("A", end= "")
    elif (i== "C"):print("G", end= "")
    elif (i== "G"):print("C", end= "")
else :
    i : ""

