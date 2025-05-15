import os
from cryptography.fernet import Fernet

life = 3
if life == 0:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("you loose, noob")
    breakpoint
print("i dont know what i was trying to do, just run the program")
print("the objective is put the correct password.")
type = input()
if type == "Rreal123":
    os.system('cls' if os.name == 'nt' else 'clear')
    print("congrats, im not impressed with that btw,")
    print("now i need you to uncover the next password.")
    print("")
    type1 = input()
    key = Fernet.generate_key
    if type1 == key:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("ye you are acctualy good on this, lets see if you can find the next flag")
        print("")
        type2 = input()
        key_u2 = Fernet.generate_key
        key1 = Fernet.encrypt(key_u2)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("wrong answer, try again.")
    if type2 == key1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("final boss, try to decrypt it,")
        print("")
        type3 = input()
        key_u3 = Fernet.generate_key
        key_u3_1 = Fernet.generate_key
        key_u3_2 = Fernet.encrypt(key)
        key2 = (key_u3 + key_u3_1 + key_u3_2 + key + key1 + key_u2)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("wrong answer, try again.")
    if type3 == key2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("H O W . . . ?")
        print("You won! Now go to therapy!")
        print("made by memz")
else:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("wrong answer, try again.")