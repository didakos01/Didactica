//ALGORITMO DE EJEMPLO, CONDICIONALES ANIDADAS
Algoritmo condicionales_anidadas
	Escribir "Ingrese su edad: "
	Leer edad
	Escribir "Ingrese su promedio: "
	Leer promedio
	Escribir "¿Hace deporte? 1=Sí, 0=No"
	Leer hace_deporte
	
	Si edad>=15 y edad<=20 Entonces
		Si promedio>=80 y promedio<=100 Entonces
			Escribir "Acredita la beca"
		SiNo
			Escribir "No hay beca"
		FinSi
	SiNo
		Si promedio>=90 o hace_deporte==1 Entonces
			Escribir "Acredita beca especial"
		SiNo
			Escribir "No hay beca"
		FinSi
	FinSi
FinAlgoritmo