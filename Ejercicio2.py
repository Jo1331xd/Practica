#Registro semanal de gastos de estudiantes de la UAM
# Se requiere un programa que permita controlar el registro semanal de gastos de estudiantes de la UAM.
# El programa debe permitir ingresar el nombre del estudiante, la cantidad de gastos que desea registrar y el precio por gasto. 
# Registro semanal de gastos de estudiantes UAM
# Se procesan datos de 4 semanas con gastos diarios.

semanas = 4
dias_por_semana = 7

total_mensual = 0

for semana in range(1, semanas + 1):
    print(f"\nSemana {semana}:")
    
    total_semana = 0
    
    for dia in range(1, dias_por_semana + 1):
        gasto_dia = float(input(f"Ingrese el gasto del día {dia}: "))
        total_semana += gasto_dia  # Se acumulan los gastos de la semana
    
    print(f"Total gastado en la semana {semana}: {total_semana:.2f}")
    
    total_mensual += total_semana  # Se acumulan los gastos del mes

print(f"\nTotal gastado en el mes: {total_mensual:.2f}")