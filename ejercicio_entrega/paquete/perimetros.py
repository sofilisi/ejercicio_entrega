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

def perimetro_circulo(radio=3):

    "Calcula el perímetro de un círculo con radio por defecto 3"
    return 2 * math.pi * radio

def perimetro_cuadrado(lado):
    
    "Calcula el perímetro de un cuadrado dado el largo del lado"
    return 4 * lado

def perimetro_triangulo(lado1, lado2, lado3):

    "Calcula el perímetro de un triángulo dado el largo de sus tres lados"
    return lado1 + lado2 + lado3