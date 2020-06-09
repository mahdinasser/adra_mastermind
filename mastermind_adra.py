from random import*
 
def mm(n,z):             # mm=mastermind z couleurs dans n cases
    s=[]
    i=0
    while i<n:
        s.append(randrange(1,z+1))
        i=i+1
    return s
 
 
def lister(s):             
#cette fonction transforme une chaine en une liste
#s est notre parametre

    liste=[]
    i=0
    while i<len(s): #len(s) longueur de la liste
        liste.append(int(s[i]))#ajoutera int(s[i])
        i=i+1
    return liste
 
     
def white(proposition,solution):   # indique le nombre de couleurs bien placé.
    bien=0  # nombre de white
    i=0
    while i < cases:
        if proposition[i]==solution[i]:
            bien=bien+1
            proposition[i]='#'   # pour éviter des compter plusieurs fois une meme couleur,
            solution[i]='*'      # on remplace ces chiffres par des lettres
        i=i+1
    return bien
 
 
def red(proposition,solution):  # indique le nombre de couleurs mal placé.
    i=0
    mal=0   # nombre de red
    while i<cases:
        j=0
        while j<cases:
            if proposition[i]==solution[j]:
                mal=mal+1
                proposition[i]='y'    # idem que pour la fonction "white"
                solution[j]='x'
            j=j+1
        i=i+1
    return mal
 
         
def copy(liste):           # copie "liste" dans "copy"
    copy=[]
    i=0
    while i<len(liste):
        copy.append(liste[i])
        i=i+1
    return copy

cases=4 #nombre des cases 
couleurs=6 #nombre de couleurs

Orange = 1
blue = 2
green = 3
yellow = 4
Violet = 5
brown = 6

max_essai=10

essai=0
field = mm(cases,couleurs)
good_num=0
wrong_num=0
copy_prop = []
copy_field = []
print("you can try ",max_essai,"times because ADRA is watching you ")
print()
while good_num<cases and essai<max_essai:
    essai=essai+1
    print("ADRA says: This is your ",essai,"chance")
    print()
    prop=lister(input('ADRA allows you to enter your proposition: '))
    copy_prop=copy(prop)
    copy_field=copy(field)
    good_num=white(copy_prop, copy_field)
    print(good_num,'white')
    print("good_answer")

    wrong_num=red(copy_prop, copy_field)
    print(wrong_num, 'red')
    print("sorry")
    print()
if good_num==cases:
    print("Congratulations !")

    print("Do you want to play again? yes ou no")
         
 # ADRA essaye de faire fonctionner cette partie pour qu'on pourra rejouer
 # si on le souhaite

       #rejouer = input() 
      #  if rejouer == 'no':
         # sys.exit()
       # if rejouer == 'yes':



else:
    print("the answer was",field)