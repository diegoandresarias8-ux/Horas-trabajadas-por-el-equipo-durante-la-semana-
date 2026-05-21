# Diego Andres Arias Infante 
# Problema 5
# Horas trabajadas por el equipo durante la semana 

# funcion para calcular el total de horas y su clasificación 
def calcular_horas(horas) :
    total = sum(horas)
    
    if total > 40:
        clasificación = "Sobretiempo"
    else:
        clasificación = "Horario Estandar"
        
    return total, clasificación

# Matriz de recursos 
# [Nombre, Lunes, Martes, Miercoles, Jueves, Viernes]

recursos = [
    ["Ana", 8,8,8,8,9],
    ["carlos", 7,8,8,7,8],
    ["Luisa", 9,9,9,8,9],
    ["pedro", 8,8,8,8,8]
]

# Mostras resultados 

print("REPORTE DE HORAS SEMANALES\n")

for recurso in recursos:
    nombre = recurso[0]
    horas = recurso[1:]
    
    total, clasificación = calcular_horas(horas)
    
    print("Recurso:", nombre)
    print("Total de horas:", total)
    print("Clasificación:", clasificación)
    print("___________________________")
    