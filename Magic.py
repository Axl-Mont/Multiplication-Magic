factores=[]

def inicio():
        print('¿Le gustaría saber qué pares de números enteros, cuando son multiplicados entre sí, dan como resultado un número que usted elija?')
        number=int(input('Si es así, por favor ingrese el número que desea investigar: '))
        if esPrimo(number):
                print (f'El numero {number} es un numero primo, no posee esta caracteristica')
        elif number != 0 and number > 1:
                busquedaDeFactores(number)
                busquedaDeMultiplicacion (number)
        else:
                print('0 y 1 no son elegibles, intenta con otro numero')

def busquedaDeFactores(n):
        cont = 1
        while cont != n:
                if n % cont == 0:
                        factores.append(cont)
                cont +=1

def busquedaDeMultiplicacion(n):
    for i in range(len(factores)):
        for j in range(len(factores)):
            if factores[i] * factores[j] == n:
                print(f'{factores[i]} * {factores[j]} = {n}')

def esPrimo(n):
        if n == 2:
                return True
        elif n % 2 == 0:
                return False
        for i in range(3, int(n**0.5)+1, 2):
                if n % i == 0:
                        return False
        return True


inicio()
input()