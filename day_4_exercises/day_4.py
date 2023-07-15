
############## FUNCIONES ##############
'''
En Python, las funciones son bloques de código reutilizables que se utilizan para realizar tareas específicas. 
Permiten estructurar el código en segmentos más pequeños y modulares, lo que facilita su mantenimiento, reutilización y 
comprensión. Una función en Python consta de varios elementos clave, que se describen a continuación con ejemplos:
'''

# Declaración de función:
# Para definir una función en Python, se utiliza la palabra clave "def", seguida del nombre de la función y paréntesis 
# que pueden contener los parámetros de entrada. Aquí tienes un ejemplo de una función simple llamada "saludar" que no 
# toma ningún parámetro:
def saludar():
    print("¡Hola! Bienvenido.")

# Parámetros de entrada:
# Las funciones pueden aceptar cero o más parámetros de entrada, que son valores que se pasan a la función para su procesamiento. 
# Estos parámetros se definen dentro de los paréntesis en la declaración de la función. Aquí tienes un ejemplo de una función 
# llamada "saludar_persona" que toma un parámetro de entrada llamado "nombre":
def saludar_persona(nombre):
    print("¡Hola,", nombre + "! Bienvenido.")

# Valor de retorno:
# Las funciones pueden devolver un valor de salida utilizando la palabra clave "return". 
# Esto permite capturar y utilizar el resultado de una función en otras partes del programa. 
# Aquí tienes un ejemplo de una función llamada "sumar" que toma dos parámetros y devuelve su suma:
def sumar(a, b):
    return a + b

# Llamada de función:
# Para utilizar una función, debes llamarla utilizando su nombre seguido de paréntesis. 
# Si la función tiene parámetros, debes proporcionar los valores adecuados al llamarla. 
# Aquí tienes un ejemplo de cómo llamar a la función "sumar" y utilizar su resultado:
resultado = sumar(3, 5)
print(resultado)  # Salida: 8

# Argumentos por posición y por nombre:
# Al llamar a una función, puedes pasar los argumentos por posición, en el orden en que los espera la función, 
# o por nombre, especificando el nombre del parámetro seguido de su valor. Aquí tienes un ejemplo de cómo llamar 
# a la función "saludar_persona" utilizando ambos métodos:
saludar_persona("Juan")  # Salida: ¡Hola, Juan! Bienvenido.
saludar_persona(nombre="Ana")  # Salida: ¡Hola, Ana! Bienvenido.





# En Python, los argumentos arbitrarios son parámetros de una función que permiten recibir un número variable de argumentos. 
# Esto es útil cuando no sabes de antemano cuántos argumentos se pasarán a la función o cuando deseas proporcionar flexibilidad 
# al usuario al llamar a la función. Hay dos tipos de argumentos arbitrarios en Python: argumentos arbitrarios posicionales y
# argumentos arbitrarios de palabras clave.

# Argumentos arbitrarios posicionales:
# Los argumentos arbitrarios posicionales permiten pasar un número variable de argumentos sin especificar sus nombres. 
# Estos argumentos se reciben como una tupla dentro de la función. Para definirlos, se utiliza el símbolo de asterisco (*) 
# seguido de un nombre de parámetro. Aquí tienes un ejemplo de una función llamada "sumar_elementos" que puede recibir 
# cualquier cantidad de números y calcular su suma:
def sumar_elementos(*numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma

# Al llamar a esta función, puedes pasar cualquier número de argumentos separados por comas:
resultado = sumar_elementos(1, 2, 3, 4, 5)
print(resultado)  # Salida: 15

# Argumentos arbitrarios de palabras clave:
# Los argumentos arbitrarios de palabras clave permiten pasar un número variable de argumentos utilizando 
# sus nombres como clave-valor. Estos argumentos se reciben como un diccionario dentro de la función. 
# Para definirlos, se utiliza el símbolo de doble asterisco (**) seguido de un nombre de parámetro. 
# Aquí tienes un ejemplo de una función llamada "imprimir_info" que puede recibir cualquier cantidad de 
# información sobre una persona:
def imprimir_info(**info_persona):
    for clave, valor in info_persona.items():
        print(clave + ": " + valor)

# Al llamar a esta función, puedes pasar cualquier cantidad de argumentos con sus nombres asociados:
imprimir_info(nombre="Juan", edad="25", ciudad="Madrid")
# Salida:
# nombre: Juan
# edad: 25
# ciudad: Madrid

############## FUNCIONES LAMBDA ##############
# Las funciones Lambda en Python son funciones anónimas y pequeñas que se definen sin un nombre específico. 
# Se utilizan comúnmente para realizar tareas simples y rápidas en el código. 
# Aquí tienes algunos ejemplos para ilustrar cómo se utilizan las funciones Lambda en Python:

# Ejemplo básico: Suma de dos números:
sumar = lambda x, y: x + y
resultado = sumar(3, 5)
print(resultado)  # Output: 8

# En este ejemplo, la función Lambda sumar toma dos argumentos x e y y devuelve su suma.



# Ejemplo con filtro: Filtrar números pares de una lista:
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares)  # Output: [2, 4, 6, 8, 10]

