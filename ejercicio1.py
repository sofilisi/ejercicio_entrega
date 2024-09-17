'''
nombre: Sofia
apellido: Lisi Azaldegui
---
Enunciado:
Parte A
Supongamos que está trabajando en desarrollar el programa de carga de una encuesta.
1 - Pedir al usuario que ingrese nombre y apellido del encuestado, guardarlo como string.
2 - Pedir al usuario que ingrese el salario mensual del encuestado y guardarla como entero.
3 - Pedir al usuario que ingrese la cantidad de horas trabajadas en la semana anterior por el
encuestado y guardarlo como entero. Validar que sea un valor entre 0 y 120
4 - Calcular el ingreso horario del encuestado (ingreso dividido por horas trabajadas) y
generar una respuesta por pantalla con todos los datos ingresados para verificar que estén
bien cargados.


'''
#> <
rta == "si"


    
while rta == "si":
    # Pedir nombre y apellido
    nombre_encuestado = input("Ingrese nombre y apellido del encuestado: ")
    
    # Pedir salario mensual
    salario_mensual = int(input("Ingrese el salario mensual: "))
    
    # Pedir cantidad de horas trabajadas con validación
    horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas en la semana anterior: "))
    while horas_trabajadas < 0 or horas_trabajadas > 120:
        horas_trabajadas = int(input("Cantidad de horas inválida. Reingrese la cantidad de horas trabajadas (debe estar entre 0 y 120): "))
    
    # Calcular ingreso horario
    ingreso_horario = salario_mensual / horas_trabajadas if horas_trabajadas > 0 else 0
    
    # Mostrar todos los datos
    print(f"\nNombre y Apellido: {nombre_encuestado}")
    print(f"Salario Mensual: {salario_mensual}")
    print(f"Cantidad de Horas Trabajadas: {horas_trabajadas}")
    print(f"Ingreso Horario: {ingreso_horario}")


    




