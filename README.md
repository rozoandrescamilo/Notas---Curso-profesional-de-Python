# Notas - Curso profesional de Python

Profesor Facundo Garcia Martoni de Platzi.

![](https://static.platzi.com/media/avatars/Platzi-f730e65b-e92b-44d3-81c0-5c59c4dc4658.png) ![](https://static.platzi.com/media/learningpath/badges/46.png) ![](https://static.platzi.com/media/achievements/badge-profesional-de-python-22f3ae5d-ce99-4519-a20a-2aa46ea2c840.png)

## Tabla de Contenidos

- [Introducción](#introducción)
  - [¿Cómo funciona Python?](#cómo-funciona-python)
  - [Cómo organizar las carpetas de tus proyectos](#cómo-organizar-las-carpetas-de-tus-proyectos)
- [Static Typing](#static-typing)
  - [¿Qué son los tipados?](#qué-son-los-tipados)
  - [Tipado estático en Python](#tipado-estático-en-python)
  - [Practicando el tipado estático](#practicando-el-tipado-estático)
- [Conceptos avanzados de funciones](#conceptos-avanzados-de-funciones)
  - [Scope: alcance de las variables](#scope-alcance-de-las-variables)
  - [Closures](#closures)
  - [Programando closures](#programando-closures)
  - [Decoradores](#decoradores)
  - [Programando decoradores](#programando-decoradores)
- [Estructuras de datos avanzadas](#estructuras-de-datos-avanzadas)
  - [Iteradores](#iteradores)
  - [La sucesión de Fibonacci](#la-sucesión-de-fibonacci)
  - [Generadores](#generadores)
  - [Mejorando nuestra sucesión de Fibonacci](#mejorando-nuestra-sucesión-de-fibonacci)
  - [Sets](#sets)
  - [Operaciones con Sets](#operaciones-con-sets)
  - [Eliminando los repetidos de una lista](#eliminando-los-repetidos-de-una-lista)
- [Bonus](#bonus)
  - [Manejo de fechas](#manejo-de-fechas)
  - [Time zones](#time-zones)

# Introducción

## ¿Cómo funciona Python?

Python es un lenguaje interpretado lo que significa que tu código es transformado por el intérprete (máquina virtual de Python) a bytecode antes de ser ejecutado por un ordenador con x sistema operativo. El byte code es un lenguaje de programación de más bajo nivel.

[![1](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/1.png?raw=true "1")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/1.png?raw=true "1")

El **Garbage collector** toma los objetos y variables que no están en uso y los elimina.

`_pycache_` es el directorio (carpeta) que contiene el bytecode (el código intermedio) que crea Python para que lo pueda leer la máquina virtual.

## Cómo organizar las carpetas de tus proyectos

Un **módulo** es cualquier archivo de Python. Generalmente, contiene código que puedes reutilizar.

Un **paquete** es un conjunto de módulos. Siempre posee el archivo `__init__.py` , se pronuncia **dunder init** diminutivo de **double underscore.**

Un ejemplo de organizar los archivos de 🐍Python es de la siguiente manera.

[![2](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/2.png?raw=true "2")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/2.png?raw=true "2")

# Static Typing

## ¿Qué son los tipados?

Los tipados son una clasificación de los lenguajes de programación, tenemos cuatro tipos:
- **Estático:** Detectan los errores en tiempo de compilación. No se ejecuta hasta corregir.
- **Dinámico:** Detectan el error en tiempo de ejecución. Nos dice el error cuando llega a la línea del código.
- **Débil:** Menos severidad con los tipos de datos. Si quiero sumar número y letra, las concatenaría como strings.
- **Fuerte:** Más severidad con los tipos de datos. Sumar un número + una letra arrojará error.

[![3](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/3.png?raw=true "3")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/3.png?raw=true "3")

El **tipado del lenguaje** depende de cómo se trata a los tipos de datos.

El **tipado estático** es el que levanta un error en el tiempo de compilación, ejemplo en JAVA:

[![4](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/4.png?raw=true "4")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/4.png?raw=true "4")

El **tipado dinámico** levanta el error en tiempo de ejecución, ejemplo en Python:

[![5](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/5.png?raw=true "5")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/5.png?raw=true "5")

El **tipado débil** es el que hace un cambio en un tipo de dato para poder operar con él, como lo hace JavaScript y PHP.

**🐍 Python es un lenguaje de tipado 👾 Dinámico y 💪 Fuerte.**

## Tipado estático en Python

Para hacer que Python sea de tipado estático es necesario agregar algo de sintaxis adicional a lo aprendido, además, esta característica solo se puede aplicar a partir de la versión 3.6.

[![6](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/6.png?raw=true "6")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/6.png?raw=true "6")

Del mismo modo se puede usar esta metodología de tipado en Python a funciones adicionando el signo menos a continuación del signo mayor que para determinar el tipo de dato. Ejemplo:

[![7](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/7.png?raw=true "7")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/7.png?raw=true "7")

Existe una librería de fabrica que viene preinstalada con Python que se llama `typing`, que es de gran utilidad para trabajar con tipado con estructuras de datos entre la versión 3.6 y 3.9, entonces:

[![8](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/8.png?raw=true "8")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/8.png?raw=true "8")

[![9](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/9.png?raw=true "9")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/9.png?raw=true "9")

**Módulo** `mypy`

El módulo mypy se complementa con el módulo typing ya que permitirá mostrar los errores de tipado débil en Python.

## Practicando el tipado estático

Para prácticar el tipado estático se utilizará el código que nos muestra si una palabra es un palindromo, pero primero es necesario inicializar nuestro repositorio con `git init`, con el comando `py -m venv venv` creamos el entorno virtual donde realizaremos todo. Se la carpeta de **.gitignore** y se agrega dentro la carpeta **venv/** para que no la agregue al repositorio, se activa el entorno con el comando `.\venv\Scripts\activate` y por ultimo instalamos  nuestro módulo con `pip install mypy`:

[![10](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/10.png?raw=true "10")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/10.png?raw=true "10")

Una vez listos se podrá programar el código de la siguiente manera probando con la palabra **ana** para saber si es o no un palíndromo:

```python
def is_palindrome(string: str) -> bool:
    string = string.replace(' ', '').lower() #Borrar espacios de la palabra
    return string == string[::-1] #Poner la palabra al revés 

def run():
    print(is_palindrome(1000))

if __name__ == '__main__':
    run()
```

[![11](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/11.png?raw=true "11")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/11.png?raw=true "11")

Como prueba cambiamos el string **ana** por el número 1000, al correrlo en la terminal nos arroja un Traceback con un error de tipo **AtributeError** debido a que nuestro código esta configurado para leer strings.

[![12](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/12.png?raw=true "12")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/12.png?raw=true "12")

Utilizando el comando flag `mypy palindrome.py --check-untyped-defs` en la terminal nos arrojará un mensaje de error mucho mas amigable y específico, informando que lo que agregamos (un número entero: int) no es compatible con el tipo que definimos (cadena de letras: str):

[![13](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/13.png?raw=true "13")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/13.png?raw=true "13")

### Reto

Crea un programa que verifique si un número es primo o no, pero hazlo con tipado estático.

```python
def is_prime(number: int) -> bool:
    """Returns True if number is prime or False if the number is not prime"""
    results_list = [x for x in range(2, number) if number % x == 0]
    return len(results_list) == 0

def run():
    number: int = 73
    number_is_prime: bool = is_prime(number)
    print(f'Is {number} a prime number? {number_is_prime}')

if __name__ == '__main__':
    run()
```

[![14](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/14.png?raw=true "14")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/14.png?raw=true "14")

# Conceptos avanzados de funciones

## Scope: alcance de las variables

El scope es el alcance que tienen las variables. Depende de donde declare o inicialice una variable para saber si tiene acceso. Regla de oro:

**"Una variable solo está disponible dentro de la región donde fue creada".**

[![14,5](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/14,5.png?raw=true "14,5")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/14,5.png?raw=true "14,5")

### Local Scope

Es la región que corresponde el ámbito de una función, donde podremos tener una o más variables, las variables van a ser accesibles únicamente en esta región y no serán visibles para otras regiones.

### Global Scope

Al escribir una o más variables en esta región, estas podrán ser accesibles desde cualquier parte del código.

[![15](https://raw.githubusercontent.com/hackmilo/Notas---Curso-profesional-de-Python/main/img/15.png "15")](https://raw.githubusercontent.com/hackmilo/Notas---Curso-profesional-de-Python/main/img/15.png "15")

## Closures

Es una forma de acceder a variables de otros scopes a través de una nested function (función anidada). Se retorna la nested function y esta recuerda el valor que imprime, aunque a la hora de ejecutarla no esté dentro de su alcance.

Reglas para encontrar un closure:

1. Debemos tener una nested function.
2. La nested function debe referenciar un valor de un scope superior.
3. La función que envuelve la nested function debe retornarla también.

### ¿Cuándo utilizar los Closures?

- Cuando tenemos una clase que tiene solo un método.
- Cuando trabajamos con decoradores.

[![16](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/16.png?raw=true "16")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/16.png?raw=true "16")

## Programando closures

Para este ejemplo se creará un closure que repita strings dependiendo de un número posible, por ejemplo el string “Platzi” con el número 3, esto debería devolver PlatziPlatziPlatzi:

```python
def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "Solo puedes utilizar cadenas"
        return string * n
    return repeater

def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("Hola"))
    repeat_10 = make_repeater_of(10)
    print(repeat_5("Platzi"))

if __name__ == "__main__":
    run()
```

[![17](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/17.png?raw=true "17")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/17.png?raw=true "17")

### Reto

Realizar un closure que retorne una función que retorne una división de un número x en n.

```python
def make_division_by(n):
    def division(x: int) -> float:
        assert n > 0, "El valor ingresado en el divisor debe ser mayor a cero"
        return round(x/n, 2)
    return division

def run():
    division_by_3 = make_division_by(3)
    division_by_5 = make_division_by(5)
    division_by_18 = make_division_by(18)
    print(division_by_3(18))
    print(division_by_5(100))
    print(division_by_18(54))
    print(division_by_3(division_by_5(200)))

if __name__ == "__main__":
    run()
```

[![18](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/18.png?raw=true "18")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/18.png?raw=true "18")

## Decoradores

Es el concepto más avanzado de funciones. Es una función que recibe como parámetro otra función, le añade cosas, y retorna una función diferente.

La función tiene que llamarse en la nested para que la función decorador pueda incluirla. Sin la nested tendríamos que llamar a la función decorador e incluirle la función hola. Con este sistema solo creamos el decorador con nested y lo colocamos como decorador en la función que queremos decorar.

[![19](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/19.png?raw=true "19")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/19.png?raw=true "19")

[![20](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/20.png?raw=true "20")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/20.png?raw=true "20")

[![21](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/21.png?raw=true "21")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/21.png?raw=true "21")

## Programando decoradores

Creamos el archivo **decorators.py** y vamos a crear un decorador que se llame **execution_time** y nos va servir para medir el tiempo de ejecución de una función hasta poner su resultado en pantalla, se podrá llevar a otras funciones como un código útil con la eficiencia de estos.

```python
from datetime import datetime #Módulo para medir tiempo de una ejecución

def execution_time(func):
    def wrapper(): #wrapper calcula el tiempo de operación
        inicial_time = datetime.now() #Tiempo exacto ahora
        func() #ejecutar la función
        final_time = datetime.now() #Tiempo final
        time_elapsed = final_time - inicial_time #Obtener la cantidad de segundos
        print("Pasaron " + str(time_elapsed.total_seconds()) + " segundos")
    return wrapper #Closure donde la nested function debe retornar

@execution_time #Decorador
def random_func():
    for _ in range(1, 100000000): #Cuando no se requiere tener el valor de cada  vuelta se coloca "_"
        pass

random_func()
```

[![22](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/22.png?raw=true "22")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/22.png?raw=true "22")

Ahora vamos a agregar algunas otras funciones para decorarlas, pero es necesario que nuestra nested function **wrapper** agreguemos los parámetros: `*args`, `**Kwargs`. No importa la cantidad de argumentos posicionales (`*args`) y la cantidad de argumentos nombrados (`**Kwargs`) la función lo leerá.

Operador de desestructuración “*”

```python
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
```

[![23](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/23.png?raw=true "23")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/23.png?raw=true "23")

### Reto libre

Utilizando el código anterior para calcular al tiempo de ejecución , realice un programa de libre elección.

```python
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
```

[![24](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/24.png?raw=true "24")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/24.png?raw=true "24")

[![25](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/25.png?raw=true "25")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/25.png?raw=true "25")

# Estructuras de datos avanzadas

## Iteradores

Son una estructura de datos para guardar datos infinitos.

Los iterables son los objetos que podemos recorrer a través de un ciclo, dicho de otra manera, son estructuras de datos divisibles en elementos que puedo recorrer en un ciclo. Por ejemplo, una lista a la cual se puede acceder a sus elementos mediante un ciclo for.

Todos los iterables pueden convertirse en iteradores. De esta manera es que internamente Python los puede recorrer realmente, esto mediante parsing usando el comando iter.

[![26](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/26.png?raw=true "26")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/26.png?raw=true "26")

[![27](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/27.png?raw=true "27")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/27.png?raw=true "27")

> Un ciclo **for** no existe en Python, realmente es un **alias** del segundo bloque donde hacemos el ciclo infinito con **while True** y condicionado con el **try** y **except** que recorre un iterador hasta encontrar el **StopIteration**.

[![28](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/28.png?raw=true "28")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/28.png?raw=true "28")

[![29](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/29.png?raw=true "29")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/29.png?raw=true "29")

## La sucesión de Fibonacci

La sucesión de Fibonacci es conocida desde hace miles de años, pero fue **Fibonacci (Leonardo de Pisa)** quien la dio a conocer al utilizarla para resolver un problema.

El primer y segundo término de la sucesión son 0 y 1, los siguientes términos se obtienen sumando los dos términos que les preceden.

La sucesión de Fibonacci es una sucesión definida por **recurrencia**. Esto significa que para calcular un término de la sucesión se necesitan los dos términos que le preceden.

[![30](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/30.png?raw=true "30")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/30.png?raw=true "30")

```python
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
```

[![31](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/31.png?raw=true "31")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/31.png?raw=true "31")

### Reto

Modificar el código de Fibonacci para que nos imprima hasta cierto valor de la sucesión (144).

```python
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
```

[![32](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/32.png?raw=true "32")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/32.png?raw=true "32")


## Generadores

Sugar syntax de los iteradores. Los generadores son funciones que guardan un estado. Es un iterador escrito de forma más simple y elegante.

> **Syntactic Sugar - Azúcar Sintáctico:** En pocas palabras, el azúcar sintáctico es una sintaxis que permite a los desarrolladores escribir código más fácilmente, de una manera “dulce”, por lo tanto, te da el lujo de no saber cómo funciona el sistema. Nos facilita la vida y muchas veces ni nos damos cuenta o ni siquiera sabemos que los estamos usando pero en cualquier caso siempre es útil saber cómo funciona en detalle, porque tarde o temprano lo haremos.

[![33](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/33.png?raw=true "33")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/33.png?raw=true "33")

Ahora veremos un generator expression (es como list comprehension, pero mucho mejor, porque podemos manejar mayor cantidad de información sin tener problemas de rendimiento):

[![34](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/34.png?raw=true "34")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/34.png?raw=true "34")

## Mejorando nuestra sucesión de Fibonacci

```python
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
```

[![34,5](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/34,5.png?raw=true "34,5")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/34,5.png?raw=true "34,5")

### Reto

Modifica el generador que acabamos de crear, pero que en lugar de devolver los infinitos números de la sucesión de Fibonacci, que solo devuelva los números hasta un máximo.

```python
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
```

[![35](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/35.png?raw=true "35")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/35.png?raw=true "35")

## Sets

Los sets son una estructura de datos muy similares a las listas en cuanto a su forma, pero presentan ciertas características particulares:

- Los sets es una colección de datos que son inmutables.
- Cada elemento del set es único, esto es que no se admiten duplicados, aun si durante la definición del set se agregan elementos repetidos Python solo guarda un elemento.
- Los sets guardan los elementos en desorden.

Para declararlos se utilizan los **{}** parecido a los diccionarios solo que carece de la composición de conjunto {a:b, c:d}.

Al set no se puede acceder con un índice.

Para declarar un set, el grupo de elementos debe ir entre llaves. Se diferencia de los diccionarios ya que no contienen el símbolo “:”, por lo que automáticamente Python lo entiende como un set de datos.

En caso de desear declarar un set vacío no es posible usar llaves ya que al no contener datos entre las llaves las interpreta como un diccionario. En este caso la declaración de un set debe ser explicita mediante el comando set().

[![36](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/36.png?raw=true "36")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/35.png?raw=true "36") [![37](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/37.png?raw=true "37")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/37.png?raw=true "37")

### Casting con Sets
Para convertir una estructura de datos a un set se utiliza el comando set(). Si se castea una lista a un set como resultado tenemos un set de elementos únicos ya que elimina los elementos repetidos. Los elementos mutables, en caso de existir, este comando los eliminará.

[![38](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/38.png?raw=true "38")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/38.png?raw=true "38")

Los sets no pueden ser leídos como las listas o recorridos a través de slices, esto debido a que no tienen un criterio de orden. Sin embargo, si podemos agregar o eliminar items de los sets utilizando métodos:

- **add():** nos permite agregar elementos al set, si se intenta agregar un elemento existente simplemente Python los ignorara.
- **update():** nos permite agregar múltiples elementos al set.
- **remove():** permite eliminar un elemento del set, en el caso en que no se encuentre presente dicho elemento, Python elevará un error.
- **discard():** permite eliminar un elemento del set, en el caso en que no se encuentre presente dicho elemento, Python dejará el set intacto, sin elevar ningún error.
- **pop():** permite eliminar un elemento del set, pero lo hará de forma aleatoria.
- **clear():** Limpia completamente el set, dejándolo vació.

[![39](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/39.png?raw=true "39")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/39.png?raw=true "39")

[![40](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/40.png?raw=true "40")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/40.png?raw=true "40")

[![41](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/41.png?raw=true "41")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/41.png?raw=true "41")

## Operaciones con Sets

- **La unión:** Resultado de combinar todos los elementos que tienen dos conjuntos.

[![42](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/42.png?raw=true "42")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/42.png?raw=true "42")

- **La intersección:** Es el resultado de combinar ambos sets y quedarse con los elementos que tienen en común.

[![43](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/43.png?raw=true "43")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/43.png?raw=true "43")

- **La diferencia:** Resultado de tomar dos sets y de uno quitar todos los elementos que tiene el otro.

[![44](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/44.png?raw=true "44")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/44.png?raw=true "44")

- **Diferencia simétrica:** Es lo contrario de la intersección, es el resultado de combinar ambos sets y quedarse con los elementos que no se comparten.

[![45](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/45.png?raw=true "45")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/45.png?raw=true "45")

Ejemplo con Pokemons :smile_cat:

```python
pokemon_tipo_fuego = { 'Charizard', 'Moltres' }
pokemon_tipo_volador = { 'Charizard', 'Butterfree', 'Pidgeot', 'Fearow', 'Dodrio', 'Gyarados', 'Aerodactyl',
  'Articuno', 'Zapdos', 'Moltres', 'Dragonite' }
pokemon_tipo_veneno = { 'Butterfree' }
pokemon_tipo_normal = { 'Pidgeot', 'Fearow', 'Dodrio' }
pokemon_tipo_agua = { 'Gyarados' }
pokemon_tipo_roca = { 'Aerodactyl' }
pokemon_tipo_hielo = { 'Articuno' }
pokemon_tipo_electrico = { 'Zapdos' }
pokemon_tipo_dragon = { 'Dragonite' }

my_set1 = pokemon_tipo_fuego | pokemon_tipo_agua
print(f'Pokemon tipo fuego | agua: {my_set1}')

my_set2 = pokemon_tipo_normal & pokemon_tipo_volador
print(f'Pokemon tipo normal & volador: {my_set2}')

my_set3 = pokemon_tipo_volador - pokemon_tipo_fuego
print(f'Pokemon tipo volador - fuego: {my_set3}')

my_set4 = pokemon_tipo_dragon ^ pokemon_tipo_electrico
print(f'Pokemon tipo dragon ^ electrico: {my_set4}')

```

[![46](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/46.png?raw=true "46")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/46.png?raw=true "46")

## Eliminando los repetidos de una lista

Se crea un programa que elimine los elementos repetidos de una lista utilizando ciclo for:

```python
def remove_duplicates(some_list):
    without_duplicates = [] #lista que contenga elementos sin repetir
    for element in some_list:
        if element not in without_duplicates: #Si no esta elemento lo agrega a la lista
            without_duplicates.append(element)
    return without_duplicates

def run():
    random_list = [1, 1, 2, 2, 4]
    print(remove_duplicates(random_list))

if __name__ == "__main__":
    run()
```

[![47](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/47.png?raw=true "47")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/47.png?raw=true "47")

### Reto

Crea un programa que elimine los elementos repetidos de una lista, pero en lugar  de un ciclo for utiliza **sets.**

```python
def remove_duplicates(some_list):
    return set(some_list)

def run():
    random_list = [1, 1, 2, 2, 4, 5, 5, 6, 6]
    print(remove_duplicates(random_list))

if __name__ == "__main__":
    run()
```

[![48](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/48.png?raw=true "48")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/48.png?raw=true "48")

# Bonus

## Manejo de fechas

**Método básico con Coordinated Universal Time / Tiempo Universal Coordinado (UTC)**

Es importante evitar usar **datetime.now()** porque toma la hora local. Mejor usar **datetime.utcnow()** para usar la hora universal. Nosotros trabajamos con equipos de todo el mundo, no podemos usar hora local.

Para esto debemos tener conocimiento del módulo **datetime,** para esto algunos ejemplos:

[![49](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/49.png?raw=true "49")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/49.png?raw=true "49")

Solo la fecha de hoy:

[![50](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/50.png?raw=true "50")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/50.png?raw=true "50")

Imprimir por separado año, mes y día:

[![51](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/51.png?raw=true "51")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/51.png?raw=true "51")

### Formateo de fechas

Tabla de código de formato resumida:

[![52](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/52.png?raw=true "52")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/52.png?raw=true "52")

Lista oficial de todos los códigos de formato:
[https://docs.python.org/es/3/library/datetime.html#strftime-and-strptime-format-codes](https://docs.python.org/es/3/library/datetime.html#strftime-and-strptime-format-codes "https://docs.python.org/es/3/library/datetime.html#strftime-and-strptime-format-codes")

Ejemplo:

[![53](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/53.png?raw=true "53")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/53.png?raw=true "53")

[![54](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/54.png?raw=true "54")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/54.png?raw=true "54")

[![55](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/55.png?raw=true "55")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/55.png?raw=true "55")

## Time zones

Para trabajar con zonas horarias se debe trabajar con el módulo **pytz,** el cual debe ser instalado por **pip** ya que no viene de fábrica:

[![56](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/56.png?raw=true "56")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/56.png?raw=true "56")

Adicional, requerimos los **Time zones database name** que podemos encontrar en el siguiente enlace:

[https://en.wikipedia.org/wiki/List_of_tz_database_time_zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones "https://en.wikipedia.org/wiki/List_of_tz_database_time_zones")

```python
from datetime import datetime
import pytz

bogota_timezone = pytz.timezone("America/Bogota") #Zona horaria Bogotá "America/Bogota"
bogota_date = datetime.now(bogota_timezone)
print("Bogotá: ", bogota_date.strftime("%d/%m/%Y, %H:%M:%S"))

mexico_timezone = pytz.timezone("America/Mexico_City")
mexico_date = datetime.now(mexico_timezone)
print("Ciudad de México: ", mexico_date.strftime("%d/%m/%Y, %H:%M:%S"))

caracas_timezone = pytz.timezone("America/Caracas")
caracas_date = datetime.now(caracas_timezone)
print("Caracas: ", caracas_date.strftime("%d/%m/%Y, %H:%M:%S"))
```

[![57](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/57.png?raw=true "57")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/57.png?raw=true "57")

# ¡FELICITACIONES!, ya eres un experto en Python.
## ¡Nunca pares de aprender!

[![58](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/58.png?raw=true "58")](https://github.com/hackmilo/Notas---Curso-profesional-de-Python/blob/main/img/58.png?raw=true "58")
