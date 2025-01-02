# Buddy Strings

## Descripción

El ejercicio "Buddy Strings" consiste en determinar si es posible hacer dos cadenas de texto iguales al intercambiar únicamente dos caracteres en una de ellas. Las cadenas de texto contienen solo letras minúsculas, y la operación de intercambio de caracteres se realiza bajo la condición de que los índices de los caracteres a intercambiar sean diferentes.

Este tipo de problema está relacionado con la teoría de cadenas y la manipulación de caracteres en secuencias. Su resolución es útil en el campo de la edición de texto, encriptación simple y ciertas pruebas de integridad de datos.

## Implementación

La implementación se realiza en Python utilizando la clase `Solution`, que contiene el método `buddyStrings`. El método recibe dos cadenas de texto, `s` y `goal`, y determina si se pueden hacer iguales al intercambiar dos caracteres en `s`.

### Detalles de la implementación

1. **Verificación de longitud:** Primero se verifica si las dos cadenas tienen la misma longitud. Si no lo tienen, se retorna `False` inmediatamente.

2. **Detección de diferencias:** Se compara cada carácter en `s` con su correspondiente en `goal`. Los caracteres que no coinciden se almacenan en una lista. Si el número de diferencias es exactamente dos, se verifica si se puede obtener `goal` al intercambiar estos dos caracteres.

3. **Caso sin diferencias:** Si no hay diferencias en los caracteres de las cadenas, se verifica si hay al menos un carácter que se repita en ambas cadenas. Si algún carácter aparece dos o más veces, se puede realizar un intercambio de esos caracteres y el resultado será igual a `goal`.

## Conclusión

El ejercicio "Buddy Strings" resuelve el problema de determinar si dos cadenas de texto pueden convertirse en idénticas mediante el intercambio de solo dos caracteres. La implementación destaca el uso de listas para el manejo de caracteres y la clase Counter para contar las ocurrencias de los caracteres. Este enfoque es eficiente y directo, adecuado para problemas en los que se necesita comparar cadenas con un alto grado de flexibilidad, como en el manejo de textos y validaciones en software.
