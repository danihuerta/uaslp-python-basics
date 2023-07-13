############## LISTAS ##############
# Las listas son uno de los tipos de datos conocidos como 'collections', los cuales permiten almacenar múltiples valores en una variable

# La forma de declarar una lista es utilizando: []
my_empty_list = []

# Si una lista tiene múltiples elementos, deben estar separados por coma
# Cada elemento puede ser de cualquier tipo de dato
# Al ser un elemento iterable, significa que cada elemento tiene una posición específica, iniciando por 0

# Posición   0        1        2
nombres = ['Luis', 'Carlos', 'María']
print(nombres) # Imprime la lista completa
print(nombres[0]) # Imprime el elemento 0 (primer elemento)
print(nombres[1]) # Imprime el elemento 1
print(nombres[2])
# print(nombres[3]) # Imprime el elemento en una posición fuera del rango, por lo tanto da ERROR

# Se pueden asignar valores en posiciones específicas
nombres[0] = 'Ernesto' # Agrega el valor 'Ernesto' en la posición 0

# Si el index es un número negativo, se partirá desde el final de la lista, hacia el inicio
print(nombres[-1]) # Es el último elemento
print(nombres[-2]) # Es el penúltimo elemento
print(nombres[-3]) # Sucesivamente...

# Posición       0         1         2         3        4
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(len(thislist)) # El método LEN permite obtener el tamaño de una lista

# El index puede ser un rango de elementos: [valor incluido : valor excluido]
print(thislist[1:3]) # Imprime desde la posición 1 hasta la 2 (3-1 = 2)
print(thislist[:3])  # Si se omite el primer elemento, tomará como 0 (inicio de la lista)
print(thislist[2:])  # Si se omite el segundo elemento, tomará el final de la lista

# IN
# Esta keyword nos arroja un boolean dependiendo de si X elemento se encuentra o no, en la lista
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist: # ¿El elemento 'apple' se encuentra en la lista 'thislist'?
  print("Yes, 'apple' is in the fruits list")

# Python hace la distinción del tipo de dato correspondiente para c/u de los elementos de la lista  
thislist = ["apple", 2]
print(thislist[0]*2) # appleapple porque Python detecta que es un String
print(thislist[1]*2) # 4 porque Python detecta que es un entero

# Añadir elementos a la lista
thislist = ["apple", "banana", "cherry"]
thislist.append("orange") # Agrega elementos al final de la lista
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange") # Agrega elementos en la posición especificada y el resto de elementos se recorre
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical) # Combinación de dos listas a partir de la lista sobre la cual se manda a llamar el método extend
print(thislist)

# Eliminar elementos
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana") # Elimina un elemento en específico, debe de encontrarse en la lista
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1) # Elimina el elemento en la posición 1
thislist.pop() # último elemento de la lista
print(thislist)

# Iterar listas
# Una lista es un elemento iterable por lo que podemos recorrer cada uno de sus elementos
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

############## TUPLAS ##############
# Muy similar a las listas, sólo que las tuplas son INMUTABLES, eso quiere decir que no se pueden modificar una vez creadas
# Utilizadas cuando sabes que a lo largo de tu ejecución del programa, la tupla permanecerá igual, como por ejemplo se puede 
# utilizar para almacenar atributos de una base de datos
user_data = ('John', 'American', 1964) # Se declaran con Paréntesis
user_one_value = ('John',) # Una tupla de un elemento debe de agregársele una coma al final
print(type(user_one_value))
print(user_data[-1]) # Al igual que en las listas, pueden ser indexadas
print(len(user_data)) # Al igual que en las listas, se puede utilizar la función LEN para obtener la longitud de una tupla

# Múltiples valores para múltiples variables
(green, yellow, red) = ("apple", "banana", "cherry") # Se asignarán los valores de la tupla, a su respectiva variable del lado izquierdo
(green, yellow, *red) = ("apple", "banana", "cherry", "a", "b", "c") # 'red' tomará el resto de valores sobrantes en la tupla
(green, *yellow, red) = ("apple", "banana", "cherry", "a", "b", "c") # 'yellow' tomará el resto de valores sobrantes en la tupla, dejándole el último a 'red'

# Listas formadas por tuplas
city1 = ('London','UK',8.98)
city2 = ('Canberra','Australia',0.4)
city3 = ('Algiers', 'Algeria', 3.9)
capitals = [city1,city2,city3]
for capital in capitals:
	print(f'Name: {capital[0]}, Country: {capital[1]}, Population: 	{capital[2]}')
	
# Tuplas con una lista en su interior
user_data = ('John','American',1964,[77.0,78.2,77.5])
user_data[3].append(79.5) # Se está modificando un elemento MUTABLE
print(user_data)


############## DICCIONARIO ##############
# Permite almacenar valores en una estructura en formato key-value

empty_dict = {} # Diccionario vacío
print(type(empty_dict)) # Pertenece a la clase dict

# Es posible agregar keys repetidas, no arrojará error pero al tratarse de elementos únicos, sólo retornará la primera ocurrencia
emails = {
'Anne Stahl': 'astahl@gmail.com',
'Dany Huerta': 'dani@gamil.com',
'Andy Herrera': 'andy@gmail.com',
'Andy Herrera': 'andy@gmail.com'
}

# Para editar el valor una key existente
emails['Anne Stahl'] = 'testing'
print(emails['Anne Stahl'])

# Podemos acceder a sus keys, values o ambos a través de los siguientes métodos. Nos lo retornará como tuplas
print(emails.keys())
print(emails.values())
print(emails.items())

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Para agregar un key-value simplemente hay que especificar el diccionario, la key nueva y el valor nuevo
thisdict["color"] = "red"
print(thisdict)

# Iterando diccionarios

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Iterando únicamente sobre los VALORES
for x in thisdict.values():
  print(x)

# Iterando únicamente sobre las KEYS
for x in thisdict.keys():
  print(x)

# Accediendo a ambos elementos
for x, y in thisdict.items():
  print(x, y) #x=key, y=value, debido a que thisdict.items() nos retorna una tupla (Revisar línea 87)