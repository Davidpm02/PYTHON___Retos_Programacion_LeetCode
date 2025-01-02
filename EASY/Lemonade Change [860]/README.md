# Lemonade Change

## Descripción

El ejercicio "Lemonade Change" consiste en verificar si un puesto de limonadas es capaz de dar el cambio correcto a cada cliente en una fila de compra. Cada cliente paga con un billete de $5, $10 o $20, y el precio de un vaso de limonada es de $5. El desafío consiste en determinar si, al inicio del día (cuando no se tiene cambio), se puede proporcionar el cambio correcto a todos los clientes en la secuencia dada de pagos.

Este tipo de problema está relacionado con la lógica de transacciones y la administración de efectivo en procesos comerciales, muy común en situaciones que requieren mantener y verificar inventarios o disponibilidades de moneda en tiempo real.

## Implementación

La implementación se realiza en Python utilizando la clase `Solution`, que contiene el método `lemonadeChange`. Este método recibe una lista de enteros `bills`, representando los pagos de cada cliente. A medida que se recorre la lista de pagos, el algoritmo verifica si el puesto de limonadas puede proporcionar el cambio adecuado en cada caso.

### Detalles de la implementación

1. **Diccionario de billetes:** Se crea un diccionario `bills_cash_dict` que mapea los billetes de $5, $10 y $20, y lleva un conteo de cuántos de estos billetes se han recibido.

2. **Verificación de pagos:** A medida que el algoritmo recorre la lista de pagos:
    - Si el cliente paga con $5, no es necesario dar cambio, se incrementa el contador de billetes de $5.
    - Si el cliente paga con $10, se debe dar un cambio de $5. Si no hay suficientes billetes de $5, se retorna `False`.
    - Si el cliente paga con $20, se deben proporcionar $15 de cambio. Si es posible proporcionar el cambio con la combinación de billetes disponibles, se ajustan los contadores apropiadamente. Si no, se retorna `False`.

3. **Resultado final:** Si el recorrido de los pagos termina sin problemas y siempre se proporciona el cambio adecuado, se retorna `True`. De lo contrario, se retorna `False`.

## Conclusión

El ejercicio "Lemonade Change" proporciona una solución eficiente y práctica para determinar si un puesto de limonadas puede dar el cambio adecuado a sus clientes con los billetes que recibe. Utilizando un diccionario para el seguimiento de los billetes y realizando verificaciones rápidas de los pagos, se asegura que cada cliente reciba el cambio correcto de manera continua. Este tipo de problemas es útil en aplicaciones que involucran transacciones o puntos de venta, donde la administración correcta del flujo de dinero es crucial para el funcionamiento correcto del sistema.
