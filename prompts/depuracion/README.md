# 🕵️ Prompts para depuración

Aquí la IA debe ayudarte a **encontrar** el error, no solamente a esconderlo con una solución nueva.

## 1. Detective de errores

> Actúa como entrenador de depuración. Este es mi código y el error que obtengo: [CÓDIGO Y ERROR]. Primero explica qué significa el mensaje de error. Después dame tres pistas, de la más general a la más específica. No muestres el código corregido hasta después de las pistas. Cuando lo hagas, explica qué causaba el problema y cómo puedo detectarlo más rápido la próxima vez.

## 2. Cuando el programa corre pero da un resultado incorrecto

> Mi programa se ejecuta sin errores, pero el resultado no es el esperado. Resultado esperado: [ESPERADO]. Resultado obtenido: [OBTENIDO]. Código: [CÓDIGO]. Ayúdame a seguir los valores de las variables paso a paso. Identifica el primer punto donde el estado del programa deja de coincidir con lo esperado. No reescribas todo el programa.

## 3. Diseñar casos de prueba

> Analiza esta función: [FUNCIÓN]. Crea casos de prueba para valores normales, límites y entradas problemáticas. Para cada caso indica la entrada y el resultado esperado. No cambies mi función todavía; quiero usar las pruebas para descubrir qué falla.
