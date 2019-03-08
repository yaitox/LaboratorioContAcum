
contCero=0
a=int(input("ingrese un numero"))
for i in range(1,a):
    residuo=a%i
    if residuo==0:
        contCero=contCero+1

        if (contCero == 2):
            print("no es primo")
            break


    else:
        if(contCero==1):
                print("es primo")
                break






