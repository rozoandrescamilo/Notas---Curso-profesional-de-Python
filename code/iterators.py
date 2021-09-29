import time #Módulo para manejar el tiempo de salida en consola

class FiboIter(): #Se crea una nueva clase  para el iterador

    def __iter__(self): #Con el primer método se inicializan las variables
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self): #Método para que funcione la sucesión
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else: #Suma de los dos anteriores
            self.aux = self.n1 + self.n2
            self.n1, self.n2 = self.n2, self.aux #Swap en Python
            self.counter += 1
            return self.aux


if __name__ == "__main__":

    fibonacci = FiboIter() #A partir de la clase FiboIter se crea iterador que se guarda en Fibonacci
    for element in fibonacci: #ejecutar método __next__
        print(element)
        time.sleep(1) #Por cada vuelta del ciclo se tiene un segundo de demora

