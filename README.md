# Fábrica de Recipientes de Vidrio - Problema de Scheduling
---
  - Grisel Porras Franco A00830414
  - Joaquin Bravo Garcia A00830409
  - David Basilio Rodriguez Cortez A00830940
---

## Descripción del proceso de producción.	

Se define el proceso de producción en una fábrica de recipientes de vidrio, donde los ingredientes se funden en un horno para obtener cristal líquido y posteriormente se vierte la masa del líquido del cristal dentro del molde con la forma del recipiente. El problema de scheduling en esta fábrica implica coordinar de manera óptima las tareas de producción para maximizar la eficiencia, minimizar el tiempo de producción y reducir costos.
	
## Layout del Proceso

El layout del proceso en la fábrica de recipientes de vidrio es un sistema de flow shop flexible. Esto implica que hay múltiples máquinas en paralelo para ciertas etapas y las tareas deben seguir una secuencia específica. En este caso, el proceso consta de las siguientes etapas:

## Etapas

El proceso de producción está compuesto por tres etapas principales:
Vidrio templado: En esta etapa, el vidrio se templa mediante un proceso de calentamiento y enfriamiento controlado para aumentar su resistencia.
Fundición: Aquí, el vidrio templado se funde en hornos especiales hasta obtener una masa líquida homogénea.
Moldeado: El vidrio líquido se vierte en moldes específicos para darle forma a los recipientes. Esta etapa se realiza en varias máquinas en paralelo.

## Reglas de Decisión

Para la toma de decisiones en el scheduling, se consideran las siguientes reglas:

1. Capacidad de las máquinas: Considerar la capacidad y disponibilidad de las máquinas para cada etapa.
2. Secuencia de operaciones: Asegurar que la secuencia Vidrio templado -> Fundición -> Moldeado se siga estrictamente.
3. Minimización de tiempos de setup: Optimizar el tiempo de configuración entre tareas para reducir el tiempo de inactividad de las máquinas.

## Instrucciones de Ejecución
El programa se ejecuta desde el archivo [main.py](main.py).

## Librerías Requeridas
Las librerías necesarias para ejecutar el programa se encuentran en el archivo requirements.txt.
