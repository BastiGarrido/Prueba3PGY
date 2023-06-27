import funciones 

while True:
    funciones.LimpiarPantalla
    print("""
    -------------------------------
    REGISTRO ESTUDIANTIL.
    -------------------------------
    1) Registrar.
    2) Buscar.
    3) Imprimir certificados.
    0) Salir.
    -------------------------------
    """)
    OPCION = int(input("Seleccione una opción: "))

    if OPCION == 0:
        print("""
        Vuelva pronto.
        Bastian Garrido.
        [Versión 1.0]
        """)
        break
    elif OPCION == 1:
        print("""
        ---------------------
             REGISTRO.
        ---------------------
        """)
        RUT = int(input("Escriba el rut del alumno: "))
        NOMBRE_COMPLETO = input("Ingrese nombre del alumno y apellido del alumno: ").capitalize()
        EDAD = int(input("Ingrese edad del alumno: "))
        GENERO = input("Ingrese género (F/M): ").upper()
        PROMEDIO_NOTAS = int(input("Ingrese promedio de notas: "))
        print("Ingrese fecha de matricula.")
        print("----------------------------")
        DIA = int(input("Ingrese el día: "))
        MES = int(input("Ingrese el mes: "))
        ANIO = int(input("Ingrese el año: "))
        FECHA_MATRICULA = (f"{DIA}/{MES}/{ANIO}.")
        APODERADO = input("Ingrese el nombre del apoderado: ").capitalize()
        funciones.Registro(RUT,NOMBRE_COMPLETO,EDAD,GENERO,PROMEDIO_NOTAS,FECHA_MATRICULA,APODERADO)
    elif OPCION == 2:
        print("""
        ---------------------
              BUSCAR.
        ---------------------
        """)
        RUT = int(input("Ingrese el rut del alumno: "))
        funciones.Buscar(RUT)

    elif OPCION == 3:
        print("""
        ----------------------
        IMPRIMIR CERTIFICADOS.
        ----------------------
        """)
        RUT = int(int("Ingrese el rut del alumno: "))
        funciones.Imprimir
    else:
        print("Opción no válida.")