import sys
import random         #importujemy biblioteke random #random.choice
import string         #importujemy string #string.ascil_lowercase

password = []
characters_left = -1

def update_characters_left (number_of_characters):    #zeby nie pisac tego samego wielokrotnie
#do funkcji przekazujemy ilosc znakow n-o-c           #aktulizujemy liczbe wolnych miejsc
    
    global characters_left   #pokazujemy ze chcemy uzywac zmienna globalna chracters_left     

    if  number_of_characters < 0 or number_of_characters > characters_left:  
        print("Liczba znaków spoza przedzialu 0, ",characters_left)
        sys.exit(0)                                
    else:                           
        characters_left -= number_of_characters
        print("Pozostało znaków:",characters_left)   #ile znakow jeszcze pozostalo
#number_of_characters - liczba znakow



password_length =int(input("Jak dlugie ma byc haso???"))      #pytamy uzytkownika jak dlugie ma byc haslo

if password_length <8:                            #dugosc hasla przez uzytkownika czy jest wieksze od 5
    #print("Hasło jest za krótkie") 
    print("Hasło musi miec minimum 5 znaków spróbuj jeszcze raz")
    sys.exit(0)                                       #do tego co na gorze import sys
else:
    characters_left = password_length                 #dostepne znaki = dlgosci znakow
#characters left - pozostale znaki
#password length - dlugosc hasla 


lowercase_letters = int(input( "Ile malych liter ma mieć hasło?" ) )          #male litery 
#if lowercase_letters <0 or lowercase_letters > characters_left:  #aktualizujemy zmienna characters_left
    #print("Liczba znaków spoza przedzialu 0, ",characters_left)
    #sys.exit(0)                               #zeby uzytkowni wiedzial ile tych znakow ma do despozycji 
#else:                            #kiedy liczba znakow jest okej
    #characters_left -= lowercase_letters        #rezygnujemy z tego na poczatku zrobilismy 
update_characters_left(lowercase_letters)

uppercase_letters = int(input( "Ile duzych liter ma mieć hasło?" ) )          #duze litery
#if uppercase_letters <0 or uppercase_letters > characters_left:  
    #print("Liczba duzych liter spoza przedzialu 0, ",characters_left)
    #sys.exit(0)
update_characters_left(uppercase_letters)   #dodajemy wywolanie do tej funkcji  napoczatku



special_characters = int(input( "Ile znaków specjalnych ma mieć hasło?" ) )   #znaki specjalne
update_characters_left(special_characters)


digits = int(input( "Ile cyfr ma mieć hasło?" ) )
update_characters_left(digits)

if characters_left > 0:
#jezeli jakies znaki zostana to uzupelniamy te znaki malymi literami
  print("Nie wszystkie znaki zostały wykorzystane.Hasło zostanie uzupelnine malymi literami ")
  lowercase_letters += characters_left

# print()
# print("Długosc hasla:",password_length)
# print("Małe litery",lowercase_letters)
# print("Duze litery",uppercase_letters)
# print("Znaki specjalne:",special_characters)
# print("Cyfry",digits)


# password = (password_length + lowercase_letters + uppercase_letters + special_characters + digits)
#kiedy nie korzystamy z jakiejs zmiennej w petli wpisujemy ( _ ) np zamiast (i)
for i in range(password_length): #for wykona sie tyle razy ile mamy znakow w hasle #mozemy wygenerowac haslo
#srawdzamy czy trzeba wygenerowac male literki duze cyfry znaki

    if lowercase_letters > 0:         #oznacza ze mamy jeszcze jakies male litery do wylosowania 
        password.append(random.choice(string.ascii_lowercase))  #albo ascil_lowercase
        lowercase_letters -= 1                      #poniejszamy liczb malych liter o 1
    
    if uppercase_letters > 0:
        password.append(random.choice(string.ascii_uppercase))
        uppercase_letters -= 1

    if special_characters > 0:
        password.append(random.choice(string.punctuation))   # albo punctuation znaki specjalne
        special_characters -= 1

    if digits > 0:
        password.append(random.choice(string.digits))
        digits -= 1

random.shuffle(password)             #zeby to co zostalo wygenerowane bylo pomieszane 
print("Twoje hasło to:", ''.join(password))

