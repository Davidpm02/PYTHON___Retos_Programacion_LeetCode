# Maximum Difference by Remapping a Digit

## Descripción

El ejercicio "Maximum Difference by Remapping a Digit" consiste en calcular la diferencia máxima que se puede obtener al transformar exactamente un dígito del número original en otro distinto. Esta operación debe aplicarse a todas las apariciones del dígito elegido dentro del número, generando así una nueva versión que represente el valor máximo o mínimo posible.

Este tipo de problema es útil para trabajar habilidades relacionadas con el manejo de cadenas numéricas, la lógica condicional y la manipulación de cifras decimales en representación textual. Además, fomenta el pensamiento estratégico en cuanto a qué transformaciones convienen más para alcanzar los extremos deseados (mínimo y máximo).

## Implementación

La implementación se desarrolla en Python mediante una clase `Solution` que contiene el método `minMaxDifference`. Este método toma un número entero como entrada y retorna la diferencia entre el mayor y el menor número que pueden obtenerse al remapear uno de sus dígitos.

## Detalles de la implementación

- **Conversión a cadena:** Se convierte el número entero a cadena para facilitar el recorrido y reemplazo de sus dígitos.
- **Cálculo del valor máximo:** Se identifica el primer dígito distinto de 9 y se reemplaza por 9 en todas sus ocurrencias para generar el número máximo.
- **Cálculo del valor mínimo:** Se busca el primer dígito que pueda ser reemplazado por 0, sin causar ceros a la izquierda no permitidos, y se hace el reemplazo correspondiente.
- **Cálculo final:** Se convierte el resultado máximo y mínimo a enteros y se devuelve la diferencia entre ellos.

## Uso

Para utilizar este código, se debe crear una instancia de la clase `Solution` y llamar al método `minMaxDifference` con el número deseado como parámetro. El método retornará un entero que representa la diferencia entre el número máximo y el mínimo posibles.

```python
if __name__ == "__main__":
    num = 11891

    sol = Solution()
    result = sol.minMaxDifference(num)
    print(result)  # Output: 99009
```

## Conclusión

El ejercicio "Maximum Difference by Remapping a Digit" pone a prueba la capacidad de transformación de dígitos en un número con el objetivo de maximizar y minimizar su valor. Es una tarea interesante para practicar operaciones con cadenas y lógica de sustitución, además de ilustrar cómo pequeños cambios en la representación decimal pueden tener un gran impacto en el resultado final. La solución presentada hace un uso eficiente del recorrido y reemplazo de caracteres para alcanzar el objetivo planteado de forma clara y comprensible.
