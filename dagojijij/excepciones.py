def suma_numerica():
    while True:
        a=input("Número 1: ")
        b=input("Número 2: ")
        try:
            resultado= int(a)+int(b)
            break
        except:
            print("Ingresa un valor numerico por favor")
    return resultado

print(suma_numerica())