from time import sleep #Módulo para manejar el tiempo de salida en consola

class FiboIter: #Se crea una nueva clase  para el iterador

    def __init__(self, max = None):
        self.max = max

    def __iter__(self): #Con el primer método se inicializan las variables
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self): #Método para que funcione la sucesión
        if not self.max:

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

        else:
            if self.counter == 0 and self.n1 <= self.max:
                self.counter += 1
                return self.n1
            elif self.counter == 1 and self.n2 <= self.max:
                self.counter += 1
                return self.n2
            elif self.counter > 1:
                self.aux = self.n1 + self.n2
                self.n1, self.n2 = self.n2, self.aux #Swap en Python
                if self.aux >= self.max + 1:
                    raise StopIteration
                self.counter += 1
                return self.aux

if __name__ == "__main__":
    fibonacci = FiboIter(144) #A partir de la clase FiboIter se crea iterador que se guarda en Fibonacci
    for element in fibonacci: #ejecutar método __next__
        print(element)
        sleep(0.7) #Por cada vuelta del ciclo se tiene un segundo de demora