import random

#symbols = ["+","-","/","*","!","&","$","#","?","@","a","b","c","d","e","f","g","h","i","j","k","l","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"]
symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

cantidad = int(input("Qué tan larga quieres tu contraseña?"))
password = ""

for i in range(cantidad):
    password += random.choice(symbols)

print("Esta es tu nueva contraseña :D", password)
