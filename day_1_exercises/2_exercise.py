# Escribir un programa que pregunte el nombre del usuario en la consola y 
# después de que el usuario lo introduzca muestre por pantalla la cadena 
# ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.
username = input('Introduce tu username: ')
age      = int(input('Introduce tu edad: '))
# print('!Hola',username, '!')

# F-Strings
print(f'!Hola {username}!')
print(f'!Hola {username}! Tu edad multiplicada por 10 es {age * 10}')