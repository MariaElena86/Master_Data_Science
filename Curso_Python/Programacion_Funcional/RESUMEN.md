# lambda
- Función anónima corta escrita en una sola línea
- La expresión se evalúa y retorna el resultado automáticamente.
- No necesita nombre
- Muy usada con map(), filter() y reduce()


### Sintaxis: 
``` python
lambda parametros: expresion
```
### Ejemplo 1:
``` python
# Elevar un número al cuadrado
# Donde:
# lambda  → indica una función anónima
# x       → parámetro de entrada
# x ** 2  → expresión que se evalúa y retorna

lambda x: x ** 2

# Equivale a:
def mifuncion(x):
    return x ** 2
```

### Ejemplo 2: 

``` python
# Multiplicar dos valores
# Donde:
# lambda  → indica una función anónima
# a y b → parámetros de entrada
# a * b → resultado retornado automáticamente

lambda a, b: a * b
# Equivale a:
def mifuncion(a, b):
    return a * b
```

# ----------------------------------------------------------

# map(fn, iterable) -- retorna todos los valores modificados
``` python
fn = lambda x: x*2
iterable = [1, 2, 3,4, 5]

listav1 = list(map(fn, iterable))
listav2 = list(map(lambda x: x*2, iterable))
print(listav2)
```
- map() aplica una función a cada elemento del iterable.
- Devuelve un nuevo iterable con los elementos transformados.
- Para convertir el resultado en una lista usamos list().

# ----------------------------------------------------------------

# filter(fn, iterable) -- retorna solo los valores que cumplen la condicion
``` python
fn = lambda x: x > 2
iterable = [1, 2, 3,4, 5]

listav1 = list(filter(fn, iterable))
listav2 = list(filter(lambda x: x > 2, iterable))
print(listav2)
```
- filter() recorre el iterable y evalúa cada elemento usando la función.
- Solo conserva los elementos para los que la función devuelve True.
- filter() retorna un objeto iterable de tipo filter.
- Para visualizar los resultados como lista, usamos list().


# ----------------------------------------------------------------

# reduce(fn, iterable) -- retorna un unico resultado
- Recorre el iterable acumulando el resultado parcial (acc) de cada operación hasta obtener un único valor final.
- La función recibe:
  - acc → acumulador (resultado parcial)
  - x   → elemento actual

## NOTA: 
- Cuando NO se proporciona un valor inicial, reduce() usa automáticamente el primer elemento del iterable como acumulador inicial (acc).
- Cuando se define acc, se usa reduce(fn, iterable, 0)

``` python
from functools import reduce

fn = lambda acc, x: acc + x
iterable = [1, 2, 3, 4, 5]

resultado = reduce(fn, iterable)
print(resultado)
```
### Proceso:
- acc = 1  → primer elemento
- x   = 2  → segundo elemento
- paso 1: acc = 1,  x = 2  → 1 + 2 = 3
- paso 2: acc = 3,  x = 3  → 3 + 3 = 6
- paso 3: acc = 6,  x = 4  → 6 + 4 = 10
- paso 4: acc = 10, x = 5  → 10 + 5 = 15
- Resultado final: 15
