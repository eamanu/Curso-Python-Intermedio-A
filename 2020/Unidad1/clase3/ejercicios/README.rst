Ejercicio
=========


Crear una clase Processor, que ejecuta un script (implementar si se quiere) y que tenga cómo mínimo, una variable `status` y `name`, que guarde el estado de un proceso: "waiting", "running" o "finished". A cada proceso yo puedo definir los datos que quiera, es decir que no estén predefinidos.

Los precesos son gestionados por un Manager, dónde yo puedo agregar cada a proceso a la lista de procesos con un `+` y eliminarlos con un `-`. Cambiar el estado con usando `>` por ejemplo `Proceso1 > waiting`. 

Solo agregar a la lista  Procesos que no existan. Y si se trata de ejecutar un proceso que no existe lanzar una exception. 

Si yo hago `len(Manager)` quiero saber la cantidad de procesos.

\+ lo que quieran
