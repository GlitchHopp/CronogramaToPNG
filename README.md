# CronogramaToPNG
Script de python que convierte un archivo de texto con un cronograma hecho de caracteres ASCII a una gráfica en PNG 

Requiere Pillow. Para instalar Pillow:
python3 -m pip install Pillow

Para ejecutarlo:
python3 script.py cronograma_ejemplo.txt
(Sustituyendo cronograma_ejemplo por la ruta del archivo de texto a convertir)

Requisitos de los cronogramas a convertir:

-El cronograma tiene que ser legible en fuentes monospace.

-Tiene que tener los instantes de tiempo marcados en la linea inmediatamente inferior a la que lleva las barras bajas. De lo contrario, la funcion "calculaEspaciosDeTiempo" no funcionará

-Todos los procesos escritos a la izquierda de la gráfica tienen que empezar con p (por ejemplo p1, Pa, P2...)
    
-Los bloqueos tienen que marcarse con una 'B', y las intervenciones del planificador con una 'P' o una 'X', lo comienzos de proceso con un '<' y los finales con un '>', y el uso del procesador se marcará con '-'
    
