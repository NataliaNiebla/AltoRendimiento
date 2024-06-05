try:
    numero=int(input("Ingresa un número por favor: "))
except ValueError:
    print("La palabra que ingresaste no es valida")
else:
    print(f"El número es: {numero}")
finally:
    print("operación finalizada")

