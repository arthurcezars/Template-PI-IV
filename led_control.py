import spidev
import ws2812

SPI = spidev.SpiDev()
SPI.open(0, 0)

QTD_LEDS = 15
CORES = []

def setColor(r, g, b):
    return [g, r, b]

def setFitaAllColor(r, g, b):
    return [setColor(r, g, b)] * QTD_LEDS

def setColorArray(arrayColor):
    executarFita(setFitaAllColor(arrayColor[0], arrayColor[1], arrayColor[2]))

def executarFita(comando):
    ws2812.write2812(SPI, comando)

def temperatura(arrecadacao):
    novo = setFitaAllColor(255, 255, 255)
    pos = 0
    print(arrecadacao)
    if arrecadacao == 0:
        print('entrei 0%')
        for x in range(3):
            novo[pos] = setColor(0, 255, 0)
            pos += 1
    if arrecadacao > 0:
        print('entrei maior que 0%')
        for x in range(5):
            novo[pos] = setColor(0, 255, 0)
            pos += 1
    if arrecadacao > 3:
        print('entrei maior que 3%')
        for x in range(3):
            novo[pos] = setColor(255, 102, 0)
            pos += 1
    if arrecadacao > 5:
        print('entrei maior que 5%')
        for x in range(2):
            novo[pos] = setColor(255, 102, 0)
            pos += 1
    if arrecadacao > 10:
        print('entrei maior que 10%')
        for x in range(3):
            novo[pos] = setColor(255, 0, 0)
            pos += 1
    if arrecadacao > 40:
        print('entrei maior que 40%')
        for x in range(2):
            novo[pos] = setColor(255, 0, 0)
            pos += 1
    return novo
