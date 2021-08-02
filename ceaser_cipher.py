#!/bin/python

from colorama import Fore,Back
import os

red = Fore.RED
green = Fore.GREEN 
reset = Fore.RESET + Back.RESET
Black = Fore.BLACK + Back.BLUE

print(Black + "Author : 106_Sam" + reset)

operation = lambda P,k: chr(((ord(P)-65+k)%26)+65

plaintext = input("Plain Text : \n")

key = input("Key : ")
print(key)
cipher = list(map(lamba x:operation(P,key),plaintext))
print(cipher)

