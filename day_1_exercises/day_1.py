############## PYTHON CLI ##############
# Python tiene una CLI "Commands Line Interface" que te permite ejecutar comandos de Python en tiempo real
# La forma en la que se accede a ella es escribiendo en la terminal 'python3' 
# Para salir de ella, ejecuta exit()

############## PYTHON EJECUTANDO ARCHIVOS ##############
# Para que un archivo Python sea ejecutable, necesita que su extensión sea '.py'
# Unicamente debes ejecutar en la terminal: python3 [Nombre del archivo].py

############## COMENTARIOS ##############

# Esto es un comentario de una sola línea

# Los comentarios suelen usarse para describir qué hace X línea de código
# Los comentarios suelen usarse también para evitar que cierto código se ejecute


"""
Esto es un comentario
de múltiples líneas :D
"""

############## VARIABLES ##############

'''
Las variables no requieren que se les defina el tipo de dato
que almacenarán, Python es capaz de distinguirlo y hacerlo por nosotros
'''
integer_var = 4 # ENTERO
float_var = 2.456 # FLOTANTE
true_boolean_var = True # BOOL
false_boolean_var = False # BOOL
string_var = 'Hola' # STRING
another_string_var = "Hola" # STRING

# Las variables pueden cambiar de tipo de dato a lo largo de la ejecución del programa
integer_var = 5
print(type(integer_var)) # IMPRIMIRÁ 'INT'
integer_var = 5.5
print(type(integer_var)) # AHORA IMPRIMIRÁ 'FLOAT'


# Técnicas para el nombramiento de variables de más de una palabra
myVariableCamelCase = "Camel Case"
MyPascalCamelCase = "Pascal Case"
my_snake_variable = "Snake"


# MÚLTIPLES VALORES PARA VARIABLES
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# UN ÚNICO VALOR PARA MÚLTIPLES VARIABLES
x = y = z = "Orange"
print(x)
print(y)
print(z)

############## OPERADORES ARTIMÉTICOS ##############

num1 = 10 
num2 = 35
suma = num1+ num2
resta = num1 - num2
division = num1 / num2 # El resultado siempre será un FLOTANTE! 
division_entera = num1 // num2 # El resultado siempre será el entero inferior más próximo
multiplicacion = num1 * num2
exponenciacion = num2 ** num1

print("Suma:", suma)
print("Resta:", resta)
print("División:",division)
print("División entera",division_entera)
print("Multiplicación:",multiplicacion)
print("Exponenciación:",exponenciacion)


############## FUNCIÓN PRINT() ##############
print('Hola Mundo')
print('Hola','Mundo') # Por defecto, las palabras se separarán por un espacio
print('Hola','Mundo',sep='/') # Puedo alterar ese comportamiento utilizando el argumento 'sep' y especificando el separador
print('Hola', end='?') # Por defecto Python agrega un salto de línea, puedo alterar ese comportamiento con el argumento 'end'

#### F-STRINGS ####
# Te permiten formatear strings de una manera sencilla
# Únicamente hay que colocar el string dentro de f''
nombre = 'Daniel' # String
edad   = 25 # Integer
print(f'Mi nombre es {nombre} y tengo {edad} años')

# Dentro de {...} puedes colocar variables o incluso operaciones como sumas, restas, llamadas a funciones, etc...
# También puedes asignar a una variable tu f-string y después mandarla a llamar:
my_f_string = f'Mi nombre es {nombre} y tengo {edad} años'
print(my_f_string)


############## FUNCIÓN INPUT() ##############
# Sirve para pedir la entrada de datos al usuario, dentro de los paréntesis vas el mensaje que quieres mostrarle
# La ejecución del programa se detiene, esperando el input del usuario
username = input('Introduce tu username:')
print(username)