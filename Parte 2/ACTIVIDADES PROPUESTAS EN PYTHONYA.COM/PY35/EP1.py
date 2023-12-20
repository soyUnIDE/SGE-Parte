# La funcion cargar crea una lista de alumnos en los cuales tienen de identificador el dni y como valor tiene una lista con dos valores el nombre de la materia y la nota
def cargar():
    alumnos={}
    for i in range(3):
        dni= int(input("Ingrese el numero de dni: "))
        listaMaterias=[]
        continua="s"
        while continua=="s":
            materia=input("Ingrese el numero de materia")
            nota=int(input("Ingrese la nota: "))
            listaMaterias.append((materia,nota))
            continua=input("Desea cargar otra materia para dicho alumno [s/n]: ")
        alumnos[dni]=listaMaterias
    return alumnos

# La funcion listar muestra por pantalla el dni de los alumnos, las materias y las notas
def listar(alumnos):
    print("Listado completo de alumnos y sus notas por materia")
    for dni in alumnos:
        print(f"DNI del alumno {dni}")
        print("Materia que cursa y notas")
        for materia,nota in alumnos[dni]:
            print(materia,nota)

# La funcion consulta_notas consulta en la lista pasada por parametro si existe el dni introducido y si existe muestra sus asignaturas y sus notas
def consulta_notas(alumnos):
    dni=int(input("Ingrese el numero a consultar: "))
    if dni in alumnos:
        for materia,nota in alumnos[dni]:
            print(materia,nota)

alumnos=cargar()
listar(alumnos)
consulta_notas(alumnos)