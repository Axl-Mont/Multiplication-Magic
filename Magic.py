
def inicio():
    print('¿Le gustaría saber qué pares de números enteros, cuando son multiplicados entre sí, dan como resultado un número que usted elija?')
    intentos = 0
    while intentos < 10:
        number = int(input('\nIngrese el número que desea investigar: '))
        if esPrimo(number):
            print( f'\nEl numero {number} es un numero primo, no posee esta caracteristica')
        elif number != 0 and number > 1:
            factores = busquedaDeFactores(number)
            busquedaDeMultiplicacion(number, factores)
        else:
            print('\n0 y 1 no son elegibles, intenta con otro numero')
        intentos +=1
        print(f'\nIntentos {intentos} de 10')


def busquedaDeFactores(n):
    cont = 1
    factores = []
    while cont != n:
        if n % cont == 0:
            factores.append(cont)
        cont += 1
    return factores


def busquedaDeMultiplicacion(n, f):
    print('\n Resultado: \n')
    for i in range(len(f)):
        for j in range(i, len(f)):
            if f[i] * f[j] == n:
                print(f'{f[i]} * {f[j]} = {n}')


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
