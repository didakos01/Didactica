#este es un programita para física
import math as m

v_ini = float(input("Ingrese velocidad inicial: "))
time = float(input("Ingrese el tiempo: "))
acel = float(input("Ingrese la aceleración: "))
#programa marca ACME

dist = v_ini*time+0.5*acel*time*time

print("La distancia es: ", dist)

#calcular área del círculo
radius = float(input("Ingrese el radio: "))
area_circ = m.pi*m.pow(radius,2)
print("El área es:", area_circ)
