cont1=0
cont2=0
a=int(input("ingrese el numero"))
while cont1>-1 and cont1 < a:

    cont1+=1
    if a%cont1==0:
        cont2+=1
if cont2>2:
    print("el numero no es primo")
else:
    print("es primo")