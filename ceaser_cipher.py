from colorama import Fore

#color
red = Fore.RED
blue = Fore.BLUE
green = Fore.GREEN
black = Fore.BLACK
reset = Fore.RESET

print(red + "Author : 106_Sam" + reset)
key=13
yek=13-26
formula = lambda x,k : chr(((ord(x)-65+k)%26)+65)
print(black + "1. Encryption \n" +
      "2. Decryption\n" + reset)
choice = int(input("Choose (1-2) : "))

if choice == 1:
    plain = input(green + "Plain Text : " + reset)
    #key=13
    ciphertext = list(map(lambda x:formula(x,key),plain))
    print(ciphertext)


elif choice == 2:
    cipher = input(blue + "Cipher Text : " + reset)
    plaintext = list(map(lambda x:formula(x, yek),cipher))
    print(plaintext)

else:
    print("Something Went wrong")
