############## PYTHON CASTING ##############
# Permite convertir tipos de datos, ya sea a tipo entero, flotante o string
estatura = float(input('Introduce tu estatura: '))
edad = int(input('Introduce tu edad: '))
print(estatura*10)
print(edad*10)

############## STRINGS ##############

# Puedes asignar strings multilínea a una variable de la siguiente forma (pueden ser comillas dobles o simples)
my_string = '''
asjhdkjashdkjashda
jasbdkjashdkjahsdka
kjasdkjahsdkjasd
'''
print(my_string)

# Cada tipo de dato en Python es una clase en específico y por lo tanto, cuenta con métodos que alteran su comportamiento
# Algunos de los métodos de la Clase <str> son:

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

y = txt.capitalize()
print (y)

# Una lista completa de los métodos se encuentra aquí https://www.w3schools.com/python/python_ref_string.asp

# "CONCATENAR" en Python significa unir dos o más strings, esto se logra utilizando el operador +
my_string_1 = 'Hola'
my_string_2 = 'Mundo!'
my_concatenated_string = my_string_1 + ' ' + my_string_2
print(my_concatenated_string)

# F-STRINGS sirve para formatear una cadena de texto de forma sencilla
name = input('Introduce your name: ')
my_output = f'My name is {name}!'

# ESCAPE CHARACTERS sirven para utilizar caracteres especiales dentro de un string, para ello se utiliza \
# Una lista de ellos se encuentra aquí: https://www.w3schools.com/python/gloss_python_escape_characters.asp
my_output = 'My name is \'Daniel\''
print(my_output)

############## IF STATEMENT ##############

### IF STATEMENTS
num1 = 15
num2 = 15
if num1 != num2:
    print('Entró al IF') 
elif num1 >= num2:
    print('Entró al segundo IF')
else:
    print('Entró al ELSE')
    
# IF en una sola línea para mejor sintaxis
if 5 > 3: print("a is greater than b")

# Operador TERNARIO - IF-ELSE en una sola línea
a = 2
b = 330
print("A") if a > b else print("B")

############## WHILE LOOPS ##############

### WHILE LOOPS
i = 1
while i < 6:
	if i == 3:
		print(i)
		break # ROMPERÁ LA EJECUCIÓN DEL CICLO Y PASARÁ A LA SIGUIENTE LÍNEA (#75)
	print(i)
	i += 1 # RECUERDA SIEMPRE INCREMENTAR EL ITERADOR
print(i)


i = 0
while i < 6:
  i += 1
  if i == 3:
    continue # SALTA A LA SIGUIENTE ITERACIÓN E IGNORA LAS LÍNEAS DE CÓDIGO SIGUIENTES
  print(i) # al pasar por el CONTINUE, esta línea no se ejecutará


i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
else: # La sentencia ELSE se ejecutará siempre una vez, cuando la condición evaluada en el While ya no se cumpla
  print('Ha ginalizado el ciclo')
  print(i)

############## FOR LOOPS ##############

# La función range(x,y,z) nos brinda una lista iterable desde [x,y) en incrementos de z
print(list(range(1,11,2)))

my_string = 'HolaMundo' # Un string es una lista de caracteres: ['H','o','l','a','M','u','n','d','o'] por lo tanto se puede indexar e iterar

# Una sintaxis simple, requiere de un elemento iterable (my_string) y de un iterador (my_char)
for my_char in my_string: 
	print(my_char)


