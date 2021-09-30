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
  - [Documentación](#documentación)
  - [Documentación](#documentación)

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



