print("\n----------------------(Encoding & Decoding)-----------------------\n")

import random
import string


def encoding():
    st = input("Enter a message: ")
    words = st.split(" ")

    print("\n------------------------------------------------------------------")

    nwords = []
    all_characters = string.ascii_letters + string.digits + string.punctuation

    r1 = ''.join(random.choice(all_characters) for i in range(length))
    r2 = ''.join(random.choice(all_characters) for i in range(length))

    for word in words:
        if len(word) > 1:
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])

    print("Your message after encoding is: ", " ".join(nwords))

def decoding():
    st = input("Enter a message: ")
    words = st.split(" ")

    print("\n------------------------------------------------------------------")

    nwords = []
    for word in words:
        if len(word) > 1:
            stnew = word[length:-length]
            stnew = stnew[-1] + stnew[:-1] 
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])

    print("Your message after decoding is: "," ".join(nwords))    

def exit_():
    print("Thanks for using this system.\n\nThe coder of this system is '❤️ ❤️ ❤️  HACKSTAR ❤️ ❤️ ❤️ ' ")
    print("\n------------------------------------------------------------------\n")

    exit()


while True:
    print("\nEnter a number according to your choice:\n\n1. Encode\n2. Decode\n3. Exit\n")

    print("------------------------------------------------------------------")
    choice = int(input("Your choice is: "))

    print("------------------------------------------------------------------")
    if choice == 1 or choice == 2:
        length = int(input("Enter length you want to encode or decode: "))
        print("------------------------------------------------------------------")

    if choice == 1:
        encoding()
    elif choice == 2:
        decoding()
    elif choice == 3:
        exit_()
    else:
        print("\nInvalid choice. Please choose a valid option.")
        
    print("\n------------------------------------------------------------------\n")