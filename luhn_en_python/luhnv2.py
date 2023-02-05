while True : 
    
    # J'ai crée une classe qui permet de gérer si l'utilisateur se trompe au niveau de la longueur du nombre
    class InvalidNumberOfDigitsError(Exception):
        def __init__(self, message="Le nombre n'a pas 16 chiffres"):
            self.message = message

    def check_number_of_digits(card_number):
        try:    
            card_number = card_number.replace(" ", "") # sert à gérer les espaces
            number = int(card_number)
            if len(str(number)) != 16:
                raise InvalidNumberOfDigitsError()
            print("Le nombre a 16 chiffres")
            
            
            inverted_list = list(card_number[::-1]) #sert à inverser le nombre, ça sera plus facile pour la suite
            liste_index_pair = []
            liste_index_impair = []

            for i in range(16) :
                if i % 2 == 0 :
                    liste_index_pair.append(inverted_list[i])
                else : 
                    liste_index_impair.append(inverted_list[i])
                    
            sum_pair = 0
            sum_impair = 0

            for i in liste_index_impair : 
                i = int(i)
                i = 2*i
                if i > 9 : 
                    i = str(i)
                    i = int(i[0]) + int(i[1])
                sum_impair += i
                print(sum_impair)
                
                
            for j in liste_index_pair : 
                j = int(j)
                sum_pair += j
                
            def isValid() : 
                final_number = sum_impair + sum_pair
                if final_number % 10 == 0 : 
                    print('La carte est valide selon l\'algorithme de Luhn')
                else : 
                    print('La carte n\'est pas valide selon l\'algorithme de Luhn')

            isValid()
            
            
        except ValueError:
            print("Le nombre contient des caractères spéciaux")
        except InvalidNumberOfDigitsError as e:
            print(e.message)
        except Exception as e:
            print("Entrer un nombre sans espaces entre les chiffres")

    card_number = input("Entrez un nombre avec 16 chiffres: ")
    check_number_of_digits(card_number)