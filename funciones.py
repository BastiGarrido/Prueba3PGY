import numpy
import msvcrt
import os
import random

COLEGIO = numpy.empty([5,8], object)

def LimpiarPantalla():
    print("<< Presione una tecla >>")
    msvcrt.getch()
    os.system('cls')

def VerificarRut(RUT):
    if RUT == None:
        return True
    else:
        print("Rut repetido.")
        return False

def VerificarNombreCompleto(NOMBRE_COMPLETO):
    if len(NOMBRE_COMPLETO) >= 2 and len(NOMBRE_COMPLETO) <= 30:
        return True
    else:
        print("Nombre completo no válido.")
        return False

def VerificarEdad(EDAD):
    if EDAD >= 4:
        return True
    else:
        print("Edad no válida.")
        return False
    
def VerificarGenero(GENERO):
    if GENERO == "F" or GENERO == "M":
        return True
    else:
        print("Género no válido.")

def Registro(NOMBRE_COMPLETO,RUT,EDAD,GENERO,PROMEDIO_NOTAS,FECHA_MATRICULA,APODERADO):
    if None in COLEGIO:
        if VerificarRut == True:
            if VerificarNombreCompleto == True:
                if VerificarEdad == True:
                    if VerificarGenero == True:
                        if COLEGIO[i,0] == None:
                            for i in range(COLEGIO[i,0]):
                                COLEGIO[0,0] = RUT
                                COLEGIO[1,0] = NOMBRE_COMPLETO
                                COLEGIO[2,0] = EDAD
                                COLEGIO[3,0] = GENERO
                                COLEGIO[4,0] = PROMEDIO_NOTAS
                                COLEGIO[5,0] = FECHA_MATRICULA
                                COLEGIO[6,0] = APODERADO
                                print("Se registró con exito.")

def Buscar(RUT):
        if COLEGIO[0,0] is not None == RUT:
            print(f"""
            Rut:{COLEGIO[0,0]}
            Nombre Completo del alumno: {COLEGIO[1,0]}
            Edad: {COLEGIO[2,0]} años.
            Género: {COLEGIO[3,0]}.
            Promedio de notas: {COLEGIO[4,0]}.
            Fecha de matricula: {COLEGIO[5,0]}.
            Nombre del apoderado: {COLEGIO[6,0]}.
            """)

def Imprimir():
    ANOTACIONES = random.randint(0,50)
    CERTIFICADOS = random.randint(0,50)
    ALUMNO_REG = random.randint(0,50)
    print("-----------------------")
    print("ANOTACIONES DEL ALUMNO")
    print("-----------------------")
    print(f"RUT: {COLEGIO[0,0]}")
    print(f"NOMBRE: {COLEGIO[1,0]}")
    print(f"ANOTACIONES: {ANOTACIONES}")
    print("-----------------------")
    print("-----------------------")
    print("CERTIFICADO DE NOTAS")
    print("-----------------------")
    print(f"RUT: {COLEGIO[0,0]}")
    print(f"NOMBRE: {COLEGIO[1,0]}")
    print(f"ANOTACIONES: {CERTIFICADOS}")
    print("-----------------------")
    print("-----------------------")
    print("CERTIFICADO ALUMNO REGULAR")
    print("-----------------------")
    print(f"RUT: {COLEGIO[0,0]}")
    print(f"NOMBRE: {COLEGIO[1,0]}")
    print(f"ANOTACIONES: {ALUMNO_REG}")
    print("-----------------------")

