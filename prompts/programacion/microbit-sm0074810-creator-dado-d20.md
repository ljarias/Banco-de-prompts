**Dado de rol (D20)**

**By:**

Samara Motta Guerrero

Programación 2

Santa Marta

IEDT INEM Simón Bolivar

11-7

**1\. Propósito**

Diseñar, probar y documentar un prompt capaz de solicitar a una Inteligencia Artificial la generación de un miniprograma en MicroPython para la BBC micro:bit. El programa simula un dado de 20 caras (D20) para juegos de rol, activado mediante el sensor acelerómetro al agitar la placa, incorporando animaciones de carga, lógica condicional para aciertos y fallos críticos, y un ciclo de interacción continuo.

**2\. Prompt Final Adaptado**

Este es el prompt final configurado con todos los componentes requeridos:

Soy estudiante de grado 11 y estoy aprendiendo Programación 2.

Necesito crear un miniprograma en MicroPython para una BBC micro:bit.

**Objetivo del programa:** Simular un dado de 20 caras (D20). Al agitar la placa, genera un número aleatorio del 1 al 20, muestra una animación de carga y despliega el resultado, con reacciones especiales si sale un 20 (icono feliz) o un 1 (calavera).

**Entrada o evento:** Gesto de agitar (accelerometer.was_gesture('shake')).

**Salida esperada:** Animación breve en la matriz LED con Image.DIAMOND, número aleatorio en pantalla usando display.scroll() y símbolos especiales para los valores críticos.

**Requisitos:**

- usa una solución sencilla.
- organiza el programa con al menos una función.
- usa condicionales y un ciclo cuando corresponda.
- no uses librerías externas no autorizadas.
- comente solo lo necesario.
- explica brevemente cómo funciona.
- incluye pasos de prueba.
- señala dos errores comunes que debería revisar.

Antes de entregar el código, comprueba que la propuesta sea coherente con MicroPython para micro:bit.