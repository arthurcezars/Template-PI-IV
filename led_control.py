# Programa: Led enderecavel Neopixel com Raspberry Pi
# Adaptacoes: Arduino e Cia
# Baseado no programa exemplo da Adafruit

import time
import board
import neopixel
import RPi.GPIO as GPIO

# Pino de conexao Raspberry
# (podem ser utilizados os pinos 10, 12, 18 ou 21)
pixel_pin = board.D18

# Numero de leds que serao controlados
num_pixels = 15

# Ordem dos pixels de cor - RGB ou GRB
# Em alguns módulos as cores verde e vermelha estao invertidas
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, auto_write=False,
                           pixel_order=ORDER)


def wheel(pos):
    # Utiliza um valor entre 0 e 255 para definir a cor
    # As cores sao uma transicao r - g - b
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER == neopixel.RGB or ORDER == neopixel.GRB else (r, g, b, 0)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

def temperatura(arrecadacao):
    try:
        pixels.fill((0, 0, 0))
        pixels.show()
        while True:
            print(arrecadacao)
            if arrecadacao < 1000000:
                for i in 5:
                    pixels[i] = (0, 255, 0)
            elif arrecadacao > 1000000 and arrecadacao < 1000000000:
                for i in 10:
                    if i <= 4:
                        pixels[i] = (0, 255, 0)
                    else:
                        pixels[i] = (255, 255, 0)
            else:
                for i in 15:
                    if i <= 4:
                        pixels[i] = (0, 255, 0)
                    elif i <= 9:
                        pixels[i] = (255, 255, 0)
                    else:
                        pixels[i] = (255, 0, 0)
            pixels.show()

    except KeyboardInterrupt:
        # Apaga todos os leds
        pixels.fill((0, 0, 0))
        pixels.show()
        GPIO.cleanup()

try:
    while True:
        # Desabilite esta linha se for usar Neopixel RGBW/GRBW
        pixels.fill((255, 0, 0))
        # Habilite esta linha se for usar Neopixel RGBW/GRBW
        # pixels.fill((255, 0, 0, 0))
        pixels.show()
        time.sleep(1)
        # Desabilite esta linha se for usar Neopixel RGBW/GRBW
        pixels.fill((0, 255, 0))
        # Habilite esta linha se for usar Neopixel RGBW/GRBW
        # pixels.fill((0, 255, 0, 0))
        pixels.show()
        time.sleep(1)
        # Desabilite esta linha se for usar Neopixel RGBW/GRBW
        pixels.fill((0, 0, 255))
        # Habilite esta linha se for usar Neopixel RGBW/GRBW
        # pixels.fill((0, 0, 255, 0))
        pixels.show()
        time.sleep(1)

        # Efeito arco-iris com ciclo de 1ms por passo
        rainbow_cycle(0.001)

except KeyboardInterrupt:
    # Apaga todos os leds
    pixels.fill((0, 0, 0))
    pixels.show()
    GPIO.cleanup()