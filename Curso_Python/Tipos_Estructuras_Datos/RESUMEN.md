
# Estructuras de datos fundamentales del lenguaje Python. 
Comprender estas estructuras y saber cuándo utilizarlas permite escribir un código más limpio, eficiente y fácil de mantener.

## Listas   
Son colecciones de datos ordenadas y mutables, o sea que se permite (adicionar, modificar o eliminar) un elemento.

Ejemplo:
- Adicionar elemento: 
    lista_frutas.append("pera") # Adiciona "pera" al final de la lista

- Modificar elemento (por índice)
    lista_frutas[2] = "uvas" # Cambia "uva" por "uvas"

- Eliminar elemento (por índice)
    lista_frutas.pop(2) # Elimina "uvas"

## Tuplas  
Similares a las listas, pero inmutables, lo que significa que sus elementos no pueden modificarse después de ser creadas. 
Son ideales para datos que deben permanecer constantes.

Ejemplo:
colores = ("rojo", "azul", "verde")

## Sets  
Colecciones sin duplicados y sin un orden específico. Se  puede crear a partir de una lista.
Son muy útiles para eliminar elementos repetidos y realizar operaciones matemáticas como uniones o intersecciones.

Ejemplo:
numeros = {1, 2, 3, 3, 4} # Print: {1, 2, 3, 4}

- Convertir lista_frutas a set(para eliminar elementos duplicados)
lista_frutas = ["manzana", "banana", "uva", "manzana"]
set_frutas = set(lista_frutas) #Print: {'manzana', 'banana', 'uva'}

## Diccionarios  
Estructuras clave‑valor que permiten representar datos de forma clara y acceder a la información de manera rápida. 
Son ideales para modelar entidades del mundo real.

Ejemplo:
persona = {"nombre": "Ana", "edad": 25}

# NOTA: Cada estructura tiene su propósito. Elegir la adecuada según el contexto es clave para resolver problemas de forma eficiente.