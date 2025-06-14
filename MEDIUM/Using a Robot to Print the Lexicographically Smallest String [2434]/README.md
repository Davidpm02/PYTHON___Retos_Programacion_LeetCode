# Using a Robot to Print the Lexicographically Smallest String

## Descripción

El ejercicio **"Using a Robot to Print the Lexicographically Smallest String"** plantea un problema de manipulación de cadenas en el que se dispone de una cadena `s` y un robot que inicialmente sostiene una cadena vacía `t`. Se deben realizar operaciones para transferir caracteres desde `s` a `t` y luego desde `t` a una cadena final escrita en papel, siguiendo reglas específicas.

Las operaciones posibles son:

1. Extraer el primer carácter de `s` y pasarlo al final de `t`.  
2. Extraer el último carácter de `t` y escribirlo en el papel.

El objetivo es obtener la cadena final escrita en papel que sea lexicográficamente la más pequeña posible tras realizar todas las operaciones hasta que ambas cadenas, `s` y `t`, queden vacías.

Este problema requiere una estrategia para decidir cuándo transferir caracteres de `s` a `t` y cuándo escribir caracteres desde `t` para garantizar que el resultado sea óptimo lexicográficamente.

## Implementación

La solución está implementada en Python mediante una clase `Solution` con el método `robotWithString`. Este método simula las dos operaciones mencionadas, usando estructuras auxiliares para controlar la lexicografía del resultado:

### Detalles de la implementación

- **Cálculo del menor carácter restante:**  
  Se crea un arreglo `min_suffix` que, para cada posición `i` en `s`, guarda el menor carácter lexicográfico desde `s[i]` hasta el final. Esto permite decidir si es seguro extraer un carácter desde `t` para escribirlo en el papel sin perder la oportunidad de obtener un resultado más pequeño.

- **Estructura temporal `t`:**  
  Se utiliza una lista como pila para simular la cadena temporal que el robot sostiene. Se añaden caracteres desde `s` a `t` y se extraen para escribir en la salida.

- **Algoritmo principal:**  
  - Se recorre `s` carácter a carácter, transfiriéndolo a `t`.  
  - Mientras el carácter en la cima de `t` sea menor o igual que el menor carácter restante en `s`, se extrae de `t` y se añade al resultado final `res`.  
  - Esto asegura que se escriben en orden los caracteres más pequeños posibles en cada paso, logrando la mínima lexicografía.

Este enfoque es eficiente, lineal en complejidad, y garantiza el resultado correcto utilizando el cálculo previo de los mínimos sufijos para guiar las decisiones.

## Uso

Para usar esta implementación, basta con crear una instancia de `Solution` y llamar al método `robotWithString` pasando la cadena de entrada `s`. El método devuelve la cadena lexicográficamente mínima que puede ser escrita en el papel siguiendo las reglas del problema.

```python
if __name__ == "__main__":
    s = "zza"

    sol = Solution()
    result = sol.robotWithString(s)
    print(result)  # Output: "azz"
```

## Conclusión

El ejercicio "Using a Robot to Print the Lexicographically Smallest String" ilustra una interesante problemática de manipulación de cadenas y optimización lexicográfica que puede modelarse con estructuras de datos simples y análisis previo de la cadena. La solución implementada aprovecha un preprocesamiento para conocer el carácter mínimo restante en cada punto y una pila para simular la cadena temporal del robot, logrando un algoritmo eficiente y elegante. Este ejercicio es útil para entender cómo anticipar condiciones futuras en algoritmos y tomar decisiones locales óptimas para obtener un resultado global óptimo.
