#programita de física
import math

v_ini = float(input("Ingrese v. inicial (m/s): "))
time = float(input("Ingrese tiempo (s): "))
acel = float(input("Ingrese aceleración (m/s2): "))
dist = v_ini*time+0.5*acel*math.pow(time, 2)
print("La distancia es:", dist, "metros")
