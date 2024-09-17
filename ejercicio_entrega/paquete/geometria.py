'''
nombre: Sofia
apellido: Lisi Azaldegui
---
Enunciado:
1- Elabore un módulo que contenga 3 funciones:
a- una función que calcule el área de un círculo. Utilizar parámetros opcionales para definir
que en caso de no recibir un radio el valor del mismo será 3.
b- una función que calcule el área de un cuadrado y reciba la longitud del lado como
parámetro, sin parámetros opcionales.
c- una función que calcule el área de un triángulo recibiendo base y altura por parámetro.
2- Elaborar un módulo que contenga 3 funciones. Pero este deberá calcular los perímetros
de las mismas figuras que el punto 1.
3- generar paquete.
4- subir a github.
'''
#> <

import math

def area_circulo(radio=3):

    "Calcula el área de un círculo con radio por defecto 3"
    return math.pi * radio ** 2

def area_cuadrado(lado):

    "Calcula el área de un cuadrado dado el largo del lado"
    return lado ** 2

def area_triangulo(base, altura):

    "Calcula el área de un triángulo dado su base y altura"
    return (base * altura) / 2