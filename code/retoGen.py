from time import sleep #Módulo para manejar el tiempo de salida en consola

max = int(input("¿Hasta que número de la secuencia de Fibonacci?: "))

def fibo_gen():
    a, b = 0, 1 #Los dos primeros valores de la suceción
    while True: #Ciclo infinito
        yield a
        a, b = b, a + b #Swap con la suma de los números anteriores

for n in fibo_gen():
    if n > max:
        break
    print(n)
    sleep(0.5)
