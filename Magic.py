
def inicio():
        print('¿Le gustaría saber qué pares de números enteros, cuando son multiplicados entre sí, dan como resultado un número que usted elija?')
        number=int(input('Si es así, por favor ingrese el número que desea investigar: '))
        busquedaDeFactores(number)
        busquedaMultiplicacion (number)

def busquedaDeFactores(n):
        cont = 1
        while cont != n:
                if n % cont == 0:
                        factores.append(cont)
                cont +=1

def busquedaMultiplicacion(n):
    for i in range(len(factores)):
        for j in range(len(factores)):
            if factores[i] * factores[j] == n:
                print(f'{factores[i]} * {factores[j]} = {n}')

factores=[]

inicio()