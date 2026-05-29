#este es un programita para física
v_ini = float(input("Ingrese velocidad inicial: "))
time = float(input("Ingrese el tiempo: "))
acel = float(input("Ingrese la aceleración: "))
#programa marca ACME

dist = v_ini*time+0.5*acel*time*time

print("La distancia es: ", dist)
