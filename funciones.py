import variables as va
import funciones as fu
import time

def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return 'no se puede dividir entre 0'
    return x / y

def exit():
    return 'agur bai!'

def calculadora():
    while True:

        print(va.msg2)
        opcion = int(input('opción: '))

        if opcion == 5:
            print(fu.exit())
            break
        
        num1 = int(input(va.val1))
        num2 = int(input(va.val2))

        if opcion == 1:
            resultado = fu.sumar(num1, num2)
            time.sleep(1)
            print(f'El resultado de tu suma es {resultado}')

        elif opcion == 2:
            resultado = fu.restar(num1, num2)
            time.sleep(1)
            print(f'El resultado de tu resta es {resultado}')

        elif opcion == 3:
            resultado = fu.multiplicar(num1, num2)
            time.sleep(1)
            print(f'El resultado de tu multiplicación es {resultado}')

        elif opcion == 4:
            resultado = fu.dividir(num1, num2)
            time.sleep(1)
            print(f'El resultado de tu división es {resultado}')

        else:
            print('Opción inválida')