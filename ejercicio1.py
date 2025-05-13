#Caso 1: Control de venta de vigorón en feria universitaria UAM

cliente_atendido =  int(input("Ingres la cantidad de clinetes atendidos: "))
total_ventas =  0

for cliente in range(cliente_atendido):
    print(f"\n Cliente {cliente + 1}:")
    
    porciones =  int(input(f"Cuantas porciones de vigoron compro: "))
    
    total_cliente = 0
    
    for porcion in range(porciones):
        precio_unitario = float(input(f"Ingrese el precio de la porcion #{porcion}: "))
        total_cliente += precio_unitario
        
    print (f"Total a pagar por el cliente {cliente}: C${total_cliente:.2f}")
    
    total_ventas += total_cliente
    
print(f"\nTotal ventas en toda la feria: C${total_ventas:.2f}")