# Integer
entero = 10
print(entero)
print(type(entero), end="\n\n")

#float
flotante = 56.45
flotante = 4565.12345
print(flotante)
print(type(flotante), end="\n\n")

# String
cadena = "Hola a todos"
print(cadena)
cadena="Estoy aprendiendo Python"
print(cadena)
print(type(cadena), end="\n\n")

# Boolean
boleano = True
print(boleano)
print(type(boleano), end="\n\n")

# List, almacena valores dados ya sean enteros, cadenas al mismo tiempo.
#Se puede alterar lo que tenga contenido en cualquier momento.
# .append("texto") agrega a la lista un objeto de manera rápida
lista = [1, 2, 3, 4, 5]
lista = ['a', 'b', 'c', 'd']
lista = [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd']
lista.append("d")
print(lista)
print(type(lista), end="\n\n")

# Tuple, esta se diferencia de las listas debido a que NO se puede alterar lo que contiene.
#Notesé que no es igual cambiar un valor de la tupla a crear una nueva tupla.
tupla = (1, 2, 3, 4, 5)
tupla = ('a', 'b', 'c', 'd')
print(tupla)
print(type(tupla), end="\n\n")

#Dictionary
    #Se refiere a los indices; es decir, una busqueda rápida de una variable mediante el nombre de este.
    #Estos se usan para 
diccionario ={'nombre': 'Luis', 'apellido': 'Sixtos', 'edad': 21}
print(diccionario)
print(diccionario['apellido'])
print(type(diccionario), end="\n\n")
#Tambíen se le pueden agregar cosas de forma rápida.
diccionario['estatura']=1.83
print(diccionario)
#Notesé que es posible tener valores iguales en los diccionarios pero no variables con el mismo nombre.

#Set, No aceptan balores repetidos, no pueden ser modificados y no tienen algún orden.
mset = {'Banana', 'Manzana', 'Uva'}
print(mset)
print(type(mset), end="\n\n")
#Agregar un objeto al set.
mset.add('Pera')
print(mset)
#Combinar la lista;que teniamos previamente, con el set.
mset.update(lista)
print(mset)
