import time #Módulo para manejar el tiempo de salida en consola

def fibo_gen():
    n1 = 0
    n2 = 1
    counter = 0
    while True: #Ciclo infinito
        if counter == 0: #Primer número de la suceción
            counter += 1
            yield n1
        elif counter == 1: #Segundo número de la suceción
            counter += 1
            yield n2
        else: #Suma de números anteriores 
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            yield aux

if __name__ == "__main__":
    fibonacci = fibo_gen() #Instanciación usando variable fibonacci
    for element in fibonacci: #Recorre cada uno de los elementos
        print(element)
        time.sleep(1)
