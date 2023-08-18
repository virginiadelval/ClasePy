def redondear(data):
    if data >3.50:
        print(int(data)+1)
    else:
        print(int(data)-1)

data=float(input("Ingrese un valor =  "))
redondear(data)
