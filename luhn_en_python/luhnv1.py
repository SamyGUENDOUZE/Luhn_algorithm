################## ALGO ##################

# 1) On va créer un input qui va demander à l'utilisateur de rentrer un nombre à 16 chiffres
# 2) On va gérer les erreurs avec un try/except -> nb trop grand / nb trop petit / caractères spéciaux / lettres

class InvalidNumberOfDigitsError(Exception):
    def __init__(self, message="Le nombre n'a pas 16 chiffres"):
        self.message = message

def check_number_of_digits(card_number):
    try:
        card_number = card_number.replace(" ", "")
        number = int(card_number)
        if len(str(number)) != 16:
            raise InvalidNumberOfDigitsError()
        print("Le nombre a 16 chiffres")
    except ValueError:
        print("Le nombre contient des caractères spéciaux")
    except InvalidNumberOfDigitsError as e:
        print(e.message)
    except Exception as e:
        print("Entrer un nombre sans espaces entre les chiffres")

card_number = input("Entrez un nombre avec 16 chiffres: ")
check_number_of_digits(card_number)     
    


    


# 3) On va doubler la valeur d'un chiffre sur 2 de la droite vers la gauche, en commençant à partir de l'avant-dernier chiffre
# ex: 4624 7482 3324 9080  4624748233249080
'''
    8*2 = 16
    9*2 = 18
    2*2 = 4
    3*2 = 6
    8*2 = 16
    7*2 = 14
    2*2 = 4
    4*2 = 8

'''

inverted_list = list(card_number[::-1])
liste_index_pair = []
liste_index_impair = []

for i in range(16) : 
    #print(inverted_list[i])
    if i % 2 == 0 :
        liste_index_pair.append(inverted_list[i])
    else : 
        liste_index_impair.append(inverted_list[i])
    
#print(liste_index_impair)
#print(liste_index_pair)

sum_pair = 0
sum_impair = 0

for i in liste_index_impair : 
    i = int(i)
    i = 2*i
    # 4) Si dans l'étape précédente, on obtient des nombres à 2 chiffres, alors on additionne les 2 chiffres (ex : 16 = 1+6 = 7)
    if i > 9 : 
        i = str(i)
        i = int(i[0]) + int(i[1])
    sum_impair += i
    #print(i, sum_impair)
    
    
for j in liste_index_pair : 
    j = int(j)
    sum_pair += j
    #print(j, sum_pair)
    


# 5) Ensuite, on va additionner tous les chiffres du résultat de l'étape précédente aux chiffres restants du numéro de la carte de crédit.
# On obtient 2 sommes (celle des nombres doublés et celle des nombres non-doublés)
# 6) On va additionner les 2 nombres, si c'est un multiple de 10, alors le num à 16 chiffres est valide.

def isValid() : 
    final_number = sum_impair + sum_pair
    if final_number % 10 == 0 : 
        print('La carte est valide selon l\'algorithme de Luhn')
    else : 
        print('La carte n\'est pas valide selon l\'algorithme de Luhn')

isValid()