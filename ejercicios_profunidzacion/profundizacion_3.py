# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado

IMPORTANTE: Para ordenar las temperatuas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

temperatura1 = int(input("Ingrese una temperatura: "))

temperatura2 = int(input("Ingrese una temperatura: "))

temperatura3 = int(input("Ingrese una temperatura: "))

if (temperatura1 > temperatura2 and temperatura3):
    print("La temperatura más alta es: ",temperatura1)
elif (temperatura2 > temperatura1 and temperatura3):
    print("La temperatura más alta es: ",temperatura2)
elif (temperatura3 > temperatura1 and temperatura2):
    print("La temperatura más alta es: ",temperatura3)
else:
    print("Hay dos valores iguales.")

if (temperatura1 < temperatura2 and temperatura3):
    print("La temperatura más baja es: ", temperatura1)
elif (temperatura2 < temperatura1 and temperatura3):
    print("La temperatura más baja es: ", temperatura2)
elif (temperatura3 < temperatura1 and temperatura2):
    print("La temperatura más baja es: ", temperatura3)
else:
    print("Hay dos valoress iguales.")
promedio = ((temperatura1 + temperatura2 + temperatura3) / 3)

print("El promedio de las tres temperaturas es: ",round(promedio,2))
