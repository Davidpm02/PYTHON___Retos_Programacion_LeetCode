# Student Attendance Record I

## Descripción

El ejercicio "Student Attendance Record I" consiste en determinar si un estudiante es elegible para recibir un premio de asistencia basado en su historial. El historial se representa como una cadena de caracteres donde cada carácter indica el estado de asistencia en un día:

- `'A'`: Ausente.
- `'L'`: Tarde.
- `'P'`: Presente.

Para que un estudiante sea elegible para el premio, debe cumplir con las siguientes condiciones:

1. Haber estado ausente (`'A'`) en **menos de 2 días** en total.
2. No haber llegado tarde (`'L'`) en **3 o más días consecutivos**.

El método devuelve `true` si el estudiante cumple con los criterios y `false` en caso contrario.

## Implementación

La solución se implementa en Python dentro de la clase Solution, que contiene el método checkRecord. Este método utiliza un enfoque combinado para contar ausencias y verificar llegadas tarde consecutivas.

### Detalles de la implementación

1. Conteo de ausencias: Se utiliza Counter del módulo collections para contar las ocurrencias de 'A' en la cadena. Si el número de ausencias es mayor o igual a 2, el estudiante no es elegible.
2. Verificación de llegadas tarde consecutivas: Se utiliza un contador para rastrear secuencias consecutivas de 'L'. Si este contador alcanza 3 en cualquier punto, el estudiante no es elegible.
3. Retorno del resultado: Si ambas condiciones son satisfactorias, se devuelve true; de lo contrario, false.

## Uso

Para utilizar este código, se debe instanciar la clase Solution y llamar al método checkRecord con el historial de asistencia del estudiante como argumento.

```python
if __name__ == "__main__":
    s = "PPALLP"  # Historial de asistencia

    sol = Solution()
    result = sol.checkRecord(s)
    print(result)  # Output: True
```

En este ejemplo, el estudiante cumple con los criterios para recibir el premio, ya que no tiene 2 ausencias ni llegó tarde 3 días consecutivos.

## Conclusión

El ejercicio "Student Attendance Record I" es una práctica útil para trabajar con cadenas de texto y condiciones lógicas. La implementación presentada utiliza herramientas como el módulo collections y estructuras de control iterativas para abordar eficientemente el problema. Este tipo de ejercicios es ideal para reforzar conceptos básicos de programación y procesamiento de cadenas en Python.
