
from random import randint
import random
##Ülesanne 0
#x=0
#while x<40:

#    if x%2==0:

#        print(x, end=" ")

#    x+=1
#print()
#x=0
#while True:
#    if x%2==0: 
#        print(x, end=" ")
#    x+=1
#    if x==40: break

#print()

#for x in range (0,40,1):
#    if x%2==0: print(x, end=" ")

#print()
# #Ülesanne 3
#try:
#    f = int(input("mitu algarvu sa tahad? "))
#    for d in range (0,f,1):
#        print("täienduskoolitus")
#        a = randint(1,50)
#        b = randint(1,50)
#        c = a + b
#        for i in range (0,5,1):
#            answer = int(input(f"{a}+{b}=? "))
#            if answer == a+b:
#                print("see on õige")
#                break
#            else:
#                print("Proovi veel korra")
#                print()
#        print(f"õige on {c} ")
#except:
#    print("see ei ole õige")

#g = 0
#try:
#    f = int(input("mitu algarvu sa tahad? "))
#    while g < f :
#        g = g +1
#        print("täienduskoolitus")
#        a = randint(1,50)
#        b = randint(1,50)
#        c = a + b
#        for i in range (0,5,1):
#            answer = int(input(f"{a}+{b}=? "))
#            if answer == a+b:
#                print("see on õige")
#                break
                
#            else:
#                print("Proovi veel korra")
#                print()
#        print(f"õige on {c} ")
#except:
#    print("see ei ole õige")



##Ülesanne 10
#x=1
#while True:
#    if x> 100:
#        break
#    elif x%5==0:
#        print(x, end =" ")
#    x+=1
#print()
#for x in range(1,101,1):
#    if x%5==0:
#        print(x, end=" ")

# See on Aleksandri ülesanne
#a=random.randint(1, 100)
#b=0
#while b !=a:
#    try:
#        b=int(input("sisesta mõidtatuse numer 1-100 "))
#        if b > 100:
#            print("Value error")
#        if b < 1:
#            print("Value error")
#        elif b < a :
#            print("Liiga väike,Proovi uuesti.")
#        elif a < b:
#            print("Liiga suur,Proovi uuesti.")
#        else:
#            print("See on õige!!!!!!!1")
#    except:
#        print("Value error")

#Ülesanne 17 
try:
    num_horiz=int(input("Siseta ruutude arv horisantalset =>> \n"))
except:
    print ("vALUE ERROR!")
try:
    num_vert=int(input("Siseta ruutude arv vertikalset =>> \n"))
except:
    print ("vALUE ERROR!")
for y in range (num_vert):
    for x in range (num_horiz):
        print("m2" , end=" ")
    print()
