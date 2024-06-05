lista=[2,3,4,5,6]
indice=int(input("Ingrese el indice que desa obtener por favor: "))

try:
    print(lista[indice])
except IndexError:
    print("Error, el indice que se ha ingresado no existe")