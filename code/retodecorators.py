from datetime import datetime #Módulo para medir tiempo de una ejecución

def execution_time(func):
    def wrapper(*args, **kwargs): #wrapper calcula el tiempo de operación
        inicial_time = datetime.now() #Tiempo exacto ahora
        func(*args, **kwargs) #ejecutar la función
        final_time = datetime.now() #Tiempo final
        time_elapsed = final_time - inicial_time #Obtener la cantidad de segundos
        print("La función tardó " + str(time_elapsed.total_seconds()) + " segundos")
    return wrapper #Closure donde la nested function debe retornar

@execution_time
def exponent(x: int, n: int) -> int:
    print(x ** n)

exponent(10, 5)

