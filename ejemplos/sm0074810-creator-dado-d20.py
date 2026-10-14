from microbit import *
import random


def tirar_dado():
  # Animación de carga usando diamantes
  display.show([Image.DIAMOND, Image.DIAMOND_SMALL])
  sleep(400)
  display.clear()

  # Genera un número aleatorio del 1 al 20
  resultado = random.randint(1, 20)

  # Reacciones especiales para valores críticos
  if resultado == 20:
    display.show(Image.HAPPY)
    sleep(1000)
  elif resultado == 1:
    display.show(Image.SKULL)
    sleep(1000)

  # Muestra el número final
  display.scroll(str(resultado))


# Bucle principal que detecta el gesto de agitar
while True:
  if accelerometer.was_gesture("shake"):
    tirar_dado()
  sleep(100)
