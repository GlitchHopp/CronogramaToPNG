#!/usr/bin/env python

from __future__ import print_function, division
# from wand.color import Color
# from wand.drawing import Drawing
# from wand.image import Image
from PIL import Image, ImageDraw, ImageFont
import math
import sys

def calculaEspaciosDeTiempo():
    nextLineIsTimeValues = False
    timeValuesLine = False
    numbers = []    
    
    
    for l in lineas:
        
        splitted = l.split("   ")
        # print(splitted)
        for s in splitted:
            if ("|___|" in s):
                nextLineIsTimeValues = True

        # splitted.remove(' ')
        if timeValuesLine == True: 
            for x in splitted:
                numero = x.split(' ')
                for n in numero:
                    n = n.replace('\n', '')
                    if (str(n) != '') and (str(n) !=' '):
                        if str(n) == '0':
                            indexZero = l.find('0')
                        # print(n)
                        numbers.append(n)                 
            nextLineIsTimeValues = False
            timeValuesLine = False
            lastNumber = numbers[len(numbers)-1]
            espaciosDeTiempo = int(lastNumber)
            
        if nextLineIsTimeValues == True:
            timeValuesLine = True
        # print(timeValuesLine)
        # print(nextLineIsTimeValues)
    return espaciosDeTiempo, indexZero
          

def obtieneDatosProcesos(timeIntervals, indexZero):
    i = 0
    for l in lineas:
        splitted = l.split(' ')
        for s in splitted:
            if s.startswith("p") or s.startswith('P'):
                procesos.append(i)
                nombres.append(s)
                break
            else:
                if s != '':
                    break
        i = i+1

    for i in range(0,len(procesos)):
        line = lineas[procesos[i]]
        for c in range(indexZero, len(line)-1):
            if line[c] == 'B':
                bloqueos.append((procesos[i], c))
            if line[c] == '<':
                comienzos.append((procesos[i], c))
            if line[c] == '>':
                finales.append((procesos[i], c))
            if line[c] == 'P' or line[c] == 'X':
                planificador.append((procesos[i], c))
            if line[c] == '-':
                uso.append((procesos[i], c))
    

def dibuja(espaciosDeTiempo):
           
    fnt = ImageFont.truetype('HelveticaNeueLTStd-Bd.otf', 20)
    img=Image.open('plantilla.png')
    draw = ImageDraw.Draw(img)
    uwu = 0
    drawThisLine = True

    for i in range(0, len(uso)):
        c = uso[i]
        c2 = c[1]
        if (c2 - indiceCero)%4 == 0:
            drawThisLine = False
        c1 = procesos.index(c[0]) + 1
        
        x1= ((c2-indiceCero)/4)*(810/espaciosDeTiempo)+79
        x2= ((c2-indiceCero)/4)*(810/espaciosDeTiempo)+103
        y= 89 + c1*(340/(len(procesos)+1))
        if (i-1)>=0:
            lastOne = uso[i-1]
            if lastOne[0] != c[0]:
                uwu = uwu+1
                uwu = uwu%6
        # draw.line((90+ (i)*(810/espaciosDeTiempo), 80, 90+ (i)*(810/espaciosDeTiempo), 420), fill=128, width=2)
        if drawThisLine != False:
            draw.line((x1, y, x2, y), fill=col[uwu], width = 3)
        drawThisLine = True

    
    for i in range(0, len(planificador)):
        c = planificador[i]
        # print(c)
        c1 = procesos.index(c[0]) + 1
        c2 = c[1]
        x= ((c2-indiceCero)/4)*(810/espaciosDeTiempo)+84
        y= 82 + c1*(340/(len(procesos)+1))
        draw.text((x, y), 'X', font=fnt, fill=(0,0,0,255))

    for i in range(0, len(nombres)):
        x= 30
        y= 80 + (1+i)*(340/(len(nombres)+1))
        if nombres[i] == 'Planificador' or nombres[i] == 'planificador':
            nombres[i] = 'Planif.'            
            x = 15
            draw.text((x, y), nombres[i], font=fnt, fill=(0,0,0,255))            
        else:
            draw.text((x, y), nombres[i], font=fnt, fill=(0,0,0,255))

    for i in range(0, len(comienzos)):
        c = comienzos[i]
        c1 = procesos.index(c[0]) + 1
        c2 = c[1]
        x= ((c2-indiceCero)/4)*(810/espaciosDeTiempo)+86
        y= 75 + c1*(340/(len(procesos)+1))
        fnt = ImageFont.truetype('HelveticaNeueLTStd-Bd.otf', 30)
        draw.text((x, y), '<', font=fnt, fill=(0,0,0,255))
        fnt = ImageFont.truetype('HelveticaNeueLTStd-Bd.otf', 20)
        
    for i in range(0, len(finales)):
        c = finales[i]
        c1 = procesos.index(c[0]) + 1
        c2 = c[1]
        x= ((c2-indiceCero)/4)*(810/espaciosDeTiempo)+80
        y= 75 + c1*(340/(len(procesos)+1))
        fnt = ImageFont.truetype('HelveticaNeueLTStd-Bd.otf', 30)
        draw.text((x, y), '>', font=fnt, fill=(0,0,0,255))
        fnt = ImageFont.truetype('HelveticaNeueLTStd-Bd.otf', 20)

    draw.line((90, 80, 90, 420), fill=(0,0,0,255), width=3)
    draw.line((90, 420, 900, 420), fill=(0,0,0,255), width=3)
    for i in range(1, espaciosDeTiempo+1):
        draw.line((90+ (i)*(810/espaciosDeTiempo), 80, 90+ (i)*(810/espaciosDeTiempo), 420), fill=(0,0,0,255), width=2)
        draw.text((84+ (i)*(810/espaciosDeTiempo), 440), str(i), font=fnt, fill=(0,0,0,255))

    for i in range(0, len(bloqueos)):
        b = bloqueos[i]
        b1 = procesos.index(b[0]) + 1
        b2 = b[1]
        x= ((b2-indiceCero)/4)*(810/espaciosDeTiempo)+75
        y= 71 + b1*(340/(len(procesos)+1))
        # fnt = ImageFont.truetype('HelveticaNeueLTStd-Bd.otf', 28)        
        # draw.text((x+3, y), 'B', font=fnt, fill=(255,255,255,255))
        draw.text((x, y), 'B', font=fnt, fill=(0,0,0,255))
        fnt = ImageFont.truetype('HelveticaNeueLTStd-Bd.otf', 20)

    del draw
    path = r'./final.png'
    img.save(path, "PNG")

try:
    sys.argv[1]
except IndexError:
    print ('No has incluido argumentos')
else:
    nombrearchivo = sys.argv[1]
    if sys.argv[1].endswith('.txt'):
        
        archivo = open(nombrearchivo, "r")
        lineas = archivo.readlines()
        procesos = []
        nombres = []
        bloqueos = []
        comienzos = []
        finales = []
        planificador = []
        uso = []
        col = ((231, 35, 0, 255), (80, 124, 215, 255), (120, 200, 2, 255), (231, 124, 0, 255), (231, 124, 215, 255), (144, 87, 55))
        indiceCero = 0        
        timeIntervals, indiceCero = calculaEspaciosDeTiempo()
        obtieneDatosProcesos(timeIntervals, indiceCero)
        # print(procesos)
        # print(bloqueos)
        # print(comienzos)
        # print(finales)
        # print(planificador)
        # print(nombres)
        # print(timeIntervals)
        # print(indiceCero)
        dibuja(timeIntervals)

    else:
        print ('Debes introducir un archivo de texto')