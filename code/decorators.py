from datetime import datetime #Módulo para medir tiempo de una ejecución

def execution_time(func):
    def wrapper(*args, **kwargs): #wrapper calcula el tiempo de operación
        #No importa la cantidad de argumentos posicionales (*args) y
        #la cantidad de argumentos nombrados (**Kwargs) la función lo leerá
        inicial_time = datetime.now() #Tiempo exacto ahora
        func(*args, **kwargs) #ejecutar la función
        final_time = datetime.now() #Tiempo final
        time_elapsed = final_time - inicial_time #Obtener la cantidad de segundos
        print("Pasaron " + str(time_elapsed.total_seconds()) + " segundos")
    return wrapper #Closure donde la nested function debe retornar

@execution_time #Decorador
def random_func():
    for _ in range(1, 100000000): #Cuando no se requiere tener el valor de cada  vuelta se coloca "_"
        pass

@execution_time
def suma(a: int, b: int) -> int:
    return a + b

@execution_time
def saludo(nombre = "Andrés"):
    print("Hola " + nombre)


random_func()
suma(5, 5)
saludo("Camilo")





