# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra: '))

texto_2 = str(input('Ingrese la segunda palabra: '))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda

# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda

# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda

# Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda

# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda

if texto_1 > texto_2:
    print("{} es mayor que {}".format(texto_1, texto_2))
elif texto_1 == texto_2:
    print("{} es igual que {}".format(texto_1, texto_2))
else:
    print("{} es mayor que {}".format(texto_2, texto_1))

if len(texto_1) > len(texto_2):
    print("{} tiene mas caracteres que {}".format(texto_1, texto_2))
elif texto_1 == texto_2:
    print("{} tiene la misma cantidad de caracteres que {}".format(texto_1, texto_2))
else:
    print("{} tiene mas caracteres que {}".format(texto_2, texto_1))

# El siguiente if lo resolví buscando en Google, no estaba en los ejemplos de clase.
if str.title(texto_1) > str.title(texto_2):
    print("La primer letra de {} es mayor que la de {}".format(texto_1, texto_2))
else:
    print("La primer letra de {} es mayor que la de {}".format(texto_2, texto_1))

copia_texto_1 = texto_1

if (copia_texto_1 == texto_1):
    print("Las palabras son iguales.")
# En este if no pongo un else porque "copia_texto_1" siempre va ser igual a "texto_1".
if (copia_texto_1 != texto_2):
    print("Las palabras son diferentes.")
else:
    print("Las palabras son iguales.")




