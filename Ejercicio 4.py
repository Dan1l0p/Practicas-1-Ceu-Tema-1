##Durante la planificación de un proyecto se han acordado una lista de tareas. Para cada una de estas tareas se ha asignado un orden de prioridad (cuanto menor es el número de orden, más prioridad).##
##¿Eres capaz de crear una estructura del tipo cola con todas las tareas ordenadas pero sin los números de orden?##
##Para ordenar automáticamente una lista es posible utilizar el método .sort(), deberias probarlo.##

tareas = ["3: Jugar", "2: Comer", "4: Estudiar", "1: Dormir"]
tareas.sort()
for tarea in tareas:
    print(tarea)