# Aquí, utilizamos la función filter() junto con una función Lambda para filtrar los números pares de la lista.


# Ejemplo con map: Duplicar los elementos de una lista:
numeros = [1, 2, 3, 4, 5]
duplicados = list(map(lambda x: x * 2, numeros))
print(duplicados)  # Output: [2, 4, 6, 8, 10]

# En este ejemplo, usamos la función map() junto con una función Lambda para duplicar cada elemento de la lista.


# Ejemplo con sorted: Ordenar una lista de cadenas por longitud:
palabras = ['manzana', 'banana', 'cereza', 'uva', 'kiwi']
ordenado_por_longitud = sorted(palabras, key=lambda x: len(x))
print(ordenado_por_longitud)  # Output: ['uva', 'kiwi', 'banana', 'cereza', 'manzana']

# Aquí, utilizamos la función sorted() junto con una función Lambda para ordenar la lista de palabras por su longitud.

# Estos son solo algunos ejemplos básicos de cómo se utilizan las funciones Lambda en Python. Las funciones Lambda son 
# especialmente útiles en situaciones en las que necesitas funciones rápidas y sencillas sin tener que definirlas 
# formalmente con un nombre.

############## ALCANCE (SCOPE) DE LAS VARIABLES ##############

# El "scope" (alcance) de una variable se refiere a la región del programa donde esa variable es accesible y puede ser utilizada. 
# En Python, existen diferentes niveles de alcance para las variables. Vamos a ver los principales:

# Scope local: Las variables definidas dentro de una función tienen un alcance local, lo que significa que solo están disponibles dentro de esa función. Por ejemplo:
def mi_funcion():
    x = 10
    print(x)  # Output: 10

mi_funcion()
print(x)  # Error: NameError: name 'x' is not defined

# En este caso, la variable x solo es accesible dentro de la función mi_funcion(). Si intentamos acceder a ella fuera de la función, obtendremos un error.

# Scope global: Las variables definidas fuera de cualquier función o bloque de código tienen un alcance global. Esto significa que pueden ser utilizadas en cualquier
# parte del programa, incluyendo dentro de funciones. Por ejemplo:
x = 10

def mi_funcion():
    print(x)  # Output: 10

mi_funcion()
print(x)  # Output: 10

# En este caso, la variable x está definida fuera de la función mi_funcion(), por lo que puede ser accedida tanto dentro como fuera de la función.

# Scope de bloque: A partir de Python 3, se introdujo el concepto de alcance de bloque para variables definidas dentro de bloques condicionales (if, for, while) 
# o bloques de código (encerrados entre llaves {}). Las variables definidas en estos bloques solo son accesibles dentro del bloque en el que se definen. Por ejemplo:
if True:
    y = 20
    print(y)  # Output: 20

print(y)  # Error: NameError: name 'y' is not defined

# En este caso, la variable y está definida dentro del bloque del condicional if, por lo que solo es accesible dentro de ese bloque. 
# Si intentamos acceder a ella fuera del bloque, obtendremos un error.

# Es importante tener en cuenta el alcance de las variables para evitar errores y asegurarse de que las variables estén definidas en el
# alcance correcto para su uso. Además, se puede utilizar la declaración global para indicar que una variable se refiere a una variable global, 
# incluso dentro de una función, y la declaración nonlocal para indicar que una variable se refiere a una variable en un alcance superior 
# dentro de una función anidada.