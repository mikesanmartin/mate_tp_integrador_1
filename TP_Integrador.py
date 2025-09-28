# TP Integrador 1
# Alumno: Michel Emmanuel San Martin

# Imports necesarios
from utils import convertir_a_booleano
from operaciones import operaciones_booleanas

# Solicito informacion por pantalla al usuario
primer_numero = input("Por favor ingrese un valor de verdad, recuerde que 0 es Falso y 1 es Verdadero:")

while primer_numero != "0" and primer_numero != "1":
    primer_numero = input("El valor ingresado no es valido, por favor intente nuevamente:")

segundo_numero = input("Por favor ingrese un segundo valor de verdad, recuerde que 0 es Falso y 1 es Verdadero:")

while segundo_numero != "0" and segundo_numero != "1":
    segundo_numero = input("El valor ingresado no es valido, por favor intente nuevamente:")

# Buscamos valor de verdad en valores ingresados por usuario
valor_verdad_primer_numero = convertir_a_booleano(primer_numero)
valor_verdad_segundo_numero = convertir_a_booleano(segundo_numero)

# Se realizan operaciones una vez obtenidos los valores de verdad
operaciones_booleanas(valor_verdad_primer_numero, valor_verdad_segundo_numero)